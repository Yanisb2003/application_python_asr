pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                sshPublisher(
                    continueOnError: false, 
                    failOnError: true,
                    publishers: [
                        sshPublisherDesc(
                        configName: "AnsibleServer",
                        transfers: [
                            sshTransfer(
                                execCommand: 'touch /opt/docker/test.txt',
                                sourceFiles: '**/',
                                remoteDirectory: '/app_repo/'
                            )
                        ],
                        verbose: true
                        )
                    ]
                )
            }
        }       
    }
}