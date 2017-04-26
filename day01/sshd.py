# -*- coding: UTF-8 -*-
import paramiko

transport = paramiko.Transport(('192.168.56.102', 22))
# 连接服务器
transport.connect(username='weblogic', password='centos')

# 创建SSH对象
ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('hostname')
#打印命令结果
print stdout.read()

# 关闭连接
transport.close()