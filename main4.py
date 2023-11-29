import os
def display_notes():
    notes = [note for note in os.listdir() if note.endswith(".txt")]
    print("Все заметки:")
    for note in notes:
        print(note)