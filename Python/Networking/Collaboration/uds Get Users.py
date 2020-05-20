import requests
import xml.dom.minidom
import xmltodict
import urllib3
import json
from pprint import pprint
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#### For use with the DevNet Sandbox CUCM 11.5 #####
url = 'https://10.10.20.1/cucm-uds'
endpoint = 'users'

users_url = f'{url}/{endpoint}'

headers = {
    'Accept': 'application/xml',
    'Content-Type': 'application/xml'
}

username = 'administrator'
pw = 'ciscopsdt'

r = requests.get(users_url, auth=(username, pw), verify=False)

# Pretty up the XML response
tree = xml.dom.minidom.parseString(r.text)
pretty = tree.toprettyxml()

# Convert to Python Dict
xmldata = xmltodict.parse(pretty)
print(json.dumps(xmldata, indent=2, sort_keys=True))
print('*' * 50)

# users = xmldata['users']['user']
# for user in users:
#     print(f"{user['lastName']} {user['firstName']}")
#     print(f"ID: {user['id']}")
#     print(" ")


# Get specific userrrrrrrr

user01 = xmldata['users']['user'][0]

print("Here are User1 Details: ")
print(json.dumps(user01, indent=2, sort_keys=True))
