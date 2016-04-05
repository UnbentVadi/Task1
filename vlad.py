# -*- coding: utf-8 -*-
import re
import os
from bs4 import BeautifulSoup
​​def create_text_file():
    with open("main.html", encoding='utf-8') as markup:
        soup = BeautifulSoup(markup.read())
    with open("old_list.txt", "w") as f:
        f.write(soup.get_text())
​
​
def preformat():
        with open('list.txt', 'w') as f_out:
            with open('old_list.txt') as f_in:
                for line in f_in:
                    line = line.replace(":", " ")
                    new_str = ''.join(line.split('№')[1:])
                    f_out.write(new_str)
                f_out.close()
                os.remove('old_list.txt')
​
​
def formal():
                    f = open('list.txt')
                    text = f.read()
                    f.close()
                    clean = re.sub('\([^)]*\)', '', text)
                    reclean = re.sub(' +', ' ', clean)
                    may = re.sub(' , ', '', reclean)
                    kish = re.sub('почтомат ', ' ', may)
                    parcel = re.sub('Parcel Shop ', ' ', kish)
                    number = re.sub('97', '97 ', parcel)
                    date = re.sub('349', '349 ', number)
                    last = re.sub \
                    ('Почтоматы в отделения Приватбанка', '', date)
                    lastt = re.sub(''' ТОЧКА ВЫДАЧИ "ПРИВАТ БАНКА" ''', ' ', last)
                    f = open('list.txt', 'w')
                    f.write(lastt)
                    f.close()
​
​
def main():
    create_text_file()
    preformat()
    formal()
​
main()