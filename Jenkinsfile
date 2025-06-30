pipeline {
    agent any
    stages {
        REMOVE THIS STAGE:
        stage('Clone Repo') {
            steps {
                git url: 'https://github.com/PravinAtlas/e-Comm-QA-Suits.git', branch: 'master'
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
