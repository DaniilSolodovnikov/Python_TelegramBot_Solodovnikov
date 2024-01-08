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