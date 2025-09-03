import requests
import time
from datetime import datetime

# এখানে তোমার Bot Token বসাও
TOKEN = "8449777411:AAFVpCRDRGa_vYhgomPAxUM-7Oq0sUyb4Ig"
URL = f"https://api.telegram.org/bot{TOKEN}/"

# Get Updates
def get_updates(offset=None):
    params = {"timeout": 100, "offset": offset}
    response = requests.get(URL + "getUpdates", params=params)
    return response.json()

# Send Message
def send_message(chat_id, text):
    params = {"chat_id": chat_id, "text": text}
    requests.post(URL + "sendMessage", params=params)

# Handle Commands
def handle_message(chat_id, text, first_name):
    if text == "/start":
        send_message(chat_id, f"👋 হ্যালো {first_name}! আমি তোমার Updated Bot.")
    elif text == "/help":
        send_message(chat_id, "ℹ️ Available commands:\n/start - বট চালু করো\n/help - হেল্প দেখো\n/time - এখন সময়\n/id - তোমার Chat ID")
    elif text == "/time":
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        send_message(chat_id, f"⏰ Current time: {now}")
    elif text == "/id":
        send_message(chat_id, f"🆔 Your chat ID: {chat_id}")
    else:
        send_message(chat_id, f"তুমি লিখেছো: {text}")

# Main Bot Loop
def main():
    offset = None
    print("🤖 Bot is running...")
    while True:
        updates = get_updates(offset)
        if "result" in updates:
            for update in updates["result"]:
                offset = update["update_id"] + 1
                if "message" in update:
                    chat_id = update["message"]["chat"]["id"]
                    first_name = update["message"]["chat"].get("first_name", "User")
                    text = update["message"].get("text", "")
                    handle_message(chat_id, text, first_name)

if __name__ == "__main__":
    main()
