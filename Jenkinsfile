pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub_id')
        AWS_KEY = credentials('aws-key')
        REPO_URL = 'https://github.com/jefrey007/hello-world-app.git'
        REACT_IMAGE = 'jefrey0/react-app'
        FLASK_IMAGE = 'jefrey0/flask-app'
        REACT_TAG = 'latest'
        FLASK_TAG = 'latest' 
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    echo 'Cloning Repository...'
                }
                checkout scm 
            }
        }

        stage('Build Docker Images') {
            parallel {
                stage('Build ReactJS Image') {
                    steps {
                        script {
                            sh '''
                            cd frontend 
                            docker build -t ${REACT_IMAGE}:${REACT_TAG} .
                            '''
                        }
                    }
                }
                stage('Build Flask Image') {
                    steps {
                        script {
                            sh '''
                            cd backend 
                            docker build -t ${FLASK_IMAGE}:${FLASK_TAG} .
                            '''
                        }
                    }
                }
            }
        }

        stage('Run Unit Tests') {
            parallel {
                stage('Run ReactJS Unit Tests') {
                    steps {
                        script {
                            sh '''
                            cd frontend 
                            npm install 
                            npm test 
                            '''
                        }
                    }
                }
                stage('Run Flask Unit Tests') {
                    steps {
                        script {
                            sh '''
                            cd backend 
                            pytest 
                            '''
                        }
                    }
                }
            }
        }

        stage('Tag and Push Docker Images') {
            parallel {
                stage('Push ReactJS Image') {
                    steps {
                        script {
                            docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_id') {
                                sh '''
                                docker push ${REACT_IMAGE}:${REACT_TAG} 
                                '''
                            }
                        }
                    }
                }
                stage('Push Flask Image') {
                    steps {
                        script {
                            docker.withRegistry('https://registry.hub.docker.com', 'dockerhub_id') {
                                sh '''
                                docker push ${FLASK_IMAGE}:${FLASK_TAG}
                                '''
                            }
                        }
                    }
                }
            }
        }

        stage('Deploy to AWS') {
            steps {
                script {
                    sshagent(['aws-key']) { 
                        sh '''
                        ssh -o StrictHostKeyChecking=no ec2-user@35.154.252.53 << EOF                      
                        docker-compose down 
                        docker-compose pull 
                        docker-compose up -d 
                        EOF
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}
