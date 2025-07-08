pipeline {
    agent any
    
    environment {
        IMAGE_NAME = 'krishnaregistry/newpythonapp'
        IMAGE_TAG = "${BUILD_NUMBER}"
        REGISTRY_CREDENTIAL = 'docker-hub-credentials'
    }

    stages {
        stage('Checkout Main Branch') {
            steps {
                git branch: 'main', url: 'https://github.com/ksai7991/CI-Python-App.git'
            }
        }

        stage('Docker Login and Build') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:${IMAGE_TAG}")
                }
            }
        }

        stage('Pushing Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.digitalocean.com/', REGISTRY_CREDENTIAL) {
                        dockerImage.push("${IMAGE_TAG}")
                    }
                }
            }
        }
stage('Update Deployment and Push to GitHub') {
    steps {
        withCredentials([string(credentialsId: 'Githubtoken', variable: 'GITHUB_TOKEN')]) {
            sh '''
                git config --global user.name "krishna"
                git config --global user.email "ksai7991@gmail.com"

                # Clean up previous clone if exists
                rm -rf CD-Python-App || true

                # Clone the repo using token
                git clone https://$GITHUB_TOKEN@github.com/ksai7991/CD-Python-App.git
                cd CD-Python-App

                # Update the image in deployment.yaml
                yq e '.spec.template.spec.containers[].image = "registry.digitalocean.com/krishnaregistry/newpythonapp:'"$BUILD_NUMBER"'"' -i deployment.yaml

                git add deployment.yaml
                git commit -m "Update image to build ${BUILD_NUMBER}" || echo "No changes to commit"
                git push origin main
            '''
        }
    }
}

       
    }
}
