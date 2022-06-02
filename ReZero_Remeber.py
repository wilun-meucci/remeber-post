from datetime import datetime as dt
import schedule
import time
import telebot

adminReZero = {
    "Monday" : "@YukoNakitsu",
    "Tuesday" : "@Miliguer",
    "Wednesday" : "@Spartacus16ssl",
    "Thursday" : "@Silverio99",
    "Friday" : "@RonXD",
    "Saturday" : "@Demenziale482oro"
}

adminTQQ = {
    "Monday" : "@Your_Sirius",
    "Tuesday" : "@FilippoPazzoSgravato",
    "Wednesday" : "",
    "Thursday" : "@ohAenys",
    "Friday" : "@wlady06",
    "Saturday" : "@DRIFT_X97"
}

bot = telebot.TeleBot("5507623814:AAHoDyqHzoDE06_TtXd3Z7-10ejnqPuzO-s")

 
text = "Sono un messagio progrannato perciò non lamentatevi detto questo.... Domani tocca a {} per postare"

def tempo():
    return dt.now()

def sendNotifyTQQ():
    for a in adminTQQ:
        if(dt(t.year,t.month,t.day+1).strftime("%A")==(a)and (t.hour==19)):
            print("messagio mandato in TQQ")
            bot.send_message(-1001317450691, text.format(adminTQQ[a]))

def sendNotifyReZero():
    for a in adminReZero:
        if(dt(t.year,t.month,t.day+1).strftime("%A")==(a)and (t.hour==19)):
            print("messagio mandato in Re zero")
            bot.send_message(-1001492371018, text.format(adminReZero[a]))



schedule.every().day.at("19:30").do(sendNotifyTQQ)
schedule.every().day.at("19:30").do(sendNotifyReZero)
bot.send_message(-1001492371018, "test funge ? siamo on?")
    
while True:
    t = tempo()
    print(t)
    schedule.run_pending()
    time.sleep(60)

bot.polling(none_stop=True)
