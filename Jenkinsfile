pipeline {
    agent {
        kubernetes {
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: maven
    image: maven:alpine
    command:
    - cat
    tty: true
  - name: python
    image: python:3.9-alpine
    command:
    - cat
    tty: true
  - name: ez-docker-helm-build
    image: ezezeasy/ez-docker-helm-build:1.41
    imagePullPolicy: Always
    securityContext:
      privileged: true
"""
        }
    }

    environment {
        DOCKER_IMAGE = "omersal/rc-recommunity"
        DOCKER_CREDENTIALS = "rc-recommunity-id"
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/omersal150/RC-Recommunity-Project.git']]])
                }
            }
        }

        stage('Build and Run Python Container') {
            steps {
                container('ez-docker-helm-build') {
                    script {
                        sh "docker build -t ${DOCKER_IMAGE}:latest ./rc-recommunity"
                    }
                }
            }
        }

        stage('Build and Push Docker Images') {
            when {
                branch 'main'
            }
            steps {
                container('ez-docker-helm-build') {
                    script {
                        withDockerRegistry(credentialsId: DOCKER_CREDENTIALS) {
                            sh "docker push ${DOCKER_IMAGE}:latest"
                        }
                    }
                }
            }
        }
    }
}
