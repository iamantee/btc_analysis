from dune_client.client import DuneClient
import json
import telebot
from datetime import datetime

# load api key
AAVE_API_KEY = ''
AAVE_QUERY_ID = 0

with open('secret.json', 'r') as f:
    secret_data = json.load(f)
    AAVE_API_KEY = secret_data['aave_api_key']
    AAVE_QUERY_ID = secret_data['aave_query_id']

dune = DuneClient(AAVE_API_KEY)
query_result = dune.get_latest_result(AAVE_QUERY_ID)


tg_message = ''

try:
    total_borrow_volume_millions = 0
    today = datetime.now().strftime('%Y-%m-%d')
    tg_message += f"Date: {today}" + chr(10)
    tg_message += ("-" * 40 + chr(10))
    for r in query_result.result.rows:
        if r['day'] == today + ' 00:00:00.000 UTC':
            token = r['token']
            borrow_volume_millions = (r['Borrow_volume']  / 1_000_000) if r['Borrow_volume'] is not None else 0
            if borrow_volume_millions > 0:
                tg_message += f"{token}: {borrow_volume_millions:.2f}M" + chr(10)
                total_borrow_volume_millions += borrow_volume_millions
    tg_message += ("-" * 40 + chr(10))
    tg_message += f"Total: {total_borrow_volume_millions:.2f}M" + chr(10)
    tg_message += ">= 400M may be regarded as FOMO"
except IOError as e:
    print(f"Error writing to file: {e}")
except TypeError as e:
    print(f"Error serializing query result to JSON: {e}")



# Load Telegram bot token and chat ID from secret.json
TELEGRAM_BOT_TOKEN = secret_data['telegram_bot_token']
CHAT_ID = secret_data['chat_id']

# Initialize the Telegram bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

try:
    # Send the message to the specified chat
    bot.send_message(CHAT_ID, tg_message)
    print("Message sent successfully to Telegram.")
except Exception as e:
    print(f"Error sending message to Telegram: {e}")
