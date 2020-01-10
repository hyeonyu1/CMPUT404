import requests

print(requests.__version__)

response = requests.get("http://google.com/") 
print(response.content)

response = requests.get("https://raw.githubusercontent.com/hyeonyu1/CMPUT404/master/Lab1/question2.py") 
print(response.content)