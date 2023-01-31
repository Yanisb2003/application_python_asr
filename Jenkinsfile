pipeline {
    agent any
    stages {
        stage('Connect to Ansible Server') {
            steps {
                sshPublisher(
                    configName: 'AnsibleServer',
                    publishOver: 'SSH',
                    usePublishers: true,
                    sshPublisherDesc: [
                        sshPublisherDesc(
                            configName: 'AnsibleServer',
                            command: 'touch /opt/docker/test.txt',
                            usePty: false
                        )
                    ]
                )
            }
        }
    }
}
