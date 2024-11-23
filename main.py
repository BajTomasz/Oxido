import json
import logging
import sys
from typing import Optional, Union

import requests
from openai import OpenAI


def generate_html(api_key: str, system_prompt: str, article: str) -> Optional[str]:
    try:
        client = OpenAI(api_key=api_key)
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": article}],
        )
        return completion.choices[0].message.content
    except Exception as e:
        logging.error(f"Wystąpił nieoczekiwany błąd: {e}")
    sys.exit()


def open_json(filename: str) -> Optional[Union[dict, list]]:
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("Plik nie istnieje. Sprawdź ścieżkę do pliku.")
    except PermissionError:
        logging.error("Brak uprawnień do odczytu pliku.")
    except Exception as e:
        logging.error(f"Wystąpił nieoczekiwany błąd: {e}")
    sys.exit()


def fetch_text_from_url(url: str) -> Optional[str]:
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            response.encoding = "utf-8"
            return response.text
        else:
            logging.error(f"Nieprawidłowy status HTTP {response.status_code} dla URL: {url}")
    except requests.exceptions.Timeout:
        logging.error(f"Przekroczono limit czasu dla URL: {url}")
    except requests.exceptions.ConnectionError:
        logging.error(f"Błąd połączenia z URL: {url}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Wystąpił błąd podczas próby pobrania URL '{url}': {e}")
    sys.exit()


def save_html_to_file(file_path: str, content: str) -> bool:
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except PermissionError:
        logging.error(f"Brak uprawnień do zapisu pliku: {file_path}")
    except FileNotFoundError:
        logging.error(f"Nie znaleziono ścieżki do pliku: {file_path}")
    except Exception as e:
        logging.error(f"Wystąpił nieoczekiwany błąd podczas zapisu pliku '{file_path}': {e}")
    print(content)


def main():
    prompt_library = open_json("promptLibrary.json")
    config = open_json("config.json")
    article = fetch_text_from_url(config.get("url"))
    article_html = generate_html(config.get("api_key"), prompt_library.get("system-gen-article"), article)
    if article_html.startswith("```html") and article_html.endswith("```"):
        article_html = article_html[8:-4]

    save_html_to_file("artykul.html", article_html)


if __name__ == "__main__":
    main()
