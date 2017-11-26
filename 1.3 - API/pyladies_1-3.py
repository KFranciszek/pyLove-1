
"""
# zadanie 3.1
import requests
resp = requests.get('http://py.net/status')
print(resp.json())
resp = requests.post(
    'http://py.net/status/set',
    json={
        "status": "Nowy status"
    }
)
print(resp.json())
resp = requests.get('http://py.net/status')
print(resp.json())
"""


"""
# 3.2
import requests
url = "http://py.net/register"
login = {"name": "Damian", "password": "xxx"}

zzzz = requests.post(url, json=login)
print(zzzz.json())
"""
"""
3.3
import requests
url = "http://py.net/auth"
login = {"name": "Damian", "password": "xxx"}
zzzz = requests.post(url, json=login)
print(zzzz.json())
"""
"""
# 3.4
import requests
url = "http://py.net/auth"
login = {"name": "Damian", "password": "xxx"}
zzzz = requests.post(url, json=login)
key = zzzz.json()['api_key']
print(key)

userStatURL = "http://py.net/user_status/set"
statusJson = {"api_key": key, "status": "Usmiech"}
resp = requests.post(userStatURL, json= statusJson)
print(resp.json())

userStatusURL = "http://py.net/user_status"
resp = requests.get(userStatusURL)
print(resp.json())
"""
"""
# 3.5
import requests
url = "http://py.net/cat"
resp = requests.get(url)

with open('kot.jpeg', 'wb') as file:
    file.write(resp.content)
    file.close()
"""
"""
# 3.6
import requests
url = "http://py.net/query_string?jeden=OK&dwa=Nie Ok"
resp = requests.get(url)

print(resp.json())
"""

"""
from pprint import pprint as pp
pp(resp.json())
"""