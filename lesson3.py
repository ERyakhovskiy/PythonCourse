'''
Фнкции ________________________________________________


Задача
Необходимо создать функцию sumNumbers(n), которая будет
считать сумму всех элементов от 1 до n.
Решение:
1. Необходимо создать функцию:
def sumNumbers(n):
Очень важно понимать одну вещь, сколько аргументов мы передаем,
столько и принимаем. Или наоборот сколько аргументов мы
принимаем, столько и передаем.
В нашем случае функция sumNumbers принимает 1 аргумент(n).
принимает 1 аргумент(n).
'''

# def sum_numbers(n, y = "Hello"): # Создали фун-ию sum_numbers с аргументом n(Переменной y присвоили значение по умолчанию "Hello"(используется если не присваиваем другого значения))
#     print(y)
#     summa = 0 # Создали переменную summa
#     for i in range(1, n+1): # Пройдемся по циклу. Т.к. нужно считать с первого элемента пишем 1, чтобы посчитать сумму пишем n+1
#         summa += i # будем увеличивать summa на переменную i
#     # # print(summa) # выводим сумму
#     # return summa # Оператор return возвращает значение и заканчивает программу
#     return summa
    
# a = sum_numbers(5, 'qwerty') # Создали перменную a и присвоили ей функцию со значением 5 и 'qwerty' которая заменяет переменную по умолчанию

# # # sum_numbers(5) # вызвали ф-ю sum_numbers и Передали число 5 в пармаетрах 
# # print(sum_numbers(5))
# print(a) # Вывели результат

'''
Представим что мы хотим передать нашей ф-ии множество букв и получить единое слово
Но мы не знаем сколько будет букв

Напишем ф-ю которая будет принимать неограниченно кол-во переменных:
'''

# def sum_str(*args): # Используем "*" чтобы передать неограниченое кол-во переменных
#     res = '' # Создадим переменню res которая будет иметь тип данных строка 
#     for i in args: # Пройдемся по всем эл-ам переменной args
#         res += i # При каждой итерации к переменно res будет прибавляться переменная i
#     return res # Вернем переменню res
        
# print(sum_str('q', 'e', '1')) # Передаем ф-ии элементы q,e,1 и выводим в одним словом
# print(sum_str('q', 'e', '1', 'r', 'f'))
# # print(sum_str(1, 8, 9)) # Выдает ошибку ДЗ: Исправить ее





'''
Импорт модуля
'''


# import modul1 # Импортируем мудуль из файла modul1.py

# print(modul1.max1(5, 9)) # Обратимся к modul1. и вызовем ф-ю max1, и передадим значения 5 и 9


# # Мы можем сразу импортировать функцию

# from modul1 import max1

# print(max1(10,9))

# # Если мы не хотим перечислять фсе функциии
# from modul1 import * # Импортируем обсалютно все функции

# print(max1(3, 5))

# # Если мы хотим импортировать модуль напрямую

# import modul1 as m1 # Импортируем модуль как имя m1 и теперь мы обращаемся к модулю через m1

# print(m1.max1(6, 4))



# '''
# Рекурсия ________________________________________________
# Это функция которая вызывает саму себя



# Задача
# Пользователь вводит число n. Необходимо вывести n - первых
# членов последовательности Фибоначчи.
# Напоминание: Последовательно Фибоначчи, это такая последовательность, в
# которой каждое последующее число равно сумму 2-ух предыдущих.
# При описании рекурсии важно указать, когда функции надо остановиться и
# перестать вызывать саму себя. По-другому говоря, необходимо указать базис
# рекурсии
# '''

# def fib(n): # Создадим ф-ю fin которая будет принимать значение n
#     if n in [1, 2]: # Если пер. n будет находится в списке [1, 2]. Это базис для ряда фибоначи 
#         return 1 # то мы должны вернуть 1
#     # В противном случае мы будем возвращать рекурсию
#     return fib(n-1) + fib(n-2) # сумируем два предыдущих члена для получения нового члена фибоначи

# list_1 = [] # Создадим список list_1 в который будем записывать числа
# for i in  range(1, 10): # Прйдемся по циклу
#     list_1.append(fib(i)) # При каждой итерации цикла  в список list_1 мы будем добовлять вызов функции fib
# print(list_1)


