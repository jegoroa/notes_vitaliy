from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QHBoxLayout,QTextEdit,QListWidget,QInputDialog
import os
 
data = {}

#переделать всё в текстовые файлы
#listdir читает все файлы из текущей папки
for file in os.listdir():
    if file.endswith(".txt"): #берем только формат .txt
        name = file[:-4] #срезаем 4 символа с конца, чтобы названия заметок были без .txt на конце

        data[name] = open(file,encoding='utf-8').read() #загружаем в старом формате, ключ - название заметки(файла), 
                                        #значение - то, что прочитываем из файла функцией read()

print(data)

def show_note():
    key = names_notes.selectedItems()[0].text()
    note_edit.setText(data[key])

#сделать def с сохранением заметки 
def save_text_to_file(name):
    #вызывается при создании новой, или сохранении существующей заметки
    new_note = f"{name}.txt"
    with open(new_note, "w",encoding='utf-8') as file:
        file.write(data[name])
    print(data,name)

def save_note():
    #это обработчик для кнопки
    key = names_notes.selectedItems()[0].text() #получаем название, какую заметку сохранять
    new_text = note_edit.toPlainText()
    data[key] = new_text #тоже самое что при создании заметки
    save_text_to_file(key)

#shiwa - бог разрушения, логично)
def shiwa():
    key = names_notes.selectedItems()[0].text() #получаем название, какую заметку удалять
    note_file = f"{key}.txt"
    os.remove(note_file)
    del data[key] #из словаря который в памяти программы - тоже надо заметку выкинуть

    names_notes.clear() #очищаем и добавляем оставшиеся
    names_notes.addItems(data)

#почему это называется каким то индийским божеством, а не new_note например?)
def brahma():
    #тут как и было, запрос названия через QInputDialog
    key,result = QInputDialog.getText(winrar,'Добавить заметку','Название заметки')
    if result:
        new_text = note_edit.toPlainText()
        data[key] = new_text
        save_text_to_file(key) #тут аргумент key чтобы было понятно, какую конкретно заметку хотим сохранить
        
        names_notes.clear() #очищаем и добавляем обновленный словарь
        names_notes.addItems(data)    

appppp =QApplication([])
winrar = QWidget()
winrar.show()
winrar.setWindowTitle('Умные заметки')
buton_create = QPushButton('Создать') 
buton_create.clicked.connect(brahma)
buton_save = QPushButton('Сохранить') 
buton_save.clicked.connect(save_note)
buton_delete = QPushButton('Удалить') 
buton_delete.clicked.connect(shiwa)
note_edit = QTextEdit('')
names_notes = QListWidget()

names_notes.addItems(data)
names_notes.itemClicked.connect(show_note)

linel = QHBoxLayout()
liner = QVBoxLayout()
linel.addWidget(note_edit)
linel.addLayout(liner)
liner.addWidget(QLabel('Список заметок'))
liner.addWidget(names_notes)
liner.addWidget(buton_create)
liner.addWidget(buton_save)
liner.addWidget(buton_delete)

winrar.move(60,100)
winrar.setLayout(linel)
winrar.resize(750,500)
winrar.setStyleSheet('''font-size:20px''')  
winrar.show()
appppp.exec() 
