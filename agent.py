import requests
from bs4 import BeautifulSoup
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

# قراءة المصادر
with open("sources.txt") as f:
    sources = f.readlines()

for url in sources:
    url = url.strip()

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    for a in soup.find_all("a"):
        title = a.text.strip()

        if len(title) > 40:
            send_telegram("📰 خبر جديد\n\n" + title)
            break
