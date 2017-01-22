# -*- coding: utf-8 -*-

import sqlite3
raspisanieList1=[['fizra','matan','----'],['tehnologia','----','infa']]
raspisanieList2=[['fizra','mat222an','----'],['tehnologia','--вывы--','infa']]

token = '312026656:AAFSEq1rLFGQmiP0w9bHOwzBnqcrDhtVFvs'

helloflag = 0

database_name = 'raspisanie.db'

class SQLighter:

    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def select_all(self):
        """ Получаем все строки """
        with self.connection:
            return self.cursor.execute('SELECT * FROM raspisanie').fetchall()

    def select_single(self, rownum):
        """ Получаем одну строку с номером rownum """
        with self.connection:
            return self.cursor.execute('SELECT * FROM raspisanie WHERE id = ?', (rownum,)).fetchall()[0]

    def count_rows(self):
        """ Считаем количество строк """
        with self.connection:
            result = self.cursor.execute('SELECT * FROM raspisanie').fetchall()
            return len(result)

    def close(self):
        """ Закрываем текущее соединение с БД """
        self.connection.close()

