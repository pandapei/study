import paramiko
import zipfile
import os
from scp import SCPClient

def scandir(dirs, uplod, ssh):
    for f in os.listdir(dirs):
        _f = dirs + "/" + f
        _uplod = uplod + "/" + f
        if os.path.isdir(_f):
            ssh.exec_command("mkdir " + _uplod)
            scandir(_f, _uplod, ssh)
        elif os.path.isfile(_f):
            scpclient = SCPClient(ssh.get_transport(), socket_timeout=15.0)
            scpclient.put(_f, _uplod)
    pass

unzip = zipfile.ZipFile("/home/shiyanlou/Desktop/demo/demo_war.war")
for file in unzip.namelist():
    display = unzip.extract(file, "/home/shiyanlou/Desktop/demo/demo")
    print(display)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("127.0.0.1", 22, "shiyanlou", "65896390")

ssh.exec_command("mkdir /home/shiyanlou/Desktop/apache-tomcat-9.0.0.M17/webapps/demo")

scandir("/home/shiyanlou/Desktop/demo/demo", "/home/shiyanlou/Desktop/apache-tomcat-9.0.0.M17/webapps/demo", ssh)

(stdin, stdout, stderr)=ssh.exec_command("/home/shiyanlou/Desktop/tomcat.sh restart")
print(stdout.readlines())


ssh.close()
