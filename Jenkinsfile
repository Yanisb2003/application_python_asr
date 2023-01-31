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
                                sourceFiles: '**/',
                                remoteDirectory: '/app_repo/',
                                execCommand: 'ansible-playbook -i /opt/docker/hosts.ini /opt/docker/ansible-playbook-local.yml',
                                execCommand: 'ansible-playbook -i /opt/docker/hosts.ini /opt/docker/ansible-playbook-remote.yml'
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