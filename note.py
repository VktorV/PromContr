from datetime import datetime
import uuid


class note:
    def __init__(self, id = str(uuid.uuid1())[0:3],  title = "текст", body = "текст", date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(note1):
        return note1.id

    def get_title(note1):
        return note1.title

    def get_body(note1):
        return note1.body

    def get_date(note1):
        return note1.date

    def set_id(note1):
        note1.id = str(uuid.uuid1())[0:3]

    def set_title(note1, title):
        note1.title = title

    def set_body(note1, body):
        note1.body = body

    def set_date(note1):
        note1.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note1):
        return note1.id + ';' + note1.title + ';' + note1.body + ';' + note1.date

    def map_note(note1):
        return '\nID: ' + note1.id + '\n' + 'Название: ' + note1.title + '\n' + 'Описание: ' + note1.body + '\n' + 'Дата публикации: ' + note1.date
