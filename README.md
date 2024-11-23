### README.md

# HTML Article Generator

This project uses OpenAI's GPT-4o-mini model to generate HTML articles from a provided text file fetched from a URL.
The program reads configuration and prompt details from JSON files, processes the text, and outputs the generated HTML article to a file.

## Requirements

### Python Version

* Python 3.12

### Dependencies

* `openai`: For interacting with OpenAI's GPT-4 model.
* `requests`: For fetching text content from the web.

Install the required dependencies using builtin script:

```bash
./install.sh
```

---

## Configuration

### Example `config.json`:

```json
{
    "url": "https://example.com/file.txt",
    "api_key": "ExampleApiKey"
}
```

* **`url`** : The URL pointing to the plain text file that the program will process.
* **`api_key`** : Your OpenAI API key to authenticate requests to the GPT model.

## How to Run

1. Clone this repository or download the code.
2. Ensure the required dependencies are installed via script install.sh.
3. Prepare the configuration files (`config.json`) in the same directory.
4. Run the script:
   ```bash
   ./run.sh
   ```
5. The generated HTML article will be saved in `artykul.html` in the same directory.

---

## Output

The resulting HTML file (`artykul.html`) will contain well-structured HTML code generated from the input text.

## Notes

* Make sure to provide a valid OpenAI API key in the `config.json` file.
* Ensure the URL in `config.json` points to a valid text resource.

## ToDo

* Add tests to benchmark prompts
