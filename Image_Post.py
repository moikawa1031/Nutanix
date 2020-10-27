import paramiko,json,requests,urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

#パラメーター
user = "admin"
old_password = "nutanix/4u"
new_password = "Peg-12345!"
user_name="Masaru Oikawa"
company_name="DIS"
job_title="Systems Engineer"
IP = "172.29.161.60"
virtio = "http://172.29.30.11/iso/Nutanix-VirtIO-1.1.5.iso"
centiso = "http://172.29.30.11/iso/CentOS-7-x86_64-DVD-1810.iso"
centvm = "http://172.29.30.11/iso/centos7-1.qcow2"
winsviso = "http://172.29.30.11/iso/ja_windows_server_2019_x64_dvd_260a1d93.iso"

def exec_command(ip, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=password, timeout=3.0)
    (stdin, stdout, stderr) = client.exec_command(command)
    output = stdout.read().decode()
    client.close()
    return output

#ncliをjsonで出力
container = exec_command(IP, user, new_password,"source /etc/profile; ncli container list --json=true")
containerdict = json.loads(container)
#print(containerdict)
containernames =  containerdict["data"]
for i in containernames:
    if "default" in i["name"]:
        container_name = i["name"]
        container_uuid = i["containerUuid"]
        #print(i["name"])
    #print(i["name"])
#print(container_name)
print(container_uuid)

virtio_dict = {
    "name": "VirtIO-1.1.5",
    "annotation": "",
    "imageType": "ISO_IMAGE",
    "imageImportSpec": {
    "containerUuid": container_uuid,
    "url": virtio,
    }
}

centiso_dict = {
    "name": "CentOS_ISO",
    "annotation": "",
    "imageType": "ISO_IMAGE",
    "imageImportSpec": {
    "containerUuid": container_uuid,
    "url": centiso,
    }
}

centvm_dict = {
    "name": "Centos7_vm",
    "annotation": "",
    "imageType": "DISK_IMAGE",
    "imageImportSpec": {
    "containerUuid": container_uuid,
    "url": centvm,
    }
}

winsviso_dict = {
    "name": "win2019_ISO",
    "annotation": "",
    "imageType": "ISO_IMAGE",
    "imageImportSpec": {
    "containerUuid": container_uuid,
    "url": winsviso,
    }
}

#make session 
session = requests.Session()
session.auth = (user, new_password)
session.verify = False                 
session.headers.update({'Content-Type': 'application/json; charset=utf-8'})

response = session.post('https://172.29.161.60:9440/api/nutanix/v0.8/images/',data=json.dumps(virtio_dict, indent=2))
if response.ok:
    print("VirtIO Upload is ok")
else:
    print("VirtIO Upload is fault")

response = session.post('https://172.29.161.60:9440/api/nutanix/v0.8/images/',data=json.dumps(centiso_dict, indent=2))
if response.ok:
    print("centiso Upload is ok")
else:
    print("centiso Upload is fault")

response = session.post('https://172.29.161.60:9440/api/nutanix/v0.8/images/',data=json.dumps(centvm_dict, indent=2))
if response.ok:
    print("centos_vm Upload is ok")
else:
    print("centos_vm Upload is fault")

response = session.post('https://172.29.161.60:9440/api/nutanix/v0.8/images/',data=json.dumps(winsviso_dict, indent=2))
if response.ok:
    print("win2019iso Upload is ok")
else:
    print("win2019iso Upload is fault")


#print(containername)

#acliをjsonで出力
#print(exec_command(IP, username, Password,"source /etc/profile; acli -o json host.list"))

#jsonをDictionaryに変換
#output = exec_command(IP, username, Password,"source /etc/profile; acli -o json host.list")
#print(json.loads(output))

#jsonをDictionaryに変換し、必要なデータを抜く
#output = exec_command(IP, username, Password,"source /etc/profile; ncli cluster get-domain-fault-tolerance-status type=node --json=true")
#outputdict = json.loads(output)
#value = outputdict["data"]["componentFaultToleranceStatus"]["FREE_SPACE"]["numberOfFailuresTolerable"]
#print(value)

#コンテナの取得
#print(exec_command(IP, username, Password,"source /etc/profile; ncli container list --json=true"))

#VirtualMachineの取得
#print(exec_command(IP, username, Password,"source /etc/profile; acli -o json vm.list"))

#ネットワークの取得
#print(exec_command(IP, username, Password,"source /etc/profile; acli -o json net.list"))



