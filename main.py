import os
from dotenv import load_dotenv

import functions_framework
import flask
import telebot
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

load_dotenv()

TOKEN = os.environ.get("TELEGRAM_API_TOKEN")
MISTRAL_KEY = os.environ.get("MISTRAL_AI_API_KEY")

bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
client = MistralClient(api_key=MISTRAL_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	print("Sending to mistral ......")
	mistral_response = client.chat(
		model="mistral-small-latest",
		messages=[ChatMessage(role="user", content=str(message.text))]
	)
	bot.reply_to(message, mistral_response.choices[0].message.content)

bot.infinity_polling()