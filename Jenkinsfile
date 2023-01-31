pipeline {
    agent any
    stages {
        stage('Connect to Ansible Server') {
            steps {
                sshPublisher(
                    configName: 'AnsibleServer',
                    transferSet: [
                        sshTransfer(
                            execCommand: 'touch /opt/docker/test.txt',
                            execTimeout: 300
                        )
                    ]
                )
            }
        }
    }
}