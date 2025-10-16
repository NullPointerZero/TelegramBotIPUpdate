import os
import sys
import requests
import json

from config_loader import load_config
from IP_comparator import get_public_ip

def send(msg: str, token: str, chat_id: str) -> None:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    r = requests.post(url, data={"chat_id": chat_id, "text": msg, "disable_web_page_preview": True}, timeout=10)
    r.raise_for_status()
    ok = r.json().get("ok", False)
    if not ok:
        raise RuntimeError(f"Telegram-API-Fehler: {r.text}")

def did_IP_change(filename = "config.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    old_IP_address = data.get("old_IP_Address")
    new_IP_address = get_public_ip()

    if new_IP_address != old_IP_address:
        token, chat_id = load_config()
        send(new_IP_address, token, chat_id)


if __name__ == "__main__":

    did_IP_change()
    token, chat_id = load_config()
    send("Long live the King", token, chat_id)
    print("Gesendet.")
