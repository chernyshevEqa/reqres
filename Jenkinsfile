pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                bat 'C:\\Python39\\python.exe -m pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                bat 'C:\\Python39\\Scripts\\pytest tests/ --html=report.html'
            }
        }
    }
}