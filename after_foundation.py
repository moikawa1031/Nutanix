import json
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

#パラメーター
user = "admin"
old_password = "nutanix/4u"
new_password = "xxxxxxx"
user_name="xxxxxx"
company_name="DI"
job_title="Systems Engineer"

body_dict_passwd = {
  "oldPassword":old_password,
  "newPassword":new_password
}

body_dict_eula = {
  "username":user_name,
  "companyName":company_name,
  "jobTitle":job_title
}

body_dict_pulse = {
  "emailContactList":None,
  "enable":"true",
  "verbosityType":None,
  "enableDefaultNutanixEmail":False,
  "defaultNutanixEmail":None,
  "nosVersion":None,
  "isPulsePromptNeeded":False,
  "remindLater":None
}

#make session 
session = requests.Session()
session.auth = (user, old_password)
session.verify = False                 
session.headers.update({'Content-Type': 'application/json; charset=utf-8'})

#prism password change
response = session.post('https://172.29.161.60:9440/api/nutanix/v1/utils/change_default_system_password',data=json.dumps(body_dict_passwd, indent=2))
if response.ok:
    print("change default password is ok")
else:
    print("change default password is fault")

#make session 
session = requests.Session()
session.auth = (user, new_password)
session.verify = False                 
session.headers.update({'Content-Type': 'application/json; charset=utf-8'})

#prism eula enable
response = session.post('https://172.29.161.60:9440/api/nutanix/v1/eulas/accept',data=json.dumps(body_dict_eula, indent=2))
if response.ok:
    print("eula check is ok")
else:
    print("eula check is fault")

#prism pulse enable
response = session.put('https://172.29.161.60:9440/PrismGateway/services/rest/v1/pulse',data=json.dumps(body_dict_pulse, indent=2))
if response.ok:
    print("pulse check is ok")
else:
    print("pulse check is fault")
