from openai import OpenAI
import requests
import json

def main():
    with open("promptLibrary.json", "r") as promptLibraryFile:
        promptLibrary = json.load(promptLibraryFile)

    with open("config.json", "r") as config_file:
        config = json.load(config_file)
    url = config.get("url")

    response = requests.get(url)
    response.encoding = 'utf-8'
    article = response.text

    client = OpenAI(api_key=config.get("api_key"))
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
            "role": "system",
            "content": promptLibrary.get("system-gen-article")
            },
            {
            "role": "user",
            "content": article
            }
        ]
    )

    with open("artykul.html", "w", encoding="utf-8") as f:
        articleHtml = completion.choices[0].message.content
        if articleHtml.startswith('```html') and articleHtml.endswith('```'):
            articleHtml = articleHtml[8:-4]
        f.write(articleHtml)
    

if __name__ == "__main__":
    main()
