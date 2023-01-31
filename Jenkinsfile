pipeline {
    agent any
    environment {
        SONAR_CREDENTIAL_ID = 'sonar-token'
    }

    stages {
//     stage('sonar') {
//       steps {
//         script {
//           def scannerHome = tool 'sonar'
//           withCredentials([string(credentialsId : "$SONAR_CREDENTIAL_ID" ,variable : 'SONAR_TOKEN' ,)]) {
//             withSonarQubeEnv('sonar') {
//               sh '''pip install coverage pylint
//   cd /src
//   coverage erase
//   coverage run unit_test.py
//   coverage xml -i
//   '''
//               sh "${scannerHome}/bin/sonar-scanner -Dsonar.login=$SONAR_TOKEN"
//             }
//           }
//         }
//       }
//       post {
//         success {
//         }
//         failure {
//           script {
//             error 'Failed, exiting now...'
//           }
//         }
//         aborted {
//         }
//         unstable {
//           script {
//             error 'Unstable, exiting now...'
//           }
//         }
//       }
//     }

        stage('Connect to Ansible Server') {
            steps {
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'AnsibleServer',
                            transfer: [
                                sshTransfer(
                                    execCommand: 'ansible-playbook /opt/docker/ansible-playbook-ping.yml',
                                    execTimeout: 300,
                                    usePty: false
                                )
                            ]
                        )
                    ]
                )
            }
        }
    }
}
