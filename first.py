

def write_notes(file_name):
    with open(file_name, "w") as file:
        note = input("Write a new note: ")
        file.write(note + "\n")

def read_notes(file_name):
    with open(file_name, "r") as file:
        notes = file.readlines()
        for note in notes:
            print(note.strip())

def append_notes(file_name):
    with open(file_name, "a") as file:
        note = input("Write additional note to append: ")
        file.write(note + "\n")

file_name = "notes.txt"

# Write a new note
write_notes(file_name)

# Read existing notes
print("\nReading notes from the file:")
read_notes(file_name)

# Append new notes
append_notes(file_name)

# Read updated notes
print("\nUpdated notes in the file:")
read_notes(file_name)
