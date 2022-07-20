#Эта программа создает 100 файлов с 100 строк и определенным ключом, имеет графическую оболочку и может объединить два файла, удалив определенные строки
import os
import random
import re
import string
from datetime import date
import sqlite3
import csv
import PySimpleGUI
import pandas as pd


#Создание графического интерфейса
layout = [
    [PySimpleGUI.Text('File1'), PySimpleGUI.InputText(readonly=True, key='-fileGrowse0-'), PySimpleGUI.FileBrowse()],
    [PySimpleGUI.Text('File2'), PySimpleGUI.InputText(readonly=True, key='-FileBrowse-'), PySimpleGUI.FileBrowse(), PySimpleGUI.Checkbox('del lines with 2020', key='-check-')],
    [PySimpleGUI.Output(size=(88, 20))],
    [PySimpleGUI.Button('Generate'), PySimpleGUI.Button('Compare')]
]
window = PySimpleGUI.Window('task', layout)
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Generate': #Генерация файлов
        lines = 0
        str1 = string.ascii_lowercase
        str2 = string.ascii_uppercase
        str3 = str1 + str2
        ls = list(str3)
        random.shuffle(ls)
        lat = ''.join([random.choice(ls) for x in range(10)])
        Ru = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
        ru = 'йцукенгшщзхъфывапролджэячсмитьбю'
        str4 = Ru + ru
        ls1 = list(str4)
        random.shuffle(ls1)
        rus = ''.join([random.choice(ls1) for y in range(10)])
        start_date = date(day=1, month=1, year=2015).toordinal()
        end_date = date(day=31, month=12, year=2020).toordinal()
        random_day = date.fromordinal(random.randint(start_date, end_date))
        data1 = random.randint(1, 100000000)
        data = random.uniform(1, 20)
        data2 = round(data, 8)
        for i in range(1, 101):
            file_name = '{}.txt'.format(i)
            with open(file_name, 'w') as f:
                count = 0
                while count < 100:
                    count = count + 1
                    f.writelines(str(random_day.strftime("%d.%m.%Y")))
                    f.writelines(str(' || '))
                    f.writelines(str(lat))
                    f.writelines(' || ')
                    f.writelines(str(rus))
                    f.writelines(' || ')
                    f.writelines(str(data1))
                    f.writelines(' || ')
                    f.writelines(str(data2))
                    f.writelines(' ||\n')
                    start_date = date(day=1, month=1, year=2015).toordinal()
                    end_date = date(day=31, month=12, year=2020).toordinal()
                    random_day = date.fromordinal(random.randint(start_date, end_date))
                    str2 = string.ascii_uppercase
                    str3 = str1 + str2
                    ls = list(str3)
                    random.shuffle(ls)
                    lat = ''.join([random.choice(ls) for x in range(10)])
                    Ru = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
                    ru = 'йцукенгшщзхъфывапролджэячсмитьбю'
                    str4 = Ru + ru
                    ls1 = list(str4)
                    random.shuffle(ls1)
                    rus = ''.join([random.choice(ls1) for y in range(10)])
                    data = random.uniform(1, 20)
                    data1 = random.randint(1, 100000000)
                    data2 = round(data, 8)
                else:
                    f.close()
    if event == 'Compare':
           if values['-fileGrowse0-'] and values['-FileBrowse-']:
               file1 = re.findall('.+:\/.+\.+.', values['-fileGrowse0-'])
               file2 = re.findall('.+:\/.+\.+.', values['-FileBrowse-'])
               isitago = 1
               if isitago == 1:
                   filename = []
                   filename.append(values['-fileGrowse0-'])
                   filename.append(values['-FileBrowse-'])
                   with open('comparedfile.txt', 'w') as outfile:
                        for path in filename:
                            with open(path) as infile:
                                for line in infile:
                                    outfile.write(line)
                   if values['-check-'] == True:
                        cmd = 'findstr /V 2020  comparedfile.txt > comparedfile1.txt'
                        os.system(cmd)
                        with open('comparedfile.txt') as first:
                            fir = [row.rstrip() for row in first]
                        with open('comparedfile1.txt') as second:
                            sec = [row.rstrip() for row in second]
                            len1 = len(fir) - len(sec)
                        print('Deleted: {} files' .format(len1))
                        os.remove('comparedfile.txt')

