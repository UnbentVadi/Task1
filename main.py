# -*- coding: utf-8 -*-
import re
import os
from bs4 import BeautifulSoup


def create_text_file():
    with open("main.html", encoding='utf-8') as markup:
        soup = BeautifulSoup(markup.read())
    with open("old_list.txt", "w") as f:
        f.write(soup.get_text())


def preformat():
        with open('list.txt', 'w') as f_out:
            with open('old_list.txt', 'r') as f_in:
                for line in f_in:
                    line = line.replace(":", " ")
                    new_str = ''.join(line.split('№')[1:])
                    f_out.write(new_str)
                f_out.close()
                os.remove('old_list.txt')


def formal():
    f = open('list.txt', 'r')
    text = f.read()
    f.close()
    Lixt = ['\([^)]*\)', '  ', ' , ', 'почтомат ',
            'Parcel Shop ', 'Мини-отделение, ',
            'Почтоматы в отделения Приватбанка',
            'ТОЧКА ВЫДАЧИ "ПРИВАТ БАНКА"''', '  ']

    for s in range(len(Lixt)):
        text = re.sub(Lixt[s], ' ', text)
        print(type(List))

    f = open('list.txt', 'w')
    print(type(text))
    f.write(text)
    f.close()


def main():
    create_text_file()
    preformat()
    formal()

main()
