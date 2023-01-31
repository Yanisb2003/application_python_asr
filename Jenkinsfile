pipeline {
    agent 
    stages {
        stage('Connect to Ansible Server') {
            steps {
                sshPublisher(
                    configName: 'AnsibleServer',
                    transfers: [
                        transferSet: [
                            sshTransfer(
                                execCommand: 'touch /opt/docker/test.txt',
                                execTimeout: 300,
                                usePty: false
                            )
                        ]
                    ]    
                )
            }
        }
    }
}