pipeline {
    agent any

    environment {
        DOCKER_USERNAME = 'jefrey0'
        DOCKER_PASSWORD = 'dckr_pat_GGrPK8NZV8xY_x8o7nkqLLReYNE'
        REACT_IMAGE = 'jefrey0/react-app'
        FLASK_IMAGE = 'jefrey0/flask-app'
        REACT_TAG = 'latest'
        FLASK_TAG = 'latest'
        
        SSH_PRIVATE_KEY = '''-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAoq076wDRvbbWmvNnRUXYZi2CABVQee8QdrcHwJE6SApL/0Sv
mahZKYxTIfCGO5VjE0SsRGgwNkbR3+P01gu6TIXUEvUtcrkFQxwWT7rGjs163kjq
UYduhr+silVfh6RVdif7VTenmMwTxOYVh2jVCQrlYIvUeFVobpxir+7A5OzLF2Nl
kq37Ra1PaYmL9fR7XSLlBC1c3i2fbUSb974oZC0GJRvsNfU2zYB6m8RxYBb1Hs7D
iEkiLUE/qN+Oy+4pLL4lMnq4VdBOfL3XsggpNEqzBrbHPJOBiTTj6q+eIEkcUvmw
nSWcugAs6dJ8Jsl+lAD+NZ5qz+zI8QKdMxCVFQIDAQABAoIBAE1aaIJvikxWs6dM
lE+ZTbQQcZ+OgwzoA4EfuTz1EayN0ONaCtHa/kLGagVadMnCWDEiV3PTwxEcDdIT
eCmLvBOFE3nMQccqeXkW0vkojB/9Ty6Bp4ILDyBd5jKFM/6wwr6DdnxoEXaTm9bl
vVj9HUfGeZm2A9sQaa8nB7o2olx4BkdhuKclcekeQtBJHL49+milZoLZTQoZER7a
7L4ftkb0vE1isi6GYfqmGvhEmecUrgjBTUrYfUGuFCTBhKlUxTQRlnTwGE1llHGr
FYZWeQDDkWYgsfC/PjcGmRda5+ScMWAY1N9gyRCFYrg3NtZr+K+yMW2FIQc9uwPB
n8xZdCECgYEA0++4cHYBTkb/b9vnxBdcV2tSgwtkogFXhbKsEklBRk4q3gHWV8O2
QDu98npwiA8HhVg59davMfMe2PTXmr6SaLFCUYHDfiTred8/7TZwB4cN3e2/Z7PX
4ik9+zmGUNrBQJOQmqW1HTew2lywcx3fadztCV/Bf7V7Gbxr6RPXL0kCgYEAxH+s
d/4OkE3LkhDsMNgsLNxd1VCT9WHRWbtJGFlN2Ydfn5sLbBGAxLJW4QdILd03tpN7
ZP54O2AVlmI67FTZT9EVmMTYiWDYVCx1iQKIIE2JtLE+nKphJwqOV0XVhklqZmVZ
Yy9DJfsY/MIrL6we6wcEkaSo1v2BTHu7gG0O220CgYBGwanaIgudjqaJOenO1d3G
cdZCWfNnAvutb1FzaXGZf09gf0yIUJbwKwHnimk3g40HP8VaBirHiluqI1Q4HZfT
zBpQC/qwirLzJU26bIpKeRRwG4fjn29b2lkPHs1xARez75A/kUM+VfF9daSTSk3k
khWxI37+nCBVH0sHrdARwQKBgBYUUojZH0HPvAQZqrCCWdRgnpqNh1KXPzLZ/Iij
4D+FGpWQkmP+Q33WnDSE4PNmXBBD2iWrAk+JqGNRflV340M4tziHRd2J6ETtCffv
NOSMUeDf2a0459m/MedUjX2dWjtPQBAJC36FDHW6S6f7qy21iCnlWqNtsM2rSZJQ
rs6xAoGARYepaC6r9JnpXZyVJR2bMwSlJlBNPZyiigBikBxhXI6hgeMJPM+WyB05
tZrOwctrY6m55aNDL3SiGCwaSgAC+vJ+hcKlXMZvRwpJBt1h15MGXOCSFIs1QP7W
vW+kmEZ0QRElucMqTtPDUoMdlnEbcqXl7r6H6s5i6XSPrf3OJtU=
-----END RSA PRIVATE KEY-----'''
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
                    sh '''
                    echo "$SSH_PRIVATE_KEY" > /tmp/aws-key.pem
                    chmod 600 /tmp/aws-key.pem
                    ssh -o StrictHostKeyChecking=no -i /tmp/aws-key.pem ec2-user@35.154.252.53 << 'EOF'
                    docker-compose down
                    docker-compose pull
                    docker-compose up -d
                    EOF
                    rm -f /tmp/aws-key.pem
                    '''
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
