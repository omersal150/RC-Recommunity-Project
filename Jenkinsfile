pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your GitHub repository
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/omersal150/RC-Recommunity-Project.git']]])
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Ensure pytest is installed
                    sh 'pip install pytest'
                    // Run pytest
                    sh 'pytest tests'
                }
            }
        }
        stage('Build docker image') {
            steps {
                script {
                    sh 'docker build -t omersal/rc-recommunity .'
                }
            }
        }
        stage('Push image to Hub') {
            steps {
                script {
                    withCredentials([string(credentialsId: 'dockerhub-pwd', variable: 'dockerhubpwd')]) {
                        sh 'docker login -u omersal -p ${dockerhubpwd}'
                    }
                    sh 'docker push omersal/rc-recommunity'
                }
            }
        }
        stage('Deploy to k8s') {
            steps {
                script {
                    kubernetesDeploy(configs: 'deploymentservice.yaml', kubeconfigId: 'k8sconfigpwd')
                }
            }
        }
    }
}
