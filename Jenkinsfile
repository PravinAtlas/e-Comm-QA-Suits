pipeline {
    agent any
    stages {
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/galaxydevelopers/e-Comm-QA-Suite.git', branch: 'master'
            }
        }
        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Behave Tests') {
            steps {
                sh '''
                source venv/bin/activate
                behave
                '''
            }
        }
    }
}
