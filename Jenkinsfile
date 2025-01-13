pipeline {
    agent any  // Use any available agent for this pipeline

    environment {
        FRONTEND_IMAGE = "jefrey0/hello-world-frontend:latest"
        BACKEND_IMAGE = "jefrey0/hello-world-backend:latest"
        DOCKER_REGISTRY = "docker.io"  // Docker Hub
        DOCKER_CREDENTIALS = "dockerhub_id"  // Replace with your DockerHub credentials ID
    }

    stages {
        // Stage 1: Checkout the code from GitHub
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        // Stage 2: Build Docker images for frontend and backend
        stage('Build Docker Images') {
            steps {
                script {
                    // Build Docker images for frontend and backend using Docker Compose
                    sh 'docker-compose build --no-cache'
                }
            }
        }

        // Stage 3: Run tests (assuming you have test scripts for both backend and frontend)
        stage('Run Tests') {
            steps {
                script {
                    // Run backend tests using pytest (or your backend test tool)
                    sh 'docker-compose run backend pytest tests/'
                    // Run frontend tests (e.g., using npm or yarn)
                    sh 'docker-compose run frontend npm run test'
                }
            }
        }

        // Stage 4: Push Docker images to Docker Hub
        stage('Push Docker Images') {
            steps {
                script {
                    // Log in to Docker Hub using Jenkins credentials
                    docker.withRegistry("https://${DOCKER_REGISTRY}", "${DOCKER_CREDENTIALS}") {
                        // Push images to Docker Hub
                        sh 'docker-compose push'
                    }
                }
            }
        }

        // Stage 5: Deploy to the same EC2 instance using Docker Compose
        stage('Deploy to EC2') {
            steps {
                script {
                    // No SSH needed since we're deploying to the same EC2 instance where Jenkins is running.
                    // Docker Compose will deploy the containers on this same instance.

                    sh """
                        # Pull the latest images and deploy the containers
                        cd /path/to/your/docker-compose/directory && docker-compose pull && docker-compose up -d
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Clean up workspace after the pipeline is finished
        }
    }
}
