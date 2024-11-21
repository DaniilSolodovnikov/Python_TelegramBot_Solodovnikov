import os
import datetime
import sqlite3

from telegram.ext import CommandHandler, Updater


class Calendar:
    def __init__(self):
        self.events = {}
        self.conn = sqlite3.connect('calendar.db') #добавил строку (1 замечание)
        c = self.conn.cursor()
        c.execute("""
                    CREATE TABLE IF NOT EXISTS events (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        date date NOT NULL,
                        time time NOT NULL,
                        details TEXT
                    )
                """)
        self.conn.commit()

    def create_event(self, event_name, event_date, event_time, event_details):
        try:
            event_datetime = datetime.strptime(f"{event_date} {event_time}", "%Y-%m-%d %H:%M:%S")
            c = self.conn.cursor()
            c.execute("""
                        INSERT INTO events (name, date, time, details) VALUES (?, ?, ?, ?)
                    """, (event_name, event_date, event_time, event_details))
            self.conn.commit()
            return c.lastrowid #возвращаю .lastrowib (2 замечание)
        except ValueError:
            return 'Неверный формат даты или времени. Используйте формат YYYY-MM-DD HH:MM:SS'

    def read_event(self, event_id):
        c = self.conn.cursor()
        c.execute("""
                    SELECT * FROM events WHERE id = ?
                """, (event_id,))
        event = c.fetchone()
        if event:
            return {
                "id": event[0],
                "name": event[1],
                "date": event[2],
                "time": event[3],
                "details": event[4]
            }
        return None #Еще одно замечание исправленно

    def edit_event(self, event_id, new_details):
        c = self.conn.cursor()
        c.execute("""
                    UPDATE events SET details = ? WHERE id = ?
                """, (new_details, event_id))
        self.conn.commit()
        return 'Событие обновлено'

    def delete_events(self, event_id):
        c = self.conn.cursor()
        c.execute("""
                    DELETE FROM events WHERE id = ?
                """, (event_id,))
        self.conn.commit()
        return 'Событие удалено'

    def display_events(self):
        c = self.conn.cursor()
        c.execute("""
                    SELECT * FROM events
                """)
        events = c.fetchall()
        if events:
            for event in events:
                return (f"Event ID: {event[0]}, Имя: {event[1]}, Дата: {event[2]}, "
                      f"Время: {event[3]}, Детали: {event[4]}")
        else:
            return 'Нет событий'


calendar = Calendar()


# Создать обработчик для создания событий
def event_create_handler(update, context):
    try:
        # Взять данные о событии из сообщения пользователя
        event_name = update.message.text[14:]
        event_date = "2023-03-14"
        event_time = "14:00"
        event_details = "Описание события"

        # Создать событие с помощью метода create_event класса Calendar
        event_id = calendar.create_event(event_name, event_date, event_time, event_details)

        # Отправить пользователю подтверждение
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=f"Событие {event_name} создано и имеет номер {event_id}.")
    except:
        # Отправить пользователю сообщение об ошибке
        context.bot.send_message(chat_id=update.message.chat_id, text="При создании события произошла ошибка.")


def event_read_handler(update, context):
    try:
        event_id = int(update.message.text)
        event_data = calendar.read_event(event_id)
        if event_data:
            context.bot.send_message(chat_id=update.message.chat_id, text=f"Событие с ID {event_id}: {event_data}")
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text=f"Событие с ID {event_id} не найдено.")
    except ValueError:
        context.bot.send_message(chat_id=update.message.chat_id, text="Введите корректный ID события (число).")
    except Exception as e:
        context.bot.send_message(chat_id=update.message.chat_id, text=f"При прочтении события произошла ошибка: {e}")


def event_edit_handler(update, context, event_id, new_details):
    try:
        calendar.edit_event(event_id, new_details)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Событие с ID {event_id} отредактировано.")
    except Exception as e:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=f"При редактировании события произошла ошибка: {e}")


def event_delete_handler(update, context, event_id):
    try:
        calendar.delete_events(event_id)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Событие с ID {event_id} удалено.")
    except Exception as e:
        context.bot.send_message(chat_id=update.message.chat_id, text=f"При удалении события произошла ошибка: {e}")


def event_display_handler(update, context):
    try:
        calendar.display_events()
    except Exception as e:
        context.bot.send_message(chat_id=update.message.chat_id, text=f"При сортировке событий произошла ошибка: {e}")


Updater.dispatcher.add_handler(CommandHandler('create_event', event_create_handler))
Updater.dispatcher.add_handler(CommandHandler('read_event', event_read_handler))
Updater.dispatcher.add_handler(CommandHandler('edit_event', event_edit_handler))
Updater.dispatcher.add_handler(CommandHandler('delete_event', event_delete_handler))
Updater.dispatcher.add_handler(CommandHandler('display_event', event_display_handler))
