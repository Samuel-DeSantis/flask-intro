import requests

BASE = "http://127.0.0.1:5000/"

data = [{"name": "Do a kickflip", "views": 14, "likes": 10},
        {"name": "How to do drugs", "views": 28, "likes": 0},
        {"name": "Eating hotdogs", "views": 123, "likes": 78},]

# for i in range(len(data)):
#   response = requests.put(BASE + "video/" + str(i), data[i])
#   print(response)

response = requests.get(BASE + "video/0")
print(response)

input()

response = requests.get(BASE + "video/0")
print(response.json())

# response = requests.delete(BASE + "video/1")
# print(response)

response = requests.get(BASE + "video/1")
print(response.json())