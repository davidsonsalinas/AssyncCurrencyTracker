import requests


def get_dollar_rate():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    return data

print(get_dollar_rate())