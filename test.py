import requests
from pprint import pprint as pp

BASE = "http://127.0.0.1:5000/linda"

response = requests.get(BASE)
pp(response.json())