pipeline {
    agent any  // Run on any available agent

    environment {
        FRONTEND_IMAGE = "jefrey0/hello-world-frontend:latest"
        BACKEND_IMAGE = "jefrey0/hello-world-backend:latest"
        DOCKER_REGISTRY = "docker.io"  // Docker Hub
        DOCKER_CREDENTIALS = "dockerhub_id"  
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
                    // Build Docker images for frontend and backend
                    sh 'docker-compose build --no-cache'
                }
            }
        }

        // Stage 3: Run tests (Example, assuming you have test scripts)
        stage('Run Tests') {
            steps {
                script {
                    // Run backend tests with pytest
                    sh 'docker-compose run backend pytest tests/'
                    // Run frontend tests with npm
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

        // Stage 5: Deploy to AWS EC2 using Docker Compose (example)
        stage('Deploy to AWS EC2') {
            steps {
                script {
                    // SSH into AWS EC2 and deploy using Docker Compose
                    sh """
                    ssh -i /var/lib/jenkins/.ssh/private-key.pem ec2-user@your-ec2-ip 'cd /path/to/app && docker-compose pull && docker-compose up -d'
                    """
                }
            }
        }
    }

    post {
        // Always run this after the pipeline execution (e.g., cleanup)
        always {
            cleanWs() // Clean up workspace
        }
    }
}
