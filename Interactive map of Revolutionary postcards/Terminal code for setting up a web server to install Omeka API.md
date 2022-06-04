### Setting Up Linux Machine in Amazon Web Services (AWS)

###### 1. Choose a Linux Machine - Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type

###### 2. Connecting to the EC2 Instance Using SSH and Upgrading Linux

###### PowerShell 7: 

cd .ssh
C:\Users\username\.ssh>icacls.exe lamp-omeka.pem /reset
icacls.exe lamp-omeka.pem /grant:r "$($env:username):(r)"
icacls.exe lamp-omeka.pem /inheritance:r

###### 3. To connect to your instance using SSH:

ssh ec2-user@Public.IP.Address -i lamp-omeka.pem

###### 4. Upgrading the Linux version and its packages

sudo yum update -y

###### 5. Installing the Apache server

sudo yum install httpd24 -y
httpd -v
sudo service httpd start
chkconfig httpd on

###### 6. Create a sample HTML page

cd /var/www/html
sudo apt install nano
sudo nano index.html
###### Paste the Public DNS in the web browser URL input box. You should see the same output as follows.

###### 7. Installing the MySQL server

sudo yum install mysql-server
mysqladmin -V
service mysqld start
sudo chkconfig mysqld on
mysqladmin -u root password

###### 8. Setting up the MySQL secure installation

mysql_secure_installation
Remove the anonymous users -y
Disallow remote root login -y
Remove the test database and access to it -y
Reload privileges tables -y
Sudo service mysqld restart

###### 9.	Creating Database and User for Omeka Application

mysql -u root -p
CREATE DATABASE omeka;
SHOW DATABASES;
CREATE USER 'galkins'@'localhost' IDENTIFIED BY 'Nikita123!';
SELECT user, authentication_string, plugin, host FROM mysql.user;
GRANT ALL ON omeka.* TO 'galkins'@'localhost' IDENTIFIED BY 'Nikita123!' WITH GRANT OPTION;
FLUSH PRIVILEGES;
show grants for 'galkins'@'localhost'

###### 10.	Authorization on the Omeka platform

###### Open a browser and enter URL =  http://Public.IP.Address/omeka/admin
###### Username = galkins
###### Password = Nikita123