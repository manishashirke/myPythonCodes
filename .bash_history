ssh-add ~/.ssh/id_rsa.pub 
git config --list
cd /mnt/
ls
cd c/
ls
cd Users/rotem/PycharmProjects/pythonProject/
ls
cp myFirstTest.py /home/vm1/
cd /home/vm1/
ls#
ls
git add myFirstTest.py 
ls
git init
git add myFirstTest.py 
git commit
lsb_release -a
sudo su
sudo apt-get update
sudo apt-get -y install openjdk-11-jdk openjdk-11-jre
java --version
sudo vim /etc/environment
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt update
sudo apt -y install jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins
sudo systemctl enable jenkins
sudo systemctl status jenkins
sudo service status jenkins
sudo service start jenkins
sudo service jenkins start
sudo service jenkins status
sudo service jenkins enable
sudo systemctl enable jenkins
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
ifconfig
sudo service jenkins status
sudo apt install git
git config --global user.name "manisha"\ngit config --global user.email "rote.manisha@gmail.com"
git config user.name "manisha"\ngit config user.email "rote.manisha@gmail.com"
git config --global user.name "manisha"
git config --global user.email "rote.manisha@gmail.com"
git config user.name "manisha"
ssh-keygen -t rsa -b 4096 -C "rote.manisha@gmail.com"
ssh-add ~/.ssh/id
ssh-add ~/.ssh/id_rsa.pub 
ssh-add ~/.ssh/id_rsa
ssh-add ~/.ssh/id
ssh-agent bash
