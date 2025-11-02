pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/teju8477/quote_of_the_day.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("quote-app")
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker stop quote_container || true'
                    sh 'docker rm quote_container || true'
                    sh 'docker run -d -p 5000:5000 --name quote_container quote-app'
                }
            }
        }
    }
}
