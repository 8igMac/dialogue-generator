# Dialogue Generator
A Dialogue generator powered by ChatGPT.

## Usage
- Clone the repo.
- Install dependency.
```sh
$ poetry install
```
- Add your [API key](https://beta.openai.com/account/api-keys) and [session token](https://github.com/acheong08/ChatGPT/wiki/Setup) in `config.json` (You can just copy `config.json.example`, **Make sure you have Chrome install and updated to version 108**).
- Chat with ChatGPT.
```sh
$ poetry run revChatGPT
```
- Generate dialog data. (Generated dialog will be in `data/` directory).
```sh
$ poetry run python dialogue-generator/gen_dialog.py
```