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
                    sh 'python3 manage.py test blog'
                }
        }
         stage('Docker Build and Tag') {
           steps {
              
                sh 'docker build -t django:latest .' 
                  sh 'docker tag django praveena/django:latest'
           
               
          }
        }
         stage('Publish image to Docker Hub') {
          
            steps {
        withDockerRegistry([ credentialsId: "dockerHub", url: "" ]) {
          sh  'docker push praveena/django:latest'
          sh  'docker push praveena/django:$BUILD_NUMBER' 
        }
                  
          }
        }


    }
    
    post {
        cleanup {
            deleteDir()
        }
    }
}
