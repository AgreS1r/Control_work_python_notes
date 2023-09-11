## Для запуска программы нужно создать файл data в той же, где запускается код!!!

import os
import json
import datetime

DATA_DIR = "data"

def create_note():
    title = input("Введите заголовок заметки: ")
    message = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "title": title,
        "message": message,
        "timestamp": timestamp
    }
    note_id = save_note(note)
    print("Заметка успешно создана. ID заметки:", note_id)

def save_note(note):
    note_id = get_next_note_id()
    note["id"] = note_id
    filename = f"{DATA_DIR}/{note_id}.json"
    with open(filename, "w") as file:
        json.dump(note, file, indent=4)
    return note_id

def get_next_note_id():
    note_ids = [int(filename.split(".")[0]) for filename in os.listdir(DATA_DIR) if filename.endswith(".json")]
    if note_ids:
        return max(note_ids) + 1
    else:
        return 1

def read_notes():
    print("Список заметок:")
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".json"):
            with open(f"{DATA_DIR}/{filename}", "r") as file:
                note = json.load(file)
                print("ID:", note["id"])
                print("Заголовок:", note["title"])
                print("Текст:", note["message"])
                print("Дата/время создания:", note["timestamp"])
                print()

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    filename = f"{DATA_DIR}/{note_id}.json"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            note = json.load(file)
        print("Редактирование заметки:")
        print("Заголовок:", note["title"])
        print("Текст:", note["message"])
        new_title = input("Введите новый заголовок (оставьте пустым, если не хотите менять): ")
        new_message = input("Введите новый текст (оставьте пустым, если не хотите менять): ")
        if new_title:
            note["title"] = new_title
        if new_message:
            note["message"] = new_message
        with open(filename, "w") as file:
            json.dump(note, file, indent=4)
        print("Заметка успешно отредактирована.")
    else:
        print("Заметка с таким ID не найдена.")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    filename = f"{DATA_DIR}/{note_id}.json"
    if os.path.exists(filename):
        os.remove(filename)
        print("Заметка успешно удалена.")
    else:
        print("Заметка с таким ID не найдена.")

def filter_notes_by_date():
    date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        print("Список заметок, созданных после", date_str)
        for filename in os.listdir(DATA_DIR):
            if filename.endswith(".json"):
                with open(f"{DATA_DIR}/{filename}", "r") as file:
                    note = json.load(file)
                    note_date = datetime.datetime.strptime(note["timestamp"], "%Y-%m-%d %H:%M:%S").date()
                    if note_date > date:
                        print("ID:", note["id"])
                        print("Заголовок:", note["title"])
                        print("Текст:", note["message"])
                        print("Дата/время создания:", note["timestamp"])
                        print()
    except ValueError:
        print("Некорректный формат даты.")

def main():
    print("Добро пожаловать в программу заметок!")
    while True:
        print()
        print("Выберите команду:")
        print("1. Создать новую заметку")
        print("2. Просмотреть список заметок")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Фильтровать заметки по дате")
        print("0. Выйти из программы")
        choice = input("Введите номер команды: ")
        if choice == "1":
            create_note()
        elif choice == "2":
            read_notes()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            filter_notes_by_date()
        elif choice == "0":
            break
        else:
            print("Некорректная команда. Попробуйте ещё раз.")

if __name__ == "__main__":
    main()
