import os
import sys
import requests
import json

from config_loader import load_config
from IP_comparator import get_public_ip


# Potentially reusable for other Projects. Or to make the Bot more interactive.
# No interaction planned yet.
def send(msg: str, token: str, chat_id: str) -> None:
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    r = requests.post(url, data={"chat_id": chat_id, "text": msg, "disable_web_page_preview": True}, timeout=10)
    r.raise_for_status()
    ok = r.json().get("ok", False)
    if not ok:
        raise RuntimeError(f"Telegram-API-Fehler: {r.text}")


# This function is not reuasable anyway. it only checks wether the IP changed. It uses the config for
# it.
def did_IP_change(filename = "config.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    old_IP_address = data.get("old_IP_Address")
    new_IP_address = get_public_ip()

    if new_IP_address != old_IP_address:
        token, chat_id = load_config()
        send(new_IP_address, token, chat_id)
        write_IP_to_File(new_IP_address)
        print("[did IP change] new IP Address written")

# This function writes the IP to the config file. It uses a certain Identifier for it.
# potentially it could be reused in another project. Maybe i should make it more reusable.
def write_IP_to_File(new_ip, filename = "config.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    if "old_IP_Address" not in data:
        raise KeyError("identifier 'old_IP_Address' not Found")

    data["old_IP_Address"] = new_ip

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":

    did_IP_change()
    token, chat_id = load_config()
    #send("Long live the King", token, chat_id)
    print("Gesendet.")
