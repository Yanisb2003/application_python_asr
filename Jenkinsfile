pipeline {
    agent any

    environment {
    SONAR_CREDENTIAL_ID = 'Projet_Python'
    }
    
    stages {
        stage('sonar') {
            steps {
                script {
                    def scannerHome = tool 'sonar_python'
                    withCredentials([string(credentialsId : "$SONAR_CREDENTIAL_ID" ,variable : 'SONAR_TOKEN' ,)]) {
                        withSonarQubeEnv('sonar_python') {
                            sh "${scannerHome}/bin/sonar-scanner -Dsonar.login=$SONAR_TOKEN"
                        }
                    }
                }
            }
        }

        // stage('run ansible') {
        //     steps {
        //         sshPublisher(
        //             continueOnError: false, 
        //             failOnError: true,
        //             publishers: [
        //                 sshPublisherDesc(
        //                 configName: "AnsibleServer",
        //                 transfers: [
        //                     sshTransfer(
        //                         sourceFiles: '**/',
        //                         remoteDirectory: '/app_repo/',
        //                         execCommand: 'ansible-playbook -i /opt/docker/hosts.ini /opt/docker/ansible-playbook-local.yml'
        //                     ),
        //                     sshTransfer(
        //                         execCommand: 'ansible-playbook -i /opt/docker/hosts.ini /opt/docker/ansible-playbook-remote.yml'
        //                     )
        //                 ],
        //                 verbose: true
        //                 )
        //             ]
        //         )
        //     }
        // }       
    }
}
