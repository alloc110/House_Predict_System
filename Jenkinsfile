pipeline {
    agent any

    environment {
        GEMINI_KEY = credentials('gemini-api-key-id')
        APP_NAME = "house-predict"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Deploy') {
           
            steps {
                sscript {
            // Bước 1: Dừng toàn bộ các container cũ thuộc project này
            // --remove-orphans: Xóa cả những container "mồ côi" không còn nằm trong file yml
            sh 'docker compose down --remove-orphans'
            
            // Bước 2: Khởi động lại với cờ --force-recreate
            // Điều này đảm bảo Docker sẽ xóa container cũ đi nếu nó còn sót lại
            sh 'docker compose up -d --build --force-recreate'
        }
            }
        }
    }
}