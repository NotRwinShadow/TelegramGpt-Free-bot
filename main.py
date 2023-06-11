###########################################################################################
#                                                                                         #
#      _   _       _  ______          _       _____ _               _                     #
#     | \ | |     | | | ___ \        (_)     /  ___| |             | |                    #
#     |  \| | ___ | |_| |_/ /_      ___ _ __ \ `--.| |__   __ _  __| | _____      __      #
#     | . ` |/ _ \| __|    /\ \ /\ / / | '_ \ `--. \ '_ \ / _` |/ _` |/ _ \ \ /\ / /      #
#     | |\  | (_) | |_| |\ \ \ V  V /| | | | /\__/ / | | | (_| | (_| | (_) \ V  V /       #
#     \_| \_/\___/ \__\_| \_| \_/\_/ |_|_| |_\____/|_| |_|\__,_|\__,_|\___/ \_/\_/        #
#                                                                                         #
#      contact me --> rwinshadow@gmail.com                                                #            
#                                                                                         #
###########################################################################################

import telebot
import requests

# Initialize the Telegram bot
bot = telebot.TeleBot("TELEGRAM-BOT-TOKEN")

# Handle /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, 'command list : ' + '\n \n' + '/help : for seeing this message' + '\n \n' + '/chat + <command> : to send message to BOT' + '\n \n' + 'exp : ' + '\n' + '/chat hi, what is your name?' + '\n \n' + 'designer: https://github.com/NotRwinShadow')

# Handle /start 
@bot.message_handler(commands=['start'])
def handle_start(message):
  bot.send_message(
    message.chat.id, "Hi, Welcome to robot" + ' ' +
    str(message.chat.first_name) + ' ' + '\u2764' + '\n \n' +
    ' Send /help to How to use ' + '\n \n ' + 'https://github.com/NotRwinShadow' )


@bot.message_handler(commands=['chat'])
def handle_chat(message):

  command = '/chat'
  text = message.text.replace(command, '', 1).strip()

  if text:
    sent_message = bot.reply_to(message, ' Procssenig \u23F3')
  
    url = 'https://amirroboti.eliyahost.ir/ApiWeb/ChatGPT1.php?text=' + text
    response = requests.get(url)
    ResponseText = response.text
  
    # Send the generated text as a response to the user
    bot.edit_message_text(ResponseText, message.chat.id, sent_message.message_id)

  else:
    bot.send_message(message.chat.id, "Cant send empty message use /help for help")

# Handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, "Message is not true use /help for help")


# Start the bot
bot.polling()
