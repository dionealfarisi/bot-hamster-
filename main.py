import telebot
import requests
import time
import os

# Ambil token dari environment variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHANNEL_ID = "@hamsterpricesss"
CRYPTO_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=hamster-kombat&vs_currencies=usd'

# Inisialisasi bot
bot = telebot.TeleBot(TOKEN)

# Fungsi untuk mendapatkan harga crypto
def get_crypto_price():
    response = requests.get(CRYPTO_API_URL)
    data = response.json()
    return data['hamster-kombat']['usd']

last_price = None

while True:
    price = get_crypto_price()
    if price != last_price:
        message = f"{price}$"
        bot.send_message(CHANNEL_ID, message)
        last_price = price
    time.sleep(1000)
