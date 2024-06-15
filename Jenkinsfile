pipeline {
    agent any
    
    stages {
        stage('Check MongoDB Inputs - Feature Branch') {
            when {
                branch 'feature'
            }
            steps {
                script {
                    echo 'Checking MongoDB inputs for the feature branch...'
                    // Connect to MongoDB and check inputs
                    def mongoClient = new MongoClient('mongo-service.mongo-namespace', 27017)
                    def db = mongoClient.getDatabase('rc_recommunity')
                    def modelsCollection = db.getCollection('models')
                    def commentsCollection = db.getCollection('comments')
                    def usersCollection = db.getCollection('users')
                    
                    def newModelsCount = modelsCollection.countDocuments()
                    def newCommentsCount = commentsCollection.countDocuments()
                    def newUsersCount = usersCollection.countDocuments()
                    
                    if (newModelsCount > 0 && newCommentsCount > 0 && newUsersCount > 0) {
                        echo 'MongoDB inputs check passed for the feature branch.'
                    } else {
                        error 'MongoDB inputs check failed for the feature branch.'
                    }
                }
            }
        }

        stage('Check GitHub Push - Feature Branch') {
            when {
                branch 'feature'
            }
            steps {
                script {
                    echo 'Checking GitHub push for the feature branch...'
                    // Clone the repository and check for specific files or changes
                    git 'https://github.com/omersal150/RC-Recommunity-Project.git'
                    if (fileExists('app.py')) {
                        echo 'GitHub push check passed for the feature branch.'
                    } else {
                        error 'GitHub push check failed for the feature branch.'
                    }
                }
            }
        }

        stage('Check MongoDB Inputs - Main Branch') {
            when {
                branch 'main'
            }
            steps {
                script {
                    echo 'Checking MongoDB inputs for the main branch...'
                    // Connect to MongoDB and check inputs
                    def mongoClient = new MongoClient('mongo-service.mongo-namespace', 27017)
                    def db = mongoClient.getDatabase('rc_recommunity')
                    def modelsCollection = db.getCollection('models')
                    def commentsCollection = db.getCollection('comments')
                    def usersCollection = db.getCollection('users')
                    
                    def newModelsCount = modelsCollection.countDocuments()
                    def newCommentsCount = commentsCollection.countDocuments()
                    def newUsersCount = usersCollection.countDocuments()
                    
                    if (newModelsCount > 0 && newCommentsCount > 0 && newUsersCount > 0) {
                        echo 'MongoDB inputs check passed for the main branch.'
                    } else {
                        error 'MongoDB inputs check failed for the main branch.'
                    }
                }
            }
        }

        stage('Check GitHub Push - Main Branch') {
            when {
                branch 'main'
            }
            steps {
                script {
                    echo 'Checking GitHub push for the main branch...'
                    // Clone the repository and check for specific files or changes
                    git 'https://github.com/omersal150/RC-Recommunity-Project.git'
                    if (fileExists('app.py')) {
                        echo 'GitHub push check passed for the main branch.'
                    } else {
                        error 'GitHub push check failed for the main branch.'
                    }
                }
            }
        }

        // Add more stages for building, testing, deploying, etc.
    }
}
