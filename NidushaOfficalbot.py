"""
MIT License

Copyright (c) 2021 Nidusha Amarasinghe

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import telebot, requests, json
from telebot import types
from os import getenv

bot = telebot.TeleBot(getenv("BOT_TOKEN"))

# /help command menu
help = f"""
Contact Help!\n@NidushaChat_Bot
"""

# Markup
mark1 = telebot.types.InlineKeyboardMarkup()
mark1.add(telebot.types.InlineKeyboardButton(text='🔁Updates🔁', url='https://t.me/slaptap'),
          telebot.types.InlineKeyboardButton(text='🧑‍💻Support🧑‍💻', url='https://t.me/slaptaps')),
mark1.add(telebot.types.InlineKeyboardButton(text='➕Add Me To A Group➕', url="http://t.me/NidushaOfficial_Bot?startgroup=new")),
mark1.add(telebot.types.InlineKeyboardButton(text='🔰Github🔰', url='https://github.com/NidushaAmarasinghe')),

mark2 = telebot.types.InlineKeyboardMarkup()
mark2.add(telebot.types.InlineKeyboardButton(text='➕Add Me To A Group➕', url="http://t.me/NidushaOfficial_Bot?startgroup=new"),
          telebot.types.InlineKeyboardButton(text='🔰Github🔰', url='https://github.com/NidushaAmarasinghe')),
# Commands
@bot.message_handler(commands=['start'])
def send_start(message):
   bot.send_message(message.chat.id, text="💕Hi There! 😁Welcome To Nidusha Official Bot😘\nJoin @SlapTap",parse_mode='Markdown', reply_markup=mark1)

@bot.message_handler(commands=["help"])
def send_help(message):
    bot.send_message(message.chat.id, text="Contact Help!\n@NidushaChat_Bot") 

@bot.message_handler(commands=["about"])
def send_about(message):
    bot.send_message(message.chat.id, text="This Is Nidusha Amarasinghe's Official Bot!\nDeverloper-@NidushaAmarasinghe"

@bot.message_handler(commands=["alive"])
def send_help(message):
    bot.send_message(message.chat.id, text="Hey There! Bot Online now. 💃🏻\n♥️Developer: ɳιԃυαԋα αɱαɾαʂιɳɠԋҽ\nSupport: @SlapTaps\nThank You For Using Niduha Official Bot💞") 

@bot.message_handler(commands=["stats"])
def send_help(message):
    bot.send_message(message.chat.id, text="💻System Stats💻\n⏳Uptime⏳:-  10 h: 8 m: 58 s.\n🔋Ram Usage🔋 :- 8%\n💾Disk Usage💾 :- 0.441") 

bot.polling()
