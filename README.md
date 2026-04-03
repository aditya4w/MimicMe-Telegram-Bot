# MimicMe Telegram Bot

A fun Telegram bot that mimics your messages in a mocking way, tells jokes, and converts text to sPoNgEbOb case.

## Features
- Mimics any message you send in a mocking way
- `/joke` — Get a random joke from the internet
- `/mock <text>` — Convert text to sPoNgEbOb case
- `/help` — Show available commands

## Setup

1. Clone the repo
```bash
git clone https://github.com/aditya4w/MimicMe-Telegram-Bot
cd MimicMe_TGBot
```

2. Install dependencies
```bash
pip install python-telegram-bot requests
```

3. Configure
```bash
cp config.example.py config.py
```

4. Add your credentials in `config.py`
```python
TOKEN = 'your-bot-token'
BOT_USERNAME = '@your-bot-username'
```

5. Run
```bash
python main.py
```

## Built With
- Python
- python-telegram-bot v22
- JokeAPI
