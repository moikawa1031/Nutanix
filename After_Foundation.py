import json
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)
import os

file = os.path.abspath("iso.json")
print(file)
#json_open = open('C:\\Users\\moikawa\\Documents\\PEG\\Python\\ライブラリ\\iso.json','r',encoding="utf_8")
#json_load = json.load(json_open)
#print(json_load)  