import requests
from bs4 import BeautifulSoup
import os

TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": msg}
    requests.post(url, data=data)

url = "https://www.mubasher.info/countries/eg/news"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

for a in soup.find_all("a"):
    title = a.text.strip()

    if len(title) > 40:
        send_telegram("📰 EGX News\n\n" + title)
        break
