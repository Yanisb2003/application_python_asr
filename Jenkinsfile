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
                        configName: "AnsibleServet",
                        transfers: [sshTransfer(execCommand: 'touche /opt/docker/test.txt')],
                        verbose: true
                        )
                    ]
                )
            }
        }       
    }
}