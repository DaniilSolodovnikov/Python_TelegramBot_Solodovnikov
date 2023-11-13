import os.path
def build_note(note_text, note_name):
    with open(f'{note_name}.txt', 'w', encoding='utf-8') as file:
        file.write(note_text)
    print(f'Заметка {note_name} создана')

def create_note():
    note_name = input('Введите название заметки')
    note_text = input('Введите текст заметки')
    build_note(note_text, note_name)

def read_note():
    note_name = input('Введите название заметки')
    file_path = os.path.join("./", note_name)
    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            content = f.read()
            print(content)
    else:
        print("Заметка не найдена.")

def edit_note():
    note_name = input('Введите название заметки')
    file_path = os.path.join("./", note_name)
    if os.path.isfile(file_path):
        with open(file_path, "w") as f:
            content = f.write()
    else:
        print("Заметка не найдена.")


def delete_note():
    note_name = input('Введите название заметки')
    file_path = os.path.join("./", note_name)
    if os.path.isfile(file_path):
        remove(file_path)
    else:
        print("Заметка не найдена.")

def main():
    build_note()
    create_note()
    read_note()
    edit_note()
    delete_note()

