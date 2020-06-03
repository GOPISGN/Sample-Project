pipeline {
	agent any
     
	stages {
		
		stage('Build') {
			steps {
				git 'https://github.com/GOPISGN/Sample-Project.git'
			}
		}

		stage('Stage 1 : Check Python Installed or not -- Pre-requestic') {
			steps {
				bat 'echo off'
				echo "Check Python Version"
				bat 'python --version'
				echo "Python latest version is installed, up and running"
				bat 'echo on'
                           
            }
        }
		
		stage('Unit Test') {
			parallel {
				
				stage('Stage 2 : Run the test for positive scenario') {
					steps {
						bat 'echo "Lets run the test for positive scenario"'
						bat 'python Sample.py "5"'
						bat 'echo "Testcase for positive scenario is successful"'
					}
				}
				stage('Sleep') {
					steps {
						bat 'waitfor SomethingThatIsNeverHappening /t 5 >nul 2>&1'
						bat 'echo "Waited for 5 seconds"'
					}
				}
				stage('Stage 3: Run the test for negative scenario') {
					steps {
						bat 'echo "Lets run the test for negative scenario"'
						bat 'python Sample.py "-1"'
						bat 'echo "Testcase for negative scenario is successful"'
					}
				}
				
				stage('Stage 4 : Run the test for exception') {
					steps {
						bat 'echo "Lets run the test for exception scenario"'
						bat 'python Sample.py "string"'
						bat 'echo "Testcase for exception scenario is successful"'
					}
				}
			}
		}
	}
	post {
		always {
			bat 'echo "Cleanup the workspace"'
		}
		success {
			bat 'echo "Run Success"'
		}
		unstable {
			bat 'echo "Run is Unstable"'
		}
		failure {
			bat 'echo "Run Failed"'
		}
	}
}
