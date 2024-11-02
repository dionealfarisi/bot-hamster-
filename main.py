import telebot
import requests
import time

# Masukkan token bot dan ID channel
TOKEN = "7697093794:AAEn6athk-FuRUknkH7vlHt4wmg97Z-2owM"
CHANNEL_ID = "@hamsterpricesss"  # Contoh: @btcpricesss
CRYPTO_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids=hamster-kombat&vs_currencies=usd'

# Inisialisasi bot
bot = telebot.TeleBot(TOKEN)

# Fungsi untuk mendapatkan harga crypto
def get_crypto_price():
    response = requests.get(CRYPTO_API_URL)
    data = response.json()
    return data['hamster-kombat']['usd']

# Menyimpan harga terakhir untuk pengecekan perubahan
last_price = None

# Loop untuk mengirim harga setiap satu jam jika ada perubahan
while True:
    price = get_crypto_price()
    
    # Mengirim pesan hanya jika harga berubah
    if price != last_price:
        message = f"{price}$"
        bot.send_message(CHANNEL_ID, message)
        last_price = price  # Update harga terakhir
    
    time.sleep(1000)  # Menunggu 1 jam sebelum pengecekan ulang
