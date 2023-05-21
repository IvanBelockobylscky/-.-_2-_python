from curses.ascii import isupper
from typing import Text
import re
import random
from math import *
import datetime
import itertools

print("Лабораторная работа №1")

#1)
try :
   number = float(input("Введите число "))
   assert number >= 0 
   rub = int(number)
   cope = int(round(number - rub,1)*100) 
   print(rub,"руб",cope,"коп")  
except AssertionError:
   print("Некоректный формат")   


list = input("Введите список через пробелы").split(" ") 
answerTwo = "True"  
i = 1;   
while len(list) >i: 
    if list[i-1]>=list[i]:
        answerTwo = "False"
        break
    i+=1
print(answerTwo)    

#2)
answerTree = ''
while True:
   cartNumber = input('введите номер кредитной карты (16 цифр): ')
   if len(cartNumber) != 16:
      print('некорректный номер карты, попробуйте еще раз')
   else:
      break
for number in range(16):
    if 3 < number < 12:
       answerTree += '*'
    else:
       answerTree += cartNumber[number]
print(answerTree)

#3)
text = input("Введите текст : ").split(" ")
answerTherd = ""
while len(answerTherd)!=len(text):
   for a in range(len(text)):
       if len(text[i])>7:
           answerTherd+=text[i]
           continue
       if 4<len(text[i])<7:
           answerTherd+=text[i]
           continue
       answerTherd+=text[i]
print(answerTherd)

#4)
text2 = input("Введите текст : ").split(" ")
for a in range(len(text2)):
    if text2[a][0].upper() == text2[a][0]:
        text2[a] = text2[a].upper()
print(" ".join(text2))

#5)
text3 = input("Введите текст : ")
for i in text3:
    quantity = 0 
    for a in text3:
        if i==a :
            quantity+=1
        if quantity == 2 :
           text3 = text3.replace(i,'')
print(text3)  

#6)
text4 = input("Введите текст : ").split(" ")
for i in range(len(text4)):
   result = re.search("www",text4[i])
   if result[0] == "www": 
       text4[i] = "http://"+text4[i]
   result = re.search(".com",text4[i])
   if result[0]!=".com" :
      text4[i]+=".com"
print(" ".join(text4))

#7)
n = random.randint(1, 10000)
array = {}
for i in range(n):
    array.pow(random.randint(1, 10))
for i in range(pow(2, ceil(log(n, 2))) - len(array)):
    array.append(0)
print(array)

#8)
n = random.randint(1, 10000)
array = []
for i in range(n):
    array.append(random.randint(1, 10))
for i in range(ceil(pow(n+1,2) - pow(n,2))):
    array.append(0)
print(array)

#9)
cash = {"1000": 5, "100": 10, "50": 4, "10": 3}
result = {}
res = ""
take_money = int(input("Введите сумму, которую хотите снять: "))
for i in cash.items():
    if take_money >= int(i[0]) and i[1] > 0:
        count = take_money//int(i[0])
        if count > i[1]:
            count = i[1]
        result.update({i[0]: count})
        cash.update({i[0]: cash.get(i[0]) - count})
        take_money -= count * int(i[0])
    if take_money == 0:
        for i in result.items():
            res += str(i[1]) + " * " + i[0] + " + "
        print(res[:-2])
        break
if take_money > 0:
    print("Операция не может быть выполнена!")

#10)
password = input("Введите пароль: ")
if password.isdigit():
    print("Пароль очень легко взломать")
if password.isalnum() and len(password)<=8:
    print("Пароль не совсем надежный")
if password.isalnum() and len(password)>=8:
    print("Пароль надежный")

#11)
def frange(s, e, step):
        while s < e:
            val = round(s , 1)
            s += step 
            yield val 

for x in frange(1, 5, 0.1): 
    print(x)  

#12)
def getFrames(signal, size, overlap):  
    size = round(size*overlap)
    start = 0 
    end = int(size)
    while start <= len(signal): 
        frame = signal[start:end]
        yield frame
        start += int(size)
        end += int(size)
signalList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for frame in getFrames(signalList, size=9, overlap=0.3):
    print(frame)

#13)
def extraEnumerate(x): 
        frac, cum = 0, 0
        for i in x:
            cum += i
            frac = cum / sum(x)
            ret = [0, i, cum, frac]
            yield ret 
x = [1, 3, 4, 2]
for i, elem, cum, frac in extraEnumerate(x):
    print(elem, cum, frac)

#14)
def non_empty(fn):
    def wrapper():
        array = fn()
        newArray = []  
        for i in array:
            if i is not None and i != "":  
                newArray.append(i) 
            return newArray
    return wrapper

@non_empty
def get_pages():
    return ["array", "", "", None, "f", "therd", "two"]

#15)
def preProcess(a=0.97): 
    def decorated(func):  
        def wrapper(arg): 
            for i, val in enumerate(arg):
                arg[i] = round(arg[i] - a * arg[i - 1], 2)
                ret = func(arg)
            return ret
        return wrapper
    return decorated
@preProcess(a=0.93)
def plotSignal(s):
    for sample in s:
        print(sample)
plotSignal([3, 2, 1, 14])

#16)
commands = [ 
        "Шахтер Донецк",
        "МЮ",
        "Динамо Киев",
        "Динамо",
        "Челси",
        "Реал Мадрид",
        "Аталанта",
        "Арсенал",
        "Бенфика",
        "Реал Бетис",
        "Сантос Лагуна",
        "Атлетико Минейро",
        "Кашима Антлерс",
        "Интернасьонал",
        "Валенсия",
        "ЦСК",
    ]
groups = []
for i in range(4):
    groups.append([])  
    for j in range(4):
        k = random.randint(
            0, len(commands) - 1
        ) 
        groups[i].append(commands.pop(k))
date = datetime.datetime(  
    datetime.datetime.today().year, 9, 14, random.randint(0, 23), random.randint(0, 59)
)
while date.weekday() != 2:
    date += datetime.timedelta(days=1)  
date_s = date 
for group in groups:  
    print("Группа : " + str(group))
    games = itertools.permutations(group, 2)
    for game in games:  
        date = datetime.datetime(  
            date.year,
            date.month,
            date.day,
            random.randint(0, 23),
            random.randint(0, 59),  
        )
        print(
            str(game[0])
            + " против "
            + str(game[1])
            + " : "
            + date.strftime("%d/%m/%Y, %H:%M")
        )
        date += datetime.timedelta(days=14)
        date = date_s  