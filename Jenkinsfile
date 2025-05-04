pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }
    }
}