pipeline {
    agent { label 'python-chrome' }

    options {
        timestamps()
        disableConcurrentBuilds()
    }

    environment {
        // Jenkins agents run without a display; the driver factory
        // reads this via automation.utils.config.
        HEADLESS = 'true'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv .venv'
                sh '. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
            }
        }
        stage('Run smoke tests') {
            steps {
                sh '. .venv/bin/activate && pytest -m smoke --junitxml=reports/junit.xml --html=reports/jenkins-report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/junit.xml'
            archiveArtifacts artifacts: 'reports/**, screenshots/**', allowEmptyArchive: true
        }
    }
}
