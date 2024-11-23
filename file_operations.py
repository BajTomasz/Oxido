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


def save_html_to_file(file_path: str, content: str):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except PermissionError:
        logging.error(f"Brak uprawnień do zapisu pliku: {file_path}")
        print(content)
    except FileNotFoundError:
        logging.error(f"Nie znaleziono ścieżki do pliku: {file_path}")
        print(content)
    except Exception as e:
        logging.error(f"Wystąpił nieoczekiwany błąd podczas zapisu pliku '{file_path}': {e}")
        print(content)


def insert_article_into_site(article_html):
    try:
        with open("szablon.html", "r") as f:
            template = f.read()
    except FileNotFoundError:
        logging.error("Plik nie istnieje. Sprawdź ścieżkę do pliku.")
        sys.exit()
    except PermissionError:
        logging.error("Brak uprawnień do odczytu pliku.")
        sys.exit()
    except Exception as e:
        logging.error(f"Wystąpił nieoczekiwany błąd: {e}")
        sys.exit()

    final_html = template.replace("{article}", article_html)
    save_html_to_file("podglad.html", final_html)
