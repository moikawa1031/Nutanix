import requests, json, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

IP = '172.29.161.60'
USER = 'admin'
PASSWORD = 'xxxxxxxx!'
session = requests.Session()
session.auth = (USER, PASSWORD)
session.verify = False
session.headers.update({'Content-Type': 'application/json; charset=utf-8'})

url = f'https://{IP}:9440/PrismGateway/services/rest/v1/cluster'
response = session.get(url)
if response.ok:
    j = response.json()
    print(json.dumps(j, indent=2))
else:
    print('error happens')
    print(f'sutatus code : {response.status_code}')
    print(response.text)
