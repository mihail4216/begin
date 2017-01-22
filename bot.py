# -*- coding: utf-8 -*-
import sqlite3
from parser import parser_weather
import telebot
import config
import smiles
from telebot import types
import time
bot = telebot.TeleBot(config.token)
# c=u'asdf'+u'\U0001F601'
# sl=u'\\'
# aas='0001F601'
# print aas.encode('ascii')
##########################
@bot.message_handler(func=lambda message: True,commands=[u'главная'])
def mains(sms):
    menu = types.ReplyKeyboardMarkup()
    menu = menu.row(u'/расписание(1)',u'/расписание(2)',u'/погода(сегодня)')
    bot.send_message(sms.chat.id, u'Что надо?', reply_markup=menu)

#
# @bot.message_handler(func=lambda message: True, content_types=['text'])
# def answer_bot(message):
#     sms = message.text.lower()
#     if sms == "hi" or sms == u"привет" or sms == u"hello" or sms == u"главная" or sms == u"здарова":
#         list1 = types.ReplyKeyboardMarkup()
#         list1 = list1.row(u'/расписание',u'/главная')
#         bot.send_message(message.chat.id, u'Ну ,привет',reply_markup=list1)
#         print 2

###########################
@bot.message_handler(func=lambda message: True,commands=[u'расписание(1)'])
def raspisanie(sms):

    raspisanie = types.ReplyKeyboardMarkup()
    raspisanie = raspisanie.row(u'понедельник\U0001F601',u'вторник\U0001F601')
    raspisanie =raspisanie.row(u'/главная')
    bot.send_message(sms.chat.id, u'Выберете день:', reply_markup=raspisanie)


    @bot.message_handler(func=lambda message: True, regexp=u'понедельник\U0001F601')
    def der(message):
        print 2

        for i in config.raspisanieList1[0]:
            bot.send_message(message.chat.id, i)

    @bot.message_handler(func=lambda message: True, regexp=u'вторник\U0001F601')
    def der(message):


        for i in config.raspisanieList1[1]:
            bot.send_message(message.chat.id, i)


# def day(message):
#     sms = message.text.lower()
#     print 3
#     if sms == u'понедельник':
#         for i in config.raspisanieList1[0]:
#             bot.send_message(message.chat.id,i)😆
#     if sms == u'вторник':
#         for i in config.raspisanieList1[1]:
#             bot.send_message(message.chat.id, i)

##################################


@bot.message_handler(func=lambda message: True,commands=[u'расписание(2)'])
def raspisanie2(sms):

    raspisanie = types.ReplyKeyboardMarkup()
    raspisanie = raspisanie.row(u'понедельник\U0001F602',u'вторник\U0001F602',)
    raspisanie =raspisanie.row(u'/главная')
    bot.send_message(sms.chat.id, u'Выберете день:', reply_markup=raspisanie)
    sms1 = sms.text
    @bot.message_handler(func=lambda message: True,regexp=u'понедельник\U0001F602')
    def der(message):
        print 3

        for i in config.raspisanieList2[0]:
            bot.send_message(message.chat.id,i)

    @bot.message_handler(func=lambda message: True, regexp=u'вторник\U0001F602')
    def der(message):


        for i in config.raspisanieList2[1]:
            bot.send_message(message.chat.id, i)


# @bot.message_handler(func=lambda message: True,regexp=u'понедельник')
# def der(message):
#     print 33
#     if message.text == u'понедельник':
#         for i in config.raspisanieList2[0]:
#             bot.send_message(message.chat.id,i)
#     if message.text == u'вторник':
#         for i in config.raspisanieList2[1]:
#             bot.send_message(message.chat.id, i)

##################################
@bot.message_handler(func=lambda message: True,commands=[u'погода(сегодня)'])
def weather(sms):
    # for i in parser_weather():
    #     bot.send_message(sms.chat.id, i)
    bot.send_message(sms.chat.id,'Температура сейчас: '+parser_weather()[0])
    bot.send_message(sms.chat.id, 'Ощущается как: ' + parser_weather()[1])



















###########################################

if __name__=='__main__':
    bot.polling(none_stop=True)
##############################################