
import json

# Load the secret token + id from the json file, so that it can be published on githhub
def load_config(filename="TelegramBotConfig.json"):

    with open(filename, "r", encoding="utf-8") as f:

        data = json.load(f)

    token = data.get("BotToken")
    chat_id = data.get("ChatID")

    return token, str(chat_id)

def main():
    token, chat_id = load_config()
    print(token, chat_id)

if __name__ == "__main__":
    main()
