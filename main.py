from datetime import date, datetime
import sys 

"""
Аргуметы:
    При отсутсвии аргумента выводит:
        номер текущий пары 
        время до конца пары 
        если перемена то время до конца перемены, номер след перемены

    l  : Возвращает лист пар (обычный+четверг)
    lr : Лист пар без четверга 
    lt : Лист на сегодня
    
    h  : Выводит эту страницу 
"""

curriculumReg = { #Обычное расписание 
        "1": {'start':'8:30' , 'end':'10:00'},
        "2": {'start':'10:10', 'end':'11:40'},
        "3": {'start':'12:00', 'end':'13:30'},
        "4": {'start':'13:50', 'end':'15:20'},
        "5": {'start':'15:40', 'end':'17:10'},
        "6": {'start':'17:20', 'end':'18:50'}
        }

curriculumThurstday = { #Расписание на четверг 
        "1": {'start':'8:30' , 'end':'10:00'},
        "2": {'start':'10:10', 'end':'11:40'},
        "3": {'start':'12:00', 'end':'13:30'},
        "4": {'start':'13:40', 'end':'14:25'},
        "5": {'start':'14:45', 'end':'16:15'},
        "6": {'start':'16:35', 'end':'18:05'},
        "7": {'start':'18:15', 'end':'19:15'}
        }

timeNow = datetime.now().time()
def caclCurrentLess(time):
    #Расчитывает текущую пару или перемену, время до конца 
    if time.strftime("%A") == 'Thursday':
        #Четверг
        currentCurriculum = curriculumThurstday
    else: 
        #Будни
        currentCurriculum = curriculumReg
    print('Время сейчас {}'.format(timeNow))
    for x in currentCurriculum:
        now = datetime.now()
        formattedStart = now.replace(hour=8)

    print('До конца пары №6 12 минут, конец в 18:05')
    print('До конца перемены: 12 минут, Пара №6 начнётся в 16:35')

def printCurriculum(type):
    #Выводит расписание 
    if   type == 'reg':
        #Обычное + чет
        print('Будни')
        for para in curriculumReg:
            print("{}: {} - {}".format(para, curriculumReg[para]['start'], curriculumReg[para]['end']) )

    elif type =='full':
        #Полное
        print('Будни')
        for para in curriculumReg:
            print("{}: {} - {}".format(para, curriculumReg[para]['start'], curriculumReg[para]['end']) )
        print('Четверг')
        for para in curriculumThurstday:
            print("{}: {} - {}".format(para, curriculumThurstday[para]['start'], curriculumThurstday[para]['end']) )

    elif type == 'short':
        #Сокращенное 
        print('short')

    elif type == 'now':
        #Полное 
        caclCurrentLess(timeNow)

arguments = sys.argv
arguments.pop(0)
printCurr = False 

if 'l'  in arguments:
    listType='full'
    printCurr = True
 
if 'lr' in arguments:
    listType='reg'
    printCurr = True

if 'lt' in arguments:
    listType='now'
    printCurr = True
    
if 'ls' in arguments:
    listType='short'
    printCurr=True

if printCurr:
    printCurriculum(listType)
else:
    printCurriculum('now')

