import psycopg2

from db_api import inserting, creating, delAndSearch, showing


def connect():
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="qwer1234",
        host="localhost",
        port="5432")

    cursor = conn.cursor()
    creating.delete_db(cursor)

    creating.create_db(cursor)


def testAdd(cursor):
    field_dict = {'Ссылка на видео': 'https://www.youtube.com/watch?v=4YmBEoILpyE',
                  'Название видео': 'УрФУ проморолик',
                  'Псведоним создателя': 'Project 5-100',
                  'Жанр видео': 'проморолик',
                  'Страна создания': 'Россия',
                  'Имя создателя': '',
                  'Фамилия создателя': '',
                  'День рождения создателя': '',
                  'Пол создателя': ''}
    inserting.call_insert(field_dict, cursor)
    field_dict = {'Ссылка на видео': 'https://www.youtube.com/watch?v=WofZC2DvMSM',
                  'Название видео': 'День первый в Уральском федеральном — 2019',
                  'Псведоним создателя': 'Университетское ТВ УрФУ',
                  'Жанр видео': 'обзор',
                  'Страна создания': 'Россия',
                  'Имя создателя': '',
                  'Фамилия создателя': '',
                  'День рождения создателя': '',
                  'Пол создателя': ''}
    inserting.call_insert(field_dict, cursor)
    field_dict = {'Ссылка на видео': 'ссылка',
                  'Название видео': 'название',
                  'Псведоним создателя': 'Университетское ТВ УрФУ',
                  'Жанр видео': 'обзор',
                  'Страна создания': 'Россия',
                  'Имя создателя': '',
                  'Фамилия создателя': '',
                  'День рождения создателя': '',
                  'Пол создателя': ''}
    inserting.call_insert(field_dict, cursor)


field_dict = {'Ссылка на видео': '',
              'Название видео': '',
              'Псведоним создателя': '',
              'Жанр видео': 'обзор',
              'Страна создания': '',
              'Имя создателя': '',
              'Фамилия создателя': '',
              'День рождения создателя': '',
              'Пол создателя': ''}
# testAdd(cursor)
# a = showing.show_video(cursor)
# print(a)
# del_and_search.call_find(field_dict, cursor, 1)
# a = showing.show_video(cursor)
