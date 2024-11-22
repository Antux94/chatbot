apt-get update
apt-get install -y openjdk-8-jdk
wget https://archive.apache.org/dist/maven/maven-3/3.5.3/binaries/apache-maven-3.5.3-bin.tar.gz
tar -xvzf apache-maven-3.5.3-bin.tar.gz
export M2_HOME=/content/apache-maven-3.5.3
export PATH=$PATH:$M2_HOME/bin
v