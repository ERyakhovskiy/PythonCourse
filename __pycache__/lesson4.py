

# def f(x):
#     return x*x
# print(f(5))
# a = f # Переименовали ф-ю f(переменная a хранит в себе ссылку на фун-ю f)
# print(type(a))
# print(a(5))

# # Создадим колькулятор

# def calk1(a): # создали ф-ю calk1
#     return a+a

# def calk2(a): # создали ф-ю calk2
#     return a*a

# def math(op, x): # создадим ф-ю в которую будут перед-ся 2 аргумента "op(operant), x"
#     print(op(x)) # печатаем ф-ю (op) c оператором (x)
    
# math(calk2, 5) # вызываейм ф-ю math(в 1 агрумент вызываем ф-ю calk2, 2-м арг. пер-ем знач-е 5 )
# # мы  передаем в ф-ю math ф-ю calk1(пер-я op имеет ссылку на ф-ю calk2)
# # Затем мы ее вызываем и выводим на экран


# # Тоже самое можно дел-ть с несколькими переменными:
# def calk1(a, b): # создали ф-ю calk1
#     return a + b

# def calk2(a, b): # создали ф-ю calk2
#     return a * b

# def math(op, x, y): # создадим ф-ю в которую будут перед-ся 3 аргумента "op(operant), x, y"
#     print(op(x, y)) # печатаем ф-ю (op) c операторами (x, y)
    
# math(calk1, 5, 45)

'''
Сокращение кода
Например генератор списков(где мы все пишем в одну строчку)

Лямда функции:
'''

# def calk2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))

# # Не сокращенный вариант
# def calk1(a, b): # создали ф-ю calk1
#      return a + b
 
# # 1-й вариант сокращения
# calk1 = lambda a,b: a+b # Создадим Лямда ф-ю calk1 и передам 2 знач-я"a,b" через ":" покажу, что будет делать программа(возвращать сумму чисел)

# math(calk1, 5, 45) # 
# # 2-й (более короткий) вариант сокращения
# math(lambda a,b: a + b, 5, 45)

# # Т.Е. мы в оперативной памяти выделяем участок под ф-ю и передаем ссылку на этот участок
# # а затем с помощью ф-ии "op" вызваем эту ф-ю

'''
Задача для самостоятельного решения

1. В списке хранятся числа. Нужно выбрать только четные числа
и составить список пар(число; квадрат числа).

Пример: 1 2 3 5 8 15 23 38
Получить: [(2,4), (8,64), (38, 1444)]
'''

# data = [1, 2, 3, 5, 8, 15, 23, 38] # Зададим список data
# res = list() # Создадим список res в котором будет выводиться рез-т

# for i in data: # Пройдемся по всем эл-м списка data И каждый раз будем пров-ть
#     if i % 2 == 0: # Если пер-я i делиться на 2  без остатка(т.е. эл-т четный)
#         res.append((i, i**2))# то мы в список res будем добавлять новое значение .append(i,  и i в квадрате)
# print(res)

# # Улучшим код исп-я Лямда фун-ии:

# def select(f, col): # Создадим ф-ю select в кот-ю будем передавать саму ф-ю f и значение col
#     return [f(x) for x in col]# Она нам будет возвращать список в котором мы к каждому эл-ту будем применять ф-ю f(x) и
# # мы должны пройтись по всем эл-м

# def where(f, col):# Созд. ф-ю where в кот. будем пер-ть 2 знач-я f  и col
#     return [x for x in col if f(x)] # она будет возвращать x когда мы пройдемся по всем эл-м с условием если выполнилось f(x)

# data = [1, 2, 3, 5, 8, 15, 23, 38] # Зададим список data
# res = select(int, data) # Создадим список res путем вызова ф-ии select и приведм к типу int список data
# print(res)
# res = where(lambda x: x % 2 == 0, res) # снова обращаемся к res используя ф-ю where (будем делать выборку)
# # создадим ф-ю lambda которая принимает значение x и возвращает true или false(x%2==0) и передаем res
# print(res)

# res = list(select(lambda x: (x, x**2), res))# Опять изменяем список res: делаем выборку
# # Т.Е. мы вызываем ф-ю select и преобразовываем список res и вынемаем рез-т из кортежа
# print(res)


'''
Функция map:
принимает на вход 2 аргумнта
1-й арг. это сама ф-я
2-й арг. это объект
Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и
возвращает итератор с новыми объектами.


'''
# list_1 = [x for x in range(1, 20)] # Создадим список list_1 через генератор списков()
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1)) #список list_1 равен списку list в кот-й мы вызываем ф-ю map и
# # применять к ней ф-ю которую мы напишем через lambda(к x прибавляем 10) а также передадим список list_1 который мы хотим применять
# print(list_1)

'''
Задача: С клавиатуры вводится некий набор числе, в качестве резделителя
используется пробел. Этот набор чисел будет считан в качестве строки.
Как превратить list строк в list чисел?
'''

# Небольшое отступление:

# # ф-я .split() преобразует строку в список используя по умолчанию в качестве разделителя пробел
# # , но мы можем использовать любой знак

# data = '15 156 96 3 5 8 52 5' # создадим строку data
# print(data)

# # # преобразем строку data в список строк
# # data = data.split() 
# # print(data)

# # Теперь преобразуем список строк в список чисел
# data = list(map(int, data.split())) # сделаем data споском с ф-ей map в кот-й к каждому объекту "data.split" мы будем применять ф-ю int
# print(data)



'''
Решение:
'''

# def where(f, col):
#     return [x for  x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# print(res)
# res =where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: x ** 2, res))
# print(res)





'''
Функция  filter
Она фильтрует какието значения
На входи принемает 2 аргумента:
1-й арг. сама ф-я
2-й арг. объект


Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
возвращает итератор с теми объектами, для которых функция вернула True.
(т.е. Возвращает только те эл-ты(объекты) для которых вызов ф-ии(кот. мы передали) вернули знач-е true)
'''

# data = [15, 9, 36, 175]# Создадим список data 
# # вернем те числа которые будут заканчиваться на 5
# res = list(filter(lambda x: x % 10 == 5, data))# Создадим список res в кот. мы будем исп-ть list и прим-ть filter ко всем эл-м
# # (labda x будет возвращать значение в том случае если x % 10 и получили 5, и передали список data)
# print(res)






data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
print(res)
res =filter(lambda x: x % 2 == 0, res)
print(res)
res = list(map(lambda x: x ** 2, res))
print(res)
