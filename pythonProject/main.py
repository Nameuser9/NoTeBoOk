import notes


print("Здравствуйте , как вы хотите взаимодействовать с заметками: создать , посмотреть все заметки, искать , изменить , или же удалить ")

ch = input()
if ch == 'создать':
    notes.make_note()
if ch == 'посмотреть':
    notes.see_notes()
if ch == 'искать':
    notes.search_note()
if ch == 'удалить':
    notes.del_note()
if ch == 'изменить':
    notes.change_note()
