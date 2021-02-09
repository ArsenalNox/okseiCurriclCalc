from datetime import datetime
import sys 

help = """
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

timeNow = datetime.now()
def caclCurrentLess(time):
    #Расчитывает текущую пару или перемену, время до конца 
    if time.strftime("%A") == 'Thursday':
        #Четверг
        currentCurriculum = curriculumThurstday
    else: 
        #Будни
        currentCurriculum = curriculumReg
    for x in currentCurriculum:
        #(͡ ° ͜ʖ ͡ °) 
        start = assembleTime(currentCurriculum[x], True)
        end = assembleTime(currentCurriculum[x], False)
        if timeNow>start and timeNow<end:
            delta = end-timeNow
            minutes = round(int(delta.seconds/60))
            print('Сейчас идёт пара {}\nДо конца пары {} min\nКонец в {}'.format(x, str(minutes), currentCurriculum[x]['end']))
            return
    first = assembleTime(currentCurriculum["1"], True)
    last = assembleTime(currentCurriculum[str(len(currentCurriculum))])
    if timeNow>first and timeNow<last: 
        for x in currentCurriculum: #Поиск следующий пары 
            nextPara = assembleTime(currentCurriculum[x], True) #Парсим начало
            if nextPara>timeNow: #Первая пара, которая начинается после текущего времени = время до конца перемены 
                delta = nextPara-timeNow
                minutes = round(int(delta.seconds/60))
                print('Сейчас перемена перед парой {}\nДо конца перемены {} min\nНачало в {}'.format(x, minutes,currentCurriculum[x]['start']))
                return
        print('ERROR')
        return
    if timeNow>first and timeNow>last:
        print('Пары кончились')
        return
    if timeNow<first and timeNow<last:
        delta = assembleTime(currentCurriculum['1']['start']) - timeNow
        print('Пары ещё не начались\nДо начала первой пары {}'.format(delta))
        return


def printCurriculum(type):
    print('{}'.format(timeNow))
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
 
    elif type == 'now':
        #Полное 
        caclCurrentLess(timeNow)

def assembleTime(para, start=False):
    #Собирает объект datetime 
    if start:
        now = datetime.now()
        return now.replace(hour=int(para['start'].split(":")[0]), minute=int(para['start'].split(":")[1]))
    else:
        now = datetime.now()
        return now.replace(hour=int(para['end'].split(":")[0]), minute=int(para['end'].split(":")[1]))

arguments = sys.argv
arguments.pop(0)
printCurr = False 
listType = 'none'
if 'l'  in arguments:
    listType='full'
    printCurr = True
 
if 'lr' in arguments:
    listType='reg'
    printCurr = True

if 'lt' in arguments:
    listType='now'
    printCurr = True

if 'h' in arguments:
    print(help)
elif printCurr:
    printCurriculum(listType)
else:
    printCurriculum('now')

