import os.path
def build_note(note_text, note_name):
    try:
        with open(f'{note_name}.txt', 'w', encoding='utf-8') as file:
            file.write(note_text)
        print(f'Заметка {note_name} создана')
    except:
        print('Произошла ошибка')

def create_note():
    try:
        note_name = input('Введите название заметки')
        note_text = input('Введите текст заметки')
        build_note(note_text, note_name)
    except:
        print('Произошла ошибка')

def read_note():
    try:
        note_name = input('Введите название заметки')
        file_path = os.path.join("./", note_name)
        if os.path.isfile(file_path):
            with open(file_path, "r") as f:
                content = f.read()
                print(content)
        else:
         print("Заметка не найдена.")
    except:
        print('Произошла ошибка')

def edit_note():
    try:
        note_name = input('Введите название заметки')
        file_path = os.path.join("./", note_name)
        if os.path.isfile(file_path):
            with open(file_path, "w") as f:
                content = f.write()
        else:
            print("Заметка не найдена.")
    except:
        print('Произошла ошибка')


def delete_note():
    try:
        note_name = input('Введите название заметки')
        file_path = os.path.join("./", note_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
        else:
            print("Заметка не найдена.")
    except:
        print('Произошла ошибка')

from main5 import display_sorted_notes

functions = 'build_note', 'create_note', 'read_note', 'edit_note', 'delete_note', 'display_sorted_notes'
menu = ''
for function in functions:
    menu += 'Выберите функцию: ' + function + '\n'
print(menu)

for function in functions:
    if function == 'build_note':
        print('Создать текстовый файл')
    elif function == 'create_note':
        print('Задать имя заметке')
    elif function == 'read_note':
        print('Считать содержимое заметки')
    elif function == 'edit_note':
        print('Обновить содержимое заметки')
    elif function == 'delete_note':
        print('Удалить заметку')
    else:
        print('Сортировать заметку')


user_input = input()
if user_input == 'build_note':
    build_note()
elif user_input == 'create_note':
    create_note()
elif user_input == 'read_note':
    read_note()
elif user_input == 'edit_note':
    edit_note()
elif user_input == 'delete_note':
    delete_note()
else:
    print('Такой функции не существует.')


def main():
    try:
        build_note()
        create_note()
        read_note()
        edit_note()
        delete_note()
        display_sorted_notes()
    except:
        print('Произошла ошибка')

import os
import datetime

class Calendar:
    def __init__(self):
        self.events = {}

    def create_event(self, event_name, event_date, event_time, event_details):
        event_id = len(self.events) + 1
        event = {
            'id': event_id,
            'name': event_name,
            'date': event_date,
            'time': event_time,
            'details': event_details
        }
        self.events[event_id] = event
        return event_id

    def read_event(self, event_id):
        if event_id in self.events:
            return self.events[event_id]
        return 'Event not found'

    def edit_event(self, event_id, new_details):
        if event_id in self.events:
            self.events[event_id]['details'] = new_details
        return 'Event not found'

    def delete_events(self, event_id):
        if event_id in self.events:
            del self.events[event_id]
        return 'Event not found'

    def display_events(self):
        for event_id, event in self.events.items():
            print(f"Event ID: {event_id}, Name: {event['name']}, Date: {event['date']}, Time: {event['time']}, Details: {event['details']}")


calendar = Calendar()

def event_create_handler(context, update):
  try:
      if len(update.message.text) >= 14:
        event_name = update.message.text[14:]

        try:
            event_date = "2023-03-14"
            event_time = "14:00"
        except:
            context.bot.send_message(chat_id=update.message.chat_id, text=f'Ошибка при определении даты и времени события {event_name}')

        event_id = calendar.create_event(event_name, event_date, event_time, event_details)
        context.bot.send_message(chat_id=update.message.chat_id, text=f"Событие {event_name} создано и имеет номер {event_id}.")
      else:
        context.bot.send_message(chat_id=update.message.chat_id, text='Сообщение слишком короткое')
  except:
      context.bot.send_message(chat_id=update.message.chat_id, text="При создании события произошла ошибка.")


functions_clss = 'create_event', 'read_event', 'edit_event', 'delete_event', 'display_events' #Создаем выбор функции из класса
menu_clss = ''
for function_clss in functions_clss:
    menu_clss += 'Выберите функцию: ' + functions_clss + '\n'
print(menu_clss)
for function_clss in functions_clss:
    if function == 'create_event':
        print('Создать заметку')
    elif function == 'read_event' :
        print('Прочитать заметку')
    elif function == 'edit_event' :
        print('Редактировать заметку')
    elif function == 'delete_event' :
        print('Удалить заметку')
    elif function == 'display_events' :
        print('Отобразить заметку')
    else:
        print('Такая функция не предусмотрена')

