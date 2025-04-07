import requests
from dotenv import load_dotenv
import os

load_dotenv()

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage" # Url para enviar mensagens 
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, data=payload)
    return response
    
token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")
message = "Estou no telegram em python"

if token and chat_id:
    send_telegram_message(token, chat_id, message)
else:
    print("Token ou chat_id não encontrados nas variáveis de ambiente")
