echo hello


#cd /mount/src/chatbot

pwd

export JAVA_HOME=/mount/src/chatbot/jdk1.8.0_202
export PATH=$JAVA_HOME/bin:$PATH

export M2_HOME=/mount/src/chatbot/apache-maven-3.5.3
export PATH=$M2_HOME/bin:$PATH

echo $JAVA_HOME
echo $M2_HOME

mvn -version