import os

import telebot
import firebase_admin
from firebase_admin import db
from get_results import get_result


BOT_TOKEN = "6147728737:AAEyqSKjjhK3-CmVJzRe6KNBNw3I_Rg_afY"

bot = telebot.TeleBot(BOT_TOKEN)

cred_obj = firebase_admin.credentials.Certificate('private_key.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://plethora-of-energy-274d0-default-rtdb.europe-west1.firebasedatabase.app/'
	})
ref = db.reference("/")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Send me a number - amount of steps you walked in one day divided by 5000." + 
    " You should send the numbers for two best days of the week."
    )

@bot.message_handler(commands=['score'])
def send_welcome(message):
    res = get_result (ref)
    if (res == ""):
        res = "No scores yet"
    bot.reply_to(message, res)

@bot.message_handler(func=lambda message: message.text.isnumeric())
def update_score(message):
    username = message.from_user.username
    x = ref.get ()
    if x is None:
        x = dict ()
    if username in x:
        x[username] += int (message.text)
    else:
        x[username] = int (message.text)
    ref.set (x)
    res = get_result (ref)
    bot.reply_to(message, "Success! Updated scoreboard:\n" + res)

bot.infinity_polling()