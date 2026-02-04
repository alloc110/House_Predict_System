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
                script {
          echo "--- Đang dọn dẹp hệ thống cũ để tránh xung đột ---"
            // 1. Dừng và xóa các container, network cũ thuộc dự án này
            // --remove-orphans: Xóa cả những container cũ không còn khai báo trong file yml
            sh 'docker-compose down --remove-orphans'

            echo "--- Đang build và khởi động hệ thống mới ---"
            // 2. Build lại image và ép buộc tạo mới container (ngăn lỗi Conflict)
            sh 'docker-compose up -d --build --force-recreate'
        }
            }
        }
    }
}