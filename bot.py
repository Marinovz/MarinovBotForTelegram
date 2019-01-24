# coding=utf-8
import telebot


from futbin import Player
from autobuyer_scratch import Autobuyer

import string
import random

bot_token = '593960129:AAFyMZRvmp9broDvG2ZtNZFN97NV-aOzcyc'

bot = telebot.TeleBot(token = bot_token)

welcome_msg = "Benvenuti, qui che scrive è Marinov_BOT, il vostro assistente nelle sniperate.  Digita /help per vedere la lista comandi!"

help_msg = "Questa è la lista comandi: /strategia1 ; /strategia2 ;/donazione /strategia3 ;/find_ps ; /find_xbox ; /find_pc  ; /accounts " + "\n\n" "( LE UTLIME 4 VANNO FATTE IN MESSAGGIO PRIVATO AL BOT)"

str1 = "La prima strategia consiste nello sniping di giocatori con overall 82 -> 85 e con un prezzo che va dai 3 ai 10k. Le percecntuali di buy possono essere 80-85% per profitti di 600/1000 crediti a giocatore; oppure 88-91% per sniperate più frequenti ma con un profit di 100/300 a giocatore. Percentuale sell : 98%.  GIORNI : LUNEDI, MARTEDI, MERCOLEDI!"

str2 ="La seconda strategia consiste nello sniping dei giocatori della settimana (IF). In questo caso bisogna impostare il PriceUpdateIntervall a 5.  Le percentuali di buy sono 89% e di sell 97%.  GIORNI : GIOVEDI, VENERDI,SABATO!"

str3 = "La terza strategia consiste nello sniping di forme fisiche(WIP), stili intesa e cambiamenti ruolo.  STILI INTESA : HAUNTER, SHADOW.   CAMBIAMENTO POSZIONE : CAM -> ST ; CF -> CAM.!"



@bot.message_handler(commands=['start'])

def welcome(message):
    bot.reply_to(message,welcome_msg)

@bot.message_handler(commands=['help'])

def help(message):
    bot.reply_to(message,help_msg)

@bot.message_handler(commands=['strategia1'])
def strategia_1(message):
    bot.reply_to(message,str1)

@bot.message_handler(commands=['strategia2'])
def strategia_2(message):
    bot.reply_to(message,str2)

@bot.message_handler(commands=['strategia3'])
def strategia_3(message):
    bot.reply_to(message,str3)


@bot.message_handler(commands=['find_ps'])
def find_Player(message):
    bot.reply_to(message, 'INSERISCI IL NOME DEL GIOCATORE E LA SUA VERSIONE (ESEMPIO : Cristiano Ronaldo, CL) : ')
    @bot.message_handler(content_types=['text'])
    def handle_message(msg):
        txt = msg.text.split(',')
        if len(txt) != 2:
            bot.reply_to(msg, "ERROR : Giocatore o versione non specificata")
        else:    
            player = Player(txt[0], console = 'ps',version = txt[1].strip())
            if player.player == None:
                bot.reply_to(msg,'Giocatore non trovato')
            else:
                bot.send_photo(msg.chat.id,photo = player.player[0]['image'])
                bot.reply_to(msg,player.price)

@bot.message_handler(commands=['find_xbox'])
def find_Player2(message):
    bot.reply_to(message, 'INSERISCI IL NOME DEL GIOCATORE E LA SUA VERSIONE (ESEMPIO : Cristiano Ronaldo, CL) : ')
    @bot.message_handler(content_types=['text'])
    def handle_message(msg):
        txt = msg.text.split(',')
        if len(txt) != 2:
            bot.reply_to(msg, "ERROR : Giocatore o versione non specificata")
        else:    
            player = Player(txt[0], console = 'xbox',version = txt[1].strip())
            if player.player == None:
                bot.reply_to(msg,'Giocatore non trovato')
            else:
                bot.send_photo(msg.chat.id,photo = player.player[0]['image'])
                bot.reply_to(msg,player.price)    
                
@bot.message_handler(commands=['find_pc'])
def find_Player3(message):
    bot.reply_to(message, 'INSERISCI IL NOME DEL GIOCATORE E LA SUA VERSIONE (ESEMPIO : Cristiano Ronaldo, CL) : ')
    @bot.message_handler(content_types=['text'])
    def handle_message(msg):
        txt = msg.text.split(',')
        if len(txt) != 2:
            bot.reply_to(msg, "ERROR : Giocatore o versione non specificata")
        else:    
            player = Player(txt[0], console = 'pc',version = txt[1].strip())
            if player.player == None:
                bot.reply_to(msg,'Giocatore non trovato')
            else:
                bot.send_photo(msg.chat.id,photo = player.player[0]['image'])
                bot.reply_to(msg,player.price)
                
@bot.message_handler(commands=['donazione'])
def donation(message):
    bot.reply_to(message, 'Se vuoi contribuire dona qui -> https://paypal.me/Netsphere?locale.x=it_IT')
    
@bot.message_handler(commands=['accounts'])
def checkAccount(message):
    bot.reply_to(message,"INSERISCI INDIRIZZO BOT, EMAIL, PASSWORD per accedere al bot")
    random_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    @bot.message_handler(content_types=["text"])
    def handle_message(msg):
        txt = msg.text.split(',')
        autobuyer = Autobuyer(txt[0],txt[1],txt[2],random_name)
        bot.send_message(msg.chat.id,"PROFITTI GIORNALIERO : " + autobuyer.info[0] + "\n\n" + "PROFITTi TOTALE : " + "\n\n" + autobuyer.info[1] + "\n\n\n" + "CREDITI: " + autobuyer.info[2] + '\n\n' + 'STATUS : ' + autobuyer.info[3] + '\n\n\n' + 'ULTIME TRANSAZIONI : ')
        photo = open('C:\\Users\\virusoffice\\Documents\\Python\\Lavori personali\\Bot telegram\\' + random_name + '.png', 'rb')
        bot.send_photo(msg.chat.id, photo)
    
bot.polling()
