import os
import sys
import requests
from config_loader import load_config

def send(msg: str, token: str, chat_id: str) -> None:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    r = requests.post(url, data={"chat_id": chat_id, "text": msg, "disable_web_page_preview": True}, timeout=10)
    r.raise_for_status()
    ok = r.json().get("ok", False)
    if not ok:
        raise RuntimeError(f"Telegram-API-Fehler: {r.text}")

if __name__ == "__main__":


    token, chat_id = load_config()
    send("Long live the King", token, chat_id)
    print("Gesendet.")
