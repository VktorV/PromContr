import note


def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(note.note.to_string(notes))
        file.write('\n')
    file.close


def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note1 = note.note(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note1)
    except Exception:
        print('Нет сохраненных заметок...')
    finally:
        return array
