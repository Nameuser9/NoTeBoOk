import json
from pprint import pprint
from datetime import datetime as dt


def make_id():# СДЕЛАТЬ ОСВОБОЖДЕНИЕ НОМЕРА ID ПРИ УДАЛЕНИИ, номер должен быть
    id = 0
    if choice.RATIO() == 1:
        id = id + 1
    return id



def make_note():#сделать возможно id для каждой заметки
    print("введите заголовок заметки")
    name = input()
    # filename = name +".json"
    print("введите текст заметки")
    data = []
    while True:  # False - пустая строка
        seq = input('Введите строку: ')
        if seq:
            data.append(seq)
        else:
            break
    y = {"название": name, "содержание": data, "время": dt.now().strftime('%H:%M'), 'дата' : dt.now().strftime('%d.%m.%y')}
    with open('book.json', 'r+', encoding='UTF-8') as file:

        file_data = json.load(file)

        file_data["notes"].append(y)

        file.seek(0)

        json.dump(file_data, file,ensure_ascii=False, indent=4,sort_keys=False)


def search_note():# в работе
    print('по какому критерию выполнять поиск: названию, содержанию или же времени')
    fil = input()

    with open('book.json', 'r', encoding='UTF-8') as file:
        if fil == "названию":
            print('ваш запрос')
            req = input()
            data = json.load(file)
            minimal = 0
            for note in data['notes']:
                if note['название'] == req:
                    print(note)
                else:
                    None
                minimal += 1
           #  result = 'notes'.к(req)
           #  pprint(result)
           # return print(list(filter(lambda x: x["название"] == req, data)))
        if fil == "содержанию":
            print('ваш запрос')
            req = []
            while True:  # False - пустая строка
                seq = input('Введите строку: ')
                if seq:
                    req.append(seq)
                else:
                    break
            data = json.load(file)
            minimal = 0
            for note in data['notes']:
                if note['содержание'] == req:
                    print(note)
                else:
                    None
                minimal += 1
        if fil == "дате":
            print('ваш запрос (в формате дня.месяца.года)')
            req = input()
            data = json.load(file)
            minimal = 0
            for note in data['notes']:
                if note['дата'] == req:
                    print(note)
                else:
                    None
                minimal += 1

#filter(['название'] == req)
def change_note():
    print('какую часть необходимо изменить: название, содержание')
    fil = input()
    with open('book.json',"r" , encoding='UTF-8') as file:
        data = json.load(file)
        if fil == "название":
            name = input('введите старое название ')
            minimal = 0
            for note in data['notes']:
                if note['название'] == name:
                    print(note)
                    req = input('на что изменить название? ')
                    note['название'] = req
                    with open('book.json',"wt" ,  encoding='UTF-8') as file2:
                        json.dump(data,file2, ensure_ascii=False,indent=4 )
                else:
                    None
                minimal += 1
        if fil == "содержание":
            print('ваш запрос')
            name = input('введите старое название ')
            minimal = 0
            for note in data['notes']:
                if note['название'] == name:
                    print(note)
                    req = []
                    print('на что изменить содержание?')
                    while True:
                        seq = input('Введите строку: ')
                        if seq:
                            req.append(seq)
                        else:
                            break
                    note['содержание'] = req
                    with open('book.json', "wt", encoding='UTF-8') as file2:
                        json.dump(data, file2, ensure_ascii=False, indent=4)
                else:
                    None
                minimal += 1


def del_note():
    print('напишите название заметки, которую нужно удалить')
    order = input()
    with open("book.json",'r', encoding="utf-8") as read_file:
        data= json.load(read_file)
        minimal = 0
        for txt in data['notes']:
            if txt['название'] == order:
                data['notes'].pop(minimal)
            else:
                None
            minimal = minimal+1
    with open("book.json","w", encoding="utf-8") as write_file:
        json.dump(data, write_file, ensure_ascii=False, indent=4, sort_keys=True)


def see_notes():
    with open("book.json", encoding="utf-8") as read_file:
        superdata = json.load(read_file)
        dateorder = sorted(superdata['notes'] , key=lambda x: dt.strptime(x['дата'], '%d.%m.%y'), reverse=True)
        #orderednotes = json.dumps(superdata, sort_keys=False)
        pprint(dateorder)
        # for txt in dateorder['notes']:
        #     print(txt['название'], '-' , txt['содержание'] , ';' , txt['время'] ,' ', txt['дата'])


