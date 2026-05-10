pipeline {
    agent any
    triggers {
        githubPush()
    }
    options {
        disableConcurrentBuilds(abortPrevious: true)
    }
    triggers {
        GenericTrigger(
            genericVariables: [
                [key: 'isMerged', value: '$.pull_request.merged']
            ],
            regexpFilterText: '$isMerged',
            regexpFilterExpression: 'true'
        )
    }
    stages {
        stage('Setup Variables') {
            steps {
                script {
                    env.REPO_NAME = env.GIT_URL.tokenize('/').last().split("\\.")[0]
                }
            }
        }
        stage('Deploy') {
            when { branch 'main' }
            steps {
                withCredentials([
                    file(credentialsId: "${env.REPO_NAME}-env", variable: 'ENV_SECRET')
                ]) {
                    script {
                        sh "mkdir -p plugins"
                        sh "touch plugins/__init__.py"

                        sh "[ -f requirements.txt ] && sed -i 's/\\r\$//' requirements.txt"
                        sh "[ -f '${ENV_SECRET}' ] && cp '${ENV_SECRET}' .env && sed -i 's/\\r\$//' .env"

                        sh '''
                        if [ -f docker-compose.yml ]; then
                            # We use down to ensure old "stale" file-mount handles are released
                            docker compose down
                            docker compose up -d --build
                        else
                            echo "No docker-compose.yml found, skipping..."
                            exit 0
                        fi
                        '''

                        sh "[ -f .env ] && rm .env"
                    }
                }
            }
        }
    }
    post {
        success { echo '🚀 Deployment successful!' }
        failure { echo '❌ Deployment failed. Check the logs.' }
    }
}
