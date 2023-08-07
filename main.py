import time
from telebot import TeleBot, types
import json
from settings import *

from parser_rule34 import full_post

bot = TeleBot(token=token)

# with open('full_post.json') as f:
#     full_post = json.load(f)

image = []

alt = list(full_post.values())

for key in full_post:
    image.append(key)

for value in alt:
    image.append(value)

def add_commas(string):
  words = string.split()
  new_string = ""
  for word in words:
    new_string += "#" + word + ","
  return new_string[:-1]

def filter_values(image):
    fin_image = []
    for value in image:
        if value.find(".gif") == -1:
            fin_image.append(value)
    return fin_image


fin_image = filter_values(image)

a = 0

while a < len(image):
    print("Опубликование фото №: ", a)
    bot.send_photo(channel, fin_image[a])
    time.sleep(5)
    bot.send_message(channel, add_commas(alt[a]))
    time.sleep(5)
    a += 1
    if a % 18 == 0:
        print("Timeout 30 sec.")
        time.sleep(30)
else:
    print("ХУЙНЯ ВАШ TELEGRAM API")
