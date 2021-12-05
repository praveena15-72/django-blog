pipeline {
    agent any

    stages {

        stage('Init') {
            steps {
                deleteDir()
            }
        }
        stage('Checkout project') {
            steps {
                script {
                    git branch: "master",
                        url: 'https://github.com/praveena15-72/django-blog.git'
                }
            }
        }
        stage('Installing packages') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        
        stage('Unit Testing') {
                steps {
                    sh './manage.py test blog'
                }
        }


    }
    
    post {
        cleanup {
            deleteDir()
        }
    }
}
