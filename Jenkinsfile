pipeline {
	agent any
     
	stages {
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
						bat 'python Hello.py "5"'
						bat 'echo "Testcase for positive scenario is successful"'
					}
				}
				
				stage('Stage 3: Run the test for negative scenario') {
					steps {
						bat 'echo "Lets run the test for negative scenario"'
						bat 'python Hello.py "-1"'
						bat 'echo "Testcase for negative scenario is successful"'
					}
				}
				
				stage('Stage 4 : Run the test for exception') {
					steps {
						bat 'echo "Lets run the test for exception scenario"'
						bat 'python Hello.py "string"'
						bat 'echo "Testcase for exception scenario is successful"'
					}
				}
			}
		}
	}
}
