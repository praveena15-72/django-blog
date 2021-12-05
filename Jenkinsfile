pipeline {
    agent any

   
    stages {

            stage('Init') {
            steps {
                deleteDir()

                script {
                     sh 'pip install -r requirements.txt'
             
                }
            }
        }
        stage('Test') {
            steps {
                sh 'python app/manage.py test'
            }
        } 
        
        stage('Deploy') {
                steps {
                    sh 'echo not yet...'
                }
        }


    }
    
    post {
        cleanup {
            deleteDir()
        }
    }