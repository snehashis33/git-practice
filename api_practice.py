import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")

print(response.status_code)
data = response.json()
print("User 1")
print(data[0]["address"]["city"])
print("User 2")
print(data[1]["address"]["city"])