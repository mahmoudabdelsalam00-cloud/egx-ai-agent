import requests
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

data = {
    "chat_id": CHAT_ID,
    "text": "✅ اختبار نجاح البوت من GitHub"
}

requests.post(url, data=data)
