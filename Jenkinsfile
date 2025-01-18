pipeline {
    agent any

    environment {
        DOCKER_USERNAME = 'jefrey0'                  
        DOCKER_PASSWORD = 'dckr_pat_GGrPK8NZV8xY_x8o7nkqLLReYNE'
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

        stage('Tag and Push Docker Images') {
            parallel {
                stage('Push ReactJS Image') {
                    steps {
                        script {
                            sh '''
                            docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}
                            docker push ${REACT_IMAGE}:${REACT_TAG}
                            '''
                        }
                    }
                }
                stage('Push Flask Image') {
                    steps {
                        script {
                            sh '''
                            docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}
                            docker push ${FLASK_IMAGE}:${FLASK_TAG}
                            '''
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
