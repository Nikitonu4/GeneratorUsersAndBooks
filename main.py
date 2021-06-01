from mimesis import Person
import rstr
from mimesis.builtins import RussiaSpecProvider
import random
import datetime
import radar
from faker import Faker
import requests

person = Person('ru')
ru = RussiaSpecProvider()

arr_RU = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Э', 'Ю', 'Я'];
arr_initials = []
used_books_in_person = []
words = []
arr_jounr = ["роман", "элегия", "пьеса", "ода", "былина", "рассказ","поэма","детектив","комедия"]
book_invent_numbers = []
arr_ages = [0, 12, 16 ,18]
final_books_list = []
final_readers_list = []

def generateSixSymbolsNumber():
    return rstr.digits(6, exclude='0')

def firstGenerateBooks():
    for i in range(0, 200):
        six_number = generateSixSymbolsNumber()
        if not six_number in book_invent_numbers:
            initials = str(random.choice(arr_RU)+"."+random.choice(arr_RU)+"."+person.surname())
            arr_initials.append(initials)
            book_name = random.choice(words).title()
            jounr = random.choice(arr_jounr)
            book_name = book_name.strip()
            age = random.choice(arr_ages)
            for count in range(1, 6):
                inv_number = str(six_number)+'-'+str(count)
                output_str = initials+","+book_name+","+inv_number+","+jounr+","+str(age)+","+str(5)+","
                final_books_list.append(output_str)
                book_invent_numbers.append(inv_number)

def secondGenerateBooks():
    for i in range(0, len(book_invent_numbers)):
        book = 0
        for used_book in used_books_in_person:
            if used_book.split("-")[0] == book_invent_numbers[i].split("-")[0]:
                book+=1
        if not book == 0:
            final_books_list[i]+=str(book)
        else:
            final_books_list[i] += "0"

def readData():
    for line in open("words.txt", "r").read().split("\n"):
        for unit in line.split(" "):
            if len(unit) > 2:
                words.append(unit)

def generatePersons():
    for i in range(0, 120):
        surname_name = person.full_name().replace(" ", ",")
        surname = surname_name.split(",")[1]
        name = surname_name.split(",")[0]

        patronimyc = ','+ru.patronymic()
        date = radar.random_datetime().strftime('%Y-%m-%d')
        books = ""
        for i in range(0, 3):
            invent_num = random.choice(book_invent_numbers)
            if not invent_num in used_books_in_person:
                used_books_in_person.append(invent_num)
                datasdachi = radar.random_datetime(start=date).strftime('%Y-%m-%d')
                books += invent_num+";"+datasdachi+";"


        output_str = surname+","+name+patronimyc+','+date+','+books
        output_str = output_str[:-1]
        final_readers_list.append(output_str)

readData()
firstGenerateBooks()
generatePersons()
secondGenerateBooks()

print("Книги")
for el in final_books_list:
    print(el)
print("Читатели")
for el in final_readers_list:
    print(el)
