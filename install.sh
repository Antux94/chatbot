echo SHELL---------------------------------------------------------------------


#cd /mount/src/chatbot

wget https://download.java.net/java/GA/jdk11/9/GPL/openjdk-11.0.2_linux-x64_bin.tar.gz
tar -xvzf openjdk-11.0.2_linux-x64_bin.tar.gz




pwd
ls


export JAVA_HOME=jdk-11.0.2
export PATH=$JAVA_HOME/bin:$PATH


echo JAVA VERSION
java -version

cat /etc/os-release


#export M2_HOME=/mount/src/chatbot/apache-maven-3.5.3
#export PATH=$M2_HOME/bin:$PATH

#echo $JAVA_HOME
#echo $M2_HOME

#mvn -version

echo SHELL---------------------------------------------------------------------