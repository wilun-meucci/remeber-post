from datetime import datetime as dt



def time():
    return dt.now()



admin = {
    "Monday" : " @YukoNakitsu",
    "Tuesday" : "@Miliguer",
    "Wednesday" : "@Spartacus16ssl",
    "Thursday" : "@Silverio99",
    "Friday" : "@RonXD",
    "Saturday" : "@Demenziale482oro"
}




import telebot
from telebot import util, types
from telebot import types
from telebot.apihelper import send_animation, send_message, upload_sticker_file



bot = telebot.TeleBot("5507623814:AAHoDyqHzoDE06_TtXd3Z7-10ejnqPuzO-s")
t = time()
 
text = "Sono un messagio progrannato perciò non lamentatevi detto questo.... Domani tocca a {} per postare"

        
for a in admin:
    """if((t.strftime("%A") == (a))and(t.hour==8)):
    print("ciao")"""
    if(dt(t.year,t.month,t.day+1).strftime("%A")==(a)and (t.hour==19)):
        print("ciao")
        bot.send_message(-1001492371018, text.format(admin[a]))
            
        print((t.day+1))
        

@bot.message_handler()
def start_command(message):
    

    #Il codice deve funzionare solo in chat privata, il bot non prosegue.
    if message.chat.type != "private":
        return
    
    chat_id = message.chat.id

    bot.send_message(chat_id, "boh")


bot.polling(none_stop=True)