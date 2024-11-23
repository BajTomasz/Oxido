
from file_operations import fetch_text_from_url, generate_html, insert_article_into_site, open_json, save_html_to_file


def main():
    prompt_library = open_json("promptLibrary.json")
    config = open_json("config.json")
    article = fetch_text_from_url(config.get("url"))
    article_html = generate_html(config.get("api_key"), prompt_library.get("system-gen-article"), article)
    if article_html.startswith("```html") and article_html.endswith("```"):
        article_html = article_html[8:-4]

    save_html_to_file("artykul.html", article_html)
    insert_article_into_site(article_html)


if __name__ == "__main__":
    main()