'''
Алгоритмы ______________________________________________________
Это набор инструкций для выполнения некоторой задачи


Быстрая сортировка

Задача:

Два друга решили поиграть в игру: один загадывает число от 1 до 100, другой должен отгадать.
Согласитесь, что мы можем перебирать эти значения в случайном порядке, например: 32, 27, 60,
73… Да, мы можем угадать в какой-то момент, но что если мы обратиться к стратегии “разделяй
и властвуй” Обозначим друзей, друг_1 это Иван, который загадал число, друг_2 это Петр,
который отгадывает. Итак начнем:



Иван загадал число 77.
Петр: Число больше 50? Иван: Да.
Петр: Число больше 75? Иван: Да.
Петр: Число больше 87? Иван: Нет.
Петр: Число больше 81? Иван: Нет.
Петр: Число больше 78? Иван: Нет.
Петр: Число больше 76? Иван: Да
Число оказалось в диапазоне 76 < x < 78, значит это число 77. Задача решена. На самом деле мы
сейчас познакомились с алгоритмом бинарного поиска, который также принадлежит стратегии
“разделяй и властвуй”. Давайте перейдем к обсуждению программного кода быстрой
сортировки.
'''

# def quick_sort(array): # создадим ф-ю quick_sort а в параметр будем передовать массив array
#     if len(array) <= 1: # Если длинна массива меньше либо равна 1(Базис рекурсии. т.е место где она завершает свою работу) 
#         return array # то мы возвращаем массив
#     else: # Иначе мы будем выполнять некоторые действия
#         pivot = array[0] # Создадим переменную pivot в кот. будем сохранять первый эл-т
#     # Создадим два массива:
#     # 1-й массив
#     less = [i for i in array[1:] if i <= pivot] # будем класть зн-е i проходясь по циклу for i(берем все эл-ты после первого"[1:]")только те которые меньше либо равны переменной pivot
#     # 2-й массив
#     greater = [i for i in array[1:] if i > pivot] # будем класть зн-е i проходясь по циклу for i(берем все эл-ты после первого"[1:]")только те которые больше переменной pivot
#     return quick_sort(less) + [pivot] + quick_sort(greater) # Возвращаем значение меньше pivot + pivot+ боьше pivot и сортируем при помощи ф-ии quick_sort
#     # переменную pivot мы преобразовали в список [pivot], чтобы избежать ошибки типов
# print(quick_sort([10,5,2,3])) # [2, 3, 5, 10,]

'''
1-е повторение рекурсии:
○ array = [10, 5, 2, 3]
○ pivot = 10
○ less = [5, 2, 3]
○ greater = []
○ return quicksort([5, 2, 3]) + [10] + quicksort([])
● 2-е повторение рекурсии:
○ array = [5, 2, 3]
○ pivot = 5
○ less = [2, 3]
○ greater = []
○ return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что здесь помимо вызова рекурсии
добавляется список [10]
● 3-е повторение рекурсии:
○ array = [2, 3]
○ return [2, 3] # Сработал базовый случай рекурсии
На этом работа рекурсии завершилась и итоговый список будет выглядеть таким образом: [2, 3] + [5] + [10] = [2, 3, 5,
10]
'''



'''
Сортировка слиянием
'''

def merge_sort(nums): # Создадим ф-ю merg_sort и передадим туда значение nums
    # Будем список делить на два
    if len(nums) > 1: # Если длинна nums больше 1 то мы что то делаем
        mid = len(nums) // 2 # Создадим переменную mid в которой будет храниться зн-е "по середине"
        left = nums[:mid] # Создадим список где хр-ся левая часть(идем от начала до середины)
        right = nums[mid:]# Создадим список где хр-ся правая часть(идом от середины до конца)
        # Необходимо дальше делить списки по полам при помощи рекурсии пока не останется по дному значению
        # рекурсия:
        merge_sort(left) # Создадим ф-ю в которой будем вызывать левую часть
        merge_sort(right) # Создадим ф-ю в которой будем вызывать правую часть
        # Дальше надо все переменные соединить воедино
        i = j = k = 0 # создадим 3 переменные i,j,k, равные нулю
        # Создадим цикл while в кот будем класть все эл-ты последовательно
        while i < len(left) and j <len(right): # Будет вып-ся Пока i меньше len(left) и j меньше len(right)
            if left[i] < right[j]: # если эл-т [i] из списка left меньше чем [j] из списка right
                nums[k] = left[i]
                i += 1 # к переменной i добавим 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1 # Прибавляем 1 чтобы при каждой итерции прибавлялось новое значение
        # Допустим все эл-ты их списка left больше чем эл-ты из списка right
        # Пока у нас есть эл-т в левом списке мы добавляем их в конец
        # Либо пока у нас есть эл-т в правом всписке мы добавляем их в конец
        while i < len(left): # Пока переменная i < len(lift)
            nums[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right): # Пока переменная i < len(lift)
            nums[k] = right[j]
            j += 1
            k += 1
            
list1 = [1,2,32,43,5,3,54,65] # Создадим список list1
merge_sort(list1)   # Вызовем ф-ю merge_sort
print(list1)