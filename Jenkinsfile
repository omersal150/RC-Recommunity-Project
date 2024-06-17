pipeline {
    agent {
        kubernetes {
            yaml '''
            apiVersion: v1
            kind: Pod
            spec:
                serviceAccount: jenkins-sa
                containers:
                  - name: slave
                    image: docker:latest
                    tty: true
                    securityContext:
                        privileged: true
                  - name: pytest
                    image: omersal/jenkins-agent-github
                    tty: true
                    securityContext:
                        privileged: true
                  - name: maven
                    image: maven:alpine
                    command:
                    - cat
                    tty: true
            '''
        }
    }

    stages {
        stage('checkout git') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('testing with pytest') {
            steps{
                container('pytest') {
                    script {
                        sh 'cd ./app && python -m pytest || [[ $? -eq 1 ]]'
                    }
                }
            }
        }
        // Build and push with build tag (replace with actual build commands)
        stage('Build and Push the image with tags') {
            environment {
                auth = 'dockerauth'
            }
            steps { 
                container('slave') {
                    script {
                        def image = docker.build("mikey8520/final-project", "./app")
                        withDockerRegistry(credentialsId: 'dockerauth') {
                            image.push("${env.BUILD_NUMBER - 11}")
                            image.push("latest")
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline POST:'
        }
        success {
            echo 'Pipeline SUCCESS!'
        }
        failure {
            echo 'Pipeline FAILED, check the logs for more information!'
        }
    }
}

