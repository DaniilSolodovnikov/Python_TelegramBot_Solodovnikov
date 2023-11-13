import os
def display_notes():
    notes = [note for note in os.listdir() if note.endswith(".txt")]
    sorted_notes = sorted(notes, key = len)