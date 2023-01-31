pipeline {
    agent any
    stages {
        stage('Connect to Ansible Server') {
            steps {
                sshPublishers(
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