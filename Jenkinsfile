pipeline {
    agent any

    environment {
        FRONTEND_IMAGE = "jefrey0/hello-world-frontend:latest"
        BACKEND_IMAGE = "jefrey0/hello-world-backend:latest"
        DOCKER_REGISTRY = "docker.io"
        DOCKER_CREDENTIALS = "dockerhub_id" // Replace with your DockerHub credentials ID
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                script {
                    sh 'docker-compose build --no-cache'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'docker-compose run backend pytest'
                    sh 'docker-compose run frontend npm run test'
                }
            }
        }

        stage('Push Docker Images') {
            steps {
                script {
                    docker.withRegistry("https://${DOCKER_REGISTRY}", "${DOCKER_CREDENTIALS}") {
                        sh 'docker-compose push'
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    sh """
                        cd ${WORKSPACE}/hello-world-app
                        docker-compose pull
                        docker-compose up -d
                    """
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
