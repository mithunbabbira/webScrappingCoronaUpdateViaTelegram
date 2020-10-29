import telebot
import time
import requests
import bs4


res = requests.get('https://www.worldometers.info/coronavirus/country/india/')
print(res)
n=[]
soup = bs4.BeautifulSoup(res.text, 'lxml')

bot_token ='1228157522:AAECEHSq1ImwdM5-vvW5vyKqwJp3Ax60W4E'

bot = telebot.TeleBot(token=bot_token)


#ID = '801016893_1087390121788281336'





for i in soup.select('.maincounter-number'):
  n.append(i.text)
print(n[2])



ID = ['801016893_1087390121788281336','1103371558_2811474889819250540']
bot.send_message(chat_id=ID[0], text="\npositive="+n[0]+"\nDead="+n[1]+"\nRecovered="+n[2]+"\nby Mithun BD")

bot.send_message(chat_id=ID[1], text="\npositive="+n[0]+"\nDead="+n[1]+"\nRecovered="+n[2]+"\nby Mithun BD to shifana mallu (i will never ignore u")


# for i in range (9999999999999999,9999999999999991,-1):
# 	bot.send_message(chat_id=ID, text=i)

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
# 	bot.reply_to(message,"positive="+n[0]+"Dead="+n[1]+"Recovered="+n[2])


bot.polling()