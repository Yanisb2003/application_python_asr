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
                            command: 'ansible-playbook -i /opt/docker/hosts.ini /opt/docker/ansible-playbook-local.yml',
                            usePty: false
                        )
                    ]
                )
            }
        }
    }
}