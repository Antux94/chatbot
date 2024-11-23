echo hello

cd /workspaces/chatbot
pwd

export JAVA_HOME=jdk1.8.0_202
export PATH=$JAVA_HOME/bin:$PATH

export M2_HOME=apache-maven-3.5.3
export PATH=$M2_HOME/bin:$PATH

mvn -version