import requests
import os
from datetime import datetime, timedelta
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# API URLs und Bot Token
API_URL_CURRENT = "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/593647aa-9fea-43ec-a7d6-6476a76ae868/W/currentmeasurement.json"
API_URL_HISTORIC = "https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/593647aa-9fea-43ec-a7d6-6476a76ae868/W/measurements.json?start=P5D"
#TOKEN = ''
TOKEN = os.getenv('TELEGRAM_TOKEN')

# Funktion für den aktuellen Wasserstand
def get_current_water_level():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} - received request for current water level")
    response = requests.get(API_URL_CURRENT)
    if response.status_code == 200:
        data = response.json()
        return f"Aktueller Wasserstand: {data['value']} cm"
    return "Fehler beim Abrufen des aktuellen Wasserstands."

# Funktion für den maximalen Wasserstand der letzten 5 Tage
def get_max_water_level_last_5_days():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} - received request for weekly high water level")
    end_date = datetime.now()
    start_date = end_date - timedelta(days=5)
    params = {
        "start": start_date.strftime('%Y-%m-%dT%H:%M:%S'),
        "end": end_date.strftime('%Y-%m-%dT%H:%M:%S')
    }

    response = requests.get(API_URL_HISTORIC, params=params)
    if response.status_code == 200:
        data = response.json()
        max_level = max(data, key=lambda x: x['value'])
        max_value = max_level['value']
        max_date = max_level['timestamp']
        return f"Höchster Wasserstand der letzten 5 Tage: {max_value} cm am {max_date}"
    return "Fehler beim Abrufen der historischen Wasserstandsdaten."

# Asynchrone Handler-Funktionen
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hallo! Verwende /current für den aktuellen Wasserstand oder /weekly für den höchsten Wasserstand der letzten 5 Tage.")

async def current(update: Update, context: ContextTypes.DEFAULT_TYPE):
    water_level = get_current_water_level()
    await update.message.reply_text(water_level)

async def weekly(update: Update, context: ContextTypes.DEFAULT_TYPE):
    max_water_level = get_max_water_level_last_5_days()
    await update.message.reply_text(max_water_level)

# Bot-Einrichtung
def main():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} - Starting Aquaman Bot")
    app = Application.builder().token(TOKEN).build()

    # Befehle registrieren
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("current", current))
    app.add_handler(CommandHandler("weekly", weekly))

    # Bot starten
    app.run_polling()

if __name__ == "__main__":
    main()