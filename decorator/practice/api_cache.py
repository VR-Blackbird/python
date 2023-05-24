import requests
from clock_decor import clock
from functools import cache


@cache
@clock
def hit_request(url):
    a = requests.get(url)
    return a.json()


response = hit_request("https://urlhaus-api.abuse.ch/v1/urls/recent/")
response2 = hit_request(
    "https://urlhaus-api.abuse.ch/v1/urls/recent/"
)  # Will not be executed

print(len(response))
print(len(response2))
