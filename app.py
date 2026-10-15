import os
import threading
from flask import Flask
from bot import run_bot

app = Flask(__name__)

# Bot thread ko globally start karo (gunicorn ke saath bhi chalega)
_bot_started = False

def start_bot_once():
    global _bot_started
    if not _bot_started:
        _bot_started = True
        print("🤖 Starting Telegram bot thread...")
        t = threading.Thread(target=run_bot, daemon=True)
        t.start()

start_bot_once()

@app.route('/')
def index():
    return "Bot is running"

@app.route('/health')
def health():
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
