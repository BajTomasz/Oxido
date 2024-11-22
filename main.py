from openai import OpenAI
import requests
import json

def main():
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    url = config.get("url")

    response = requests.get(url)

    if response.status_code == 200:
        response.encoding = 'utf-8'
        print(response.text)
    else:
        print(response.status_code)

if __name__ == "__main__":
    main()
