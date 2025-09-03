import requests
import time

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
                    text = update["message"].get("text", "")
                    
                    # Simple Command Handling
                    if text == "/start":
                        send_message(chat_id, "👋 হ্যালো! আমি তোমার Simple Bot (API Version).")
                    elif text == "/help":
                        send_message(chat_id, "ℹ️ Available commands:\n/start - বট চালু করো\n/help - হেল্প দেখো")
                    else:
                        send_message(chat_id, f"তুমি লিখেছো: {text}")

if __name__ == "__main__":
    main()