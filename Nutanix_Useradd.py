import paramiko
import json

IP = "172.29.161.60"
username = "admin"
Password = "Peg-12345!"
print("How many users do you want to create?")
num = int(input(""))
#print(num)


def exec_command(ip, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=password, timeout=3.0)
    (stdin, stdout, stderr) = client.exec_command(command)
    output = stdout.read().decode()
    client.close()
    return output


#ユーザー追加
n=1
for n in range(num):
    if n < 9:
        a = "0"+str(n+1)
        loginuser = 'DIS-NTNX-'+a
        adduser = "source /etc/profile; ncli user add user-name="+loginuser+" user-password='Nutanix/4u123' first-name='DIS' last-name='Tarou' email-id=test@gmail.com"
        addrole = "source /etc/profile; ncli user grant-user-admin-role user-name="+loginuser
        print(exec_command(IP, username, Password,adduser))
        print(exec_command(IP, username, Password,addrole))
    elif n >= 9:
        a = str(n+1)
        loginuser = 'DIS-NTNX-'+a
        adduser = "source /etc/profile; ncli user add user-name="+loginuser+" user-password='Nutanix/4u123' first-name='DIS' last-name='Tarou' email-id=test@gmail.com"
        addrole = "source /etc/profile; ncli user grant-user-admin-role user-name="+loginuser
        print(exec_command(IP, username, Password,adduser))
        print(exec_command(IP, username, Password,addrole))

#print(exec_command(IP, username, Password,"source /etc/profile; ncli user add user-name='DIS-NTNX-01' user-password='Nutanix/4u123' first-name='DIS' last-name='Tarou' email-id=test@gmail.com"))
#print(exec_command(IP, username, Password,"source /etc/profile; ncli user grant-user-admin-role user-name='DIS-NTNX-01'"))


