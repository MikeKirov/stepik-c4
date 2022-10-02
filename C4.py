1.2 / 9
# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.
# Вашей программе доступна переменная objects, которая ссылается на список, содержащий не более 100 объектов.
# Выведите количество различных объектов в этом списке.
# Формат ожидаемой программы:
# ans = 0
# for obj in objects: # доступная переменная objects
#     ans += 1
# print(ans)
#
# Примечание:
# Количеством различных объектов называется максимальный размер множества объектов,
# в котором любые два объекта являются различными.
#
# Рассмотрим пример:
# objects = [1, 2, 1, 2, 3] # будем считать, что одинаковые числа соответствуют одинаковым объектам,
# а различные – различным
# Тогда все различные объекты являют собой множество {1, 2, 3} Таким образом, количество различных объектов равно трём.

# objects = [1, 2, 1, 5, True, False, True, 'false', [], [1, 2], [1, 2]]
# s = []
# for i in objects:
#     if i not in s:
#         s.append(i)
# print(len(s))
#######################################################################################################################
# print(len(set(map(id, objects))))


1.3 / 9
# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую
# самое маленькое целое число y, такое что:
# y больше или равно x
# y делится нацело на 5
# на вход функция принимает целое число. Написать функцию, которая вернет такое целое число которое будет не
# меньше(но может быть равным) чем принятый аргумент и которое при этом будет делиться без остатка на 5

# def closest_mod_5(x):
#     if x % 5 == 0:
#         return x
#     return closest_mod_5(x + 1)
# print(closest_mod_5(int(input())))

1.3 / 15
# Сочетанием из n элементов по k называется подмножество этих n элементов размера k.
# Два сочетания называются различными, если одно из сочетаний содержит элемент, который не содержит другое.
# Числом сочетаний из n по k называется количество различных сочетаний из n по k. Обозначим это число за C(n, k).
# Пример:
# Пусть n = 3, т. е. есть три элемента (1, 2, 3). Пусть k = 2.
# Все различные сочетания из 3 элементов по 2: (1, 2), (1, 3), (2, 3).
# Различных сочетаний три, поэтому C(3, 2) = 3.
# Несложно понять, что C(n, 0) = 1, так как из n элементов выбрать 0 можно единственным образом,
# а именно, ничего не выбрать.
# Также несложно понять, что если k > n, то C(n, k) = 0, так как невозможно, например, из трех элементов выбрать пять.
# Для вычисления C(n, k) в других случаях используется следующая рекуррентная формула:
# C(n, k) = C(n - 1, k) + C(n - 1, k - 1).
# Реализуйте программу, которая для заданных n и k вычисляет C(n, k).

# def C(x, y):
#     if y > x:
#         return 0
#     if y == 0:
#         return 1
#     return C(x - 1, y) + C(x - 1, y - 1)
# n, k = map(int, input().split())
# print(C(n, k))


1.4 / 10
# '''Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку
# создания пространств имен и добавление в них переменных.
#   В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
#   Вашей программе на вход подаются следующие запросы:
#     create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
#     add <namespace> <var> – добавить в пространство <namespace> переменную <var>
#     get <namespace> <var> – получить имя пространства, из которого будет взята переменная <var> при запросе из
#     пространства <namespace>, или None, если такого пространства не существует
#   Рассмотрим набор запросов:
#     add global a
#     create foo global
#     add foo b
#     create bar foo
#     add bar a
#   В основном теле программы мы объявляем переменную a, тем самым добавляя ее в пространство global. Далее мы объявляем
# функцию foo, что влечет за собой создание локального для нее пространства имен внутри пространства global.
#   В нашем случае, это описывается командой create foo global. Далее мы объявляем внутри функции foo функцию bar,
# тем самым создавая пространство bar внутри пространства foo, и добавляем в bar переменную a.
# Добавим запросы get к нашим запросам
#   get foo a
#   get foo c
#   get bar a
#   get bar b
# Представим как это могло бы выглядеть в коде
#     a = 0
#     def foo():
#         b = 1
#         get(a)
#         get(c)
#         def bar():
#             a = 2
#             get(a)
#             get(b)
#   Результатом запроса get будет имя пространства, из которого будет взята нужная переменная.
#   Например, результатом запроса get foo a будет global, потому что в пространстве foo не объявлена переменная a, но в
# пространстве global, внутри которого находится пространство foo, она объявлена. Аналогично, результатом запроса get
# bar b будет являться foo, а результатом работы get bar a будет являться bar.
#   Результатом get foo c будет являться None, потому что ни в пространстве foo, ни в его внешнем пространстве global
# не была объявлена переменная с.
#   Более формально, результатом работы get <namespace> <var> является
# <namespace>, если в пространстве <namespace> была объявлена переменная <var>
# get <parent> <var> – результат запроса к пространству, внутри которого было создано пространство <namespace>, если
# переменная не была объявлена
# None, если не существует <parent>, т. е. <namespace> – это global
#   Формат входных данных
#   В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
#   В каждой из следующих n строк дано по одному запросу. Запросы выполняются в порядке, в котором они даны во входных
# данных. Имена пространства имен и имена переменных представляют собой строки длины не более 10, состоящие из строчных
# латинских букв.'''
#
# d = {'global': ['None']}  # словарь списков(родитель,переменные)
# for data, ns, var in [input().split() for _ in range(int(input()))]:
#     if data == "create":
#         d[ns] = [var]  # создание нового списка в словаре
#     elif data == "add":
#         d[ns].append(var)  # -добавить в список новую переменную
#     elif data == 'get':  # поиск переменной (циклом)
#         while ns != 'None' and var not in d[ns]: # если нет в пространстве-меняем на родителя(пока не None)
#             ns = d[ns][0]
#         print(ns)

#######################################################################################################################
# def create(namespace, parent):
#     """ создать новое пространство имен с именем <namespace> внутри пространства <parent>"""
#     if namespace not in scope:
#         scope[namespace] = {}
#         scope[namespace]['func'] = []
#         scope[namespace]['vars'] = []
#         scope[parent]['func'].append(namespace)
#         scope[namespace]['parent'] = parent
#
#
# def add(namespace, var):
#     """ добавить в пространство <namespace> переменную <var>"""
#     if var not in scope[namespace]['vars']:
#         scope[namespace]['vars'].append(var)
#     elif var in scope[namespace]:
#         scope[namespace]['vars'].append(var)
#
#
# def get(namespace, var):
#     """ Получить имя пространства, из которого будет взята переменная <var>
#         при запросе из пространства <namespace>, или None, если такого пространства не существует"""
#     if var in scope[namespace]['vars']:
#         return namespace
#     else:
#         try:
#             upper_namespace = scope[namespace]['parent']
#         except KeyError:
#             return None
#         return get(upper_namespace, var)
#
#
# scope = {'global': {'func': [], 'vars': []}}
#
# for _ in range(int(input())):
#     cmd, ns, var = input().split()
#     if cmd == 'create':
#         create(ns, var)
#     elif cmd == 'add':
#         add(ns, var)
#     else:
#         print(get(ns, var))

#######################################################################################################################
# parent = {"global": None}
# vs = {"global": set()}
#
# for cmd, ns, var in [input().split() for i in range(int(input()))]:
#     if cmd == 'create':
#         parent[ns] = var
#         vs[ns] = set()
#     elif cmd == 'add':
#         vs[ns].add(var)
#     else:
#         while ns is not None:
#             if var in vs[ns]:
#                 break
#             ns = parent[ns]
#         print(ns)


1.5 / 8
# '''Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
#   Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые
# можно положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять
# возможность добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет,
# не превышая ее вместимость.
#   При создании копилки, число монет в ней равно 0.
#   Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True'''

# class MoneyBox:
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     def can_add(self, v):
#         return self.capacity >= v
#
#     def add(self, v):
#         if self.can_add(v):
#             self.capacity -= v
#             return True
#         return False
#
# x = MoneyBox(15)
# print(x.add(5))
# # print(x.capacity)
# print(x.add(5))
# # print(x.capacity)
# print(x.add(3))
# # print(x.capacity)
# print(x.add(6))
# # print(x.capacity)

1.5 / 9
# '''Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки
# чисел из этой последовательности, затем сумму второй пятерки, и т. д.
#   Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части.
# Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.
#   Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок
# последовательных элементов по мере их накопления.
#   Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно
# необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.
#   Обратите внимание, что во время выполнения метода add выводить сумму пятерок может потребоваться несколько раз до
# тех пор, пока в буфере не останется менее пяти элементов.'''

# class Buffer:
#     def __init__(self):
#         self.lst = []
#
#     def add(self, *a):
#         for i in a:
#             self.lst.append(i)
#             if len(self.lst) == 5:
#                 print(sum(self.lst))
#                 self.lst = []
#             ##############################
#             # self.lst += a              #
#             # while len(self.l) >= 5:    #
#             #     print(sum(self.l[:5])) #
#             #     del (self.l[:5])       #
#             ##############################
#
#     def get_current_part(self):
#         return self.lst
#
#
# buf = Buffer()
# buf.add(1, 2, 3)
# print(buf.get_current_part())  # вернуть [1, 2, 3]
# buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
# print(buf.get_current_part())  # вернуть [6]
# buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
# print(buf.get_current_part())  # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# print(buf.get_current_part())  # вернуть [1]


1.6 / 7
# '''Вам дано описание наследования классов в следующем формате.
#       <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
#   Это означает, что класс 1 унаследован от класса 2, класса 3, и т. д. Или эквивалентно записи:
#       class Class1(Class2, Class3 ... ClassK):
#       pass
#   Класс A является прямым предком класса B, если B унаследован от A:
#       class B(A):
#           pass
#   Класс A является предком класса B, если
#       A = B;
#       A - прямой предок B
#       существует такой класс C, что C - прямой предок B и A - предок C
#   Например:
#       class B(A):
#           pass
#
#       class C(B):
#           pass
#
#       # A -- предок С
#   Вам необходимо отвечать на запросы, является ли один класс предком другого класса. Важное примечание:
#   Создавать классы не требуется.
#   Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
#       Формат входных данных
#   В первой строке входных данных содержится целое число n - число классов.
#   В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется
# i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется
# сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
#   В следующей строке содержится число q - количество запросов.
#   В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
#   Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
#
#   Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No",
# если не является.'''
#
#
# def isP(pr, ch):
#     return ch == pr or any(map(lambda pl: isP(pr, pl), p[ch]))
# p = {}
# for j in range(2):
#     for c in [input().split() for i in range(int(input()))]:
#         if j:
#             print(['No', 'Yes'][isP(*c)])
#         else:
#             p[c[0]] = c[2:]
################################################
# def search(parent, child):
#     return child == parent or any(map(lambda pl: search(parent, pl), s[child]))
#
# s = {}
# for a in [input().split() for i in range(int(input()))]:
#     s[a[0]] = a[2:]
# print(s)
#
# for b in [input().split() for _ in range(int(input()))]:
#     print(['No', 'Yes'][search(*b)])

1.6 / 8
# ''' Реализуйте структуру данных, представляющую собой расширенную структуру стек. Необходимо поддерживать добавление
# элемента на вершину стека, удаление с вершины стека, и необходимо поддерживать операции сложения, вычитания, умножения
# и целочисленного деления.
#   Операция сложения на стеке определяется следующим образом. Со стека снимается верхний элемент (top1), затем
# снимается следующий верхний элемент (top2), и затем как результат операции сложения на вершину стека
# кладется элемент, равный top1 + top2.
#   Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2) и
# целочисленного деления (top1 // top2).
#   Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list.
#   Требуемая структура класса:
#
#       class ExtendedStack(list):
#           def sum(self):
#               # операция сложения
#
#           def sub(self):
#               # операция вычитания
#
#           def mul(self):
#               # операция умножения
#
#           def div(self):
#               # операция целочисленного деления
#
#   Для добавления элемента на стек используется метод append, а для снятия со стека – метод pop.
#   Гарантируется, что операции будут совершаться только когда в стеке есть хотя бы два элемента.'''
#
# class ExtendedStack(list):
#     def sum(self):
#         self.append(self.pop() + self.pop())
#
#     def sub(self):
#         self.append(self.pop() - self.pop())
#
#     def mul(self):
#         self.append(self.pop() * self.pop())
#
#     def div(self):
#         self.append(self.pop() // self.pop())
#
# ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
# ex_stack.div()
# ex_stack.sub()
# ex_stack.sum()
# ex_stack.mul()

1.6 / 9
# ''' Одно из применений множественного наследование – расширение функциональности класса каким-то заранее определенным
# способом. Например, если нам понадобится логировать какую-то информацию при обращении к методам класса.
#   Рассмотрим класс Loggable:
#       import time
#
# class Loggable: def log(self, msg): print(str(time.ctime()) + ": " + str(msg)) У него есть ровно один метод log,
# который позволяет выводить в лог (в данном случае в stdout) какое-то сообщение, добавляя при этом текущее время.
# Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при добавлении
# элемента в список посредством метода append в лог отправлялось сообщение, состоящее из только что добавленного
# элемента. Ваша программа не должна содержать класс Loggable. При проверке вашей программе будет доступен этот
# класс, и он будет содержать метод log, описанный выше.'''
#
# import time
#
# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))
#
# class LoggableList(list, Loggable):
#     def append(self, elem):
#         # super(LoggableList, self).append(elem)
#         super().append(elem)
#         self.log(elem)
#
# z = LoggableList()
# z.append('Hello!')
# z.append('Good bye!')


2.1 / 6
# ''' Вашей программе будет доступна функция foo, которая может бросать исключения.
#   Вам необходимо написать код, который запускает эту функцию, затем ловит исключения ArithmeticError, AssertionError,
# ZeroDivisionError и выводит имя пойманного исключения.
#   Пример решения, которое вы должны отправить на проверку.
#       try:
#           foo()
#       except Exception:
#           print("Exception")
#       except BaseException:
#           print("BaseException")'''
#
# try:
#     foo()
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ArithmeticError:
#     print("ArithmeticError")
# except AssertionError:
#     print("AssertionError")

2.1 / 7
# ''' Вам дано описание наследования классов исключений в следующем формате.
#       <имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
#   Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.
#   Или эквивалентно записи:
#       class Error1(Error2, Error3 ... ErrorK):
#           pass
#   Антон написал код, который выглядит следующим образом:
#       try:
#          foo()
#       except <имя 1>:
#          print("<имя 1>")
#       except <имя 2>:
#          print("<имя 2>")
#       ...
#   Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, так как ранее в коде
# будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого
# положения и напишите программу, которая будет определять обработку каких исключений можно удалить из кода.
#   Важное примечание:
#   В отличие от предыдущей задачи, типы исключений не созданы.
#   Создавать классы исключений также не требуется
#   Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее
# где-то поймали их предка.
#
#   В первой строке входных данных содержится целое число n - число классов исключений.
#   В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется
# i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется
# сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.
#   В следующей строке содержится число m - количество обрабатываемых исключений.
#   Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
#   Гарантируется, что никакое исключение не обрабатывается дважды.
#
#   Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом
# поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.''
#
#
# def is_parent(child, parent):
#     if child == parent:
#         return True
#     for p in s[child]:
#         if is_parent(p, parent):
#             return True
#     return False
#
#
# s, exceptions = {}, []
# for a in [input().split() for _ in range(int(input()))]:
#     s[a[0]] = a[2:]
# for val in [input() for _ in range(int(input()))]:
#     for i in exceptions:
#         if is_parent(val, i):
#             print(val)
#             break
#     exceptions.append(val)
############################
# def check(src, dest):
#     if src == dest:
#         return True
#     return any([check(child, dest) for child in s[src]])
#
#
# s, used = {a: b[1:] for _ in range(int(input())) for a, *b in [input().split()]}, []
# for val in [input() for _ in range(int(input()))]:
#     if any([check(val, used_one) for used_one in used]):
#         print(val)
#     used.append(val)
############################
# def check_val(d):  #хорошее решение
#     return cls[d] is None or any(map(check_val, cls[d]))
#
#
# cls = {d: set(b[1:]) for _ in range(int(input())) for d, *b in [input().split()]}
# for c in [input() for _ in range(int(input()))]:
#     if check_val(c):
#         print(c)
#     cls[c] = None
############################

2.1 / 9
# ''' Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
#   Также реализуйте новое исключение NonPositiveError.
#   В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить неположительное
# целое число бросалось исключение NonPositiveError и число не добавлялось, а при попытке добавить положительное целое
# число, число добавлялось бы как в стандартный list.
#   В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.'''
#
#
# class NonPositiveError(Exception):
#     pass
#
#
# class PositiveList(list):
#     def append(self, x):
#         if x <= 0:
#             raise NonPositiveError
#         super().append(x)


2.2 / 5
# '''В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день. Во второй строке дано одно
# число days -- число дней. Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты
# date пройдет число дней, равное days. Для решения этой задачи используйте стандартный модуль datetime.
# Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta для прибавления дней к дате.'''
#
# from datetime import date, timedelta
#
# y, m, d = map(int, input().split())
# days = int(input())
# a = date(y, m, d) + timedelta(days)
# print(a.year, a.month, a.day)

2.2 / 9
# '''Алиса владеет интересной информацией, которую хочет заполучить Боб. Алиса умна, поэтому она хранит свою информацию
# в зашифрованном файле. У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.
#   Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой
# из паролей ему нужен. Помогите ему решить эту проблему.
#   Алиса зашифровала свою информацию с помощью библиотеки simple-crypt. Она представила информацию в виде строки, и
# затем записала в бинарный файл результат работы метода simplecrypt.encrypt.
#   Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей
#   служит ключом для расшифровки файла с интересной информацией.
#   Ответом для данной задачи служит расшифрованная интересная информация Алисы. Для того, чтобы считать все данные из
# бинарного файла, можно использовать следующий код:
#     with open("encrypted.bin", "rb") as inp:
#         encrypted = inp.read()
#   Работа с файлами рассмотрена в следующем уроке, поэтому вы можете вернуться к этой задаче после просмотра
# следующего урока.'''
#
#
# from simplecrypt import decrypt, DecryptionException
#
# enc = open("encrypted.bin", "rb").read()
# pw = open("passwords.txt", "r")
# for pas in pw:
#     try:
#         txt = decrypt(pas.strip(), enc).decode('utf8')
#     except DecryptionException:
#         continue
#     print(txt)


2.3 / 4
# '''Одним из самых часто используемых классов в Python является класс filter. Он принимает в конструкторе два аргумента
# a и f – последовательность и функцию, и позволяет проитерироваться только по таким элементам x из
# последовательности a, что f(x) равно True. Будем говорить, что в этом случае функция f допускает элемент x,
# а элемент x является допущенным.
#   В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию, что и
#   стандартный класс filter, но будет использовать не одну функцию, а несколько.
#   Решение о допуске элемента будет приниматься на основании того, сколько функций допускают этот элемент, и сколько не
# допускают. Обозначим эти количества за pos и neg.
#   Введем понятие решающей функции – это функция, которая принимает два аргумента – количества pos и neg, и возвращает
# True, если элемент допущен, и False иначе.
#   Рассмотрим процесс допуска подробнее на следующем примере.
#     a = [1, 2, 3]
#     f2(x) = x % 2 == 0 # возвращает True, если x делится на 2
#     f3(x) = x % 3 == 0
#     judge_any(pos, neg) = pos >= 1 # возвращает True, если хотя бы одна функция допускает элемент
#   В этом примере мы хотим отфильтровать последовательность a и оставить только те элементы, которые делятся на два
# или на три.
#   Функция f2 допускает только элементы, делящиеся на два, а функция f3 допускает только элементы, делящиеся на три.
#   Решающая функция допускает элемент в случае, если он был допущен хотя бы одной из функций f2 или f3, то есть
#   элементы, которые делятся на два или на три.
#   Возьмем первый элемент x = 1.
#     f2(x) равно False, т. е. функция f2 не допускает элемент x.
#     f3(x) также равно False, т. е. функция f3 также не допускает элемент x.
#   В этом случае pos = 0, так как ни одна функция не допускает x, и соответственно neg = 2.
#     judge_any(0, 2) равно False, значит мы не допускаем элемент x = 1.
#   Возьмем второй элемент x = 2.
#     f2(x) равно True
#     f3(x) равно False
#     pos = 1, neg = 1
#     judge_any(1, 1) равно True, значит мы допускаем элемент x = 2.
#   Аналогично для третьего элемента x = 3. Таким образом, получили последовательность допущенных элементов [2, 3].'''
#
#
# class multifilter:
#     def judge_half(pos, neg):
#         return pos >= neg  # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
#
#     def judge_any(pos, neg):
#         return pos >= 1  # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
#
#     def judge_all(pos, neg):
#         return neg == 0  # допускает элемент, если его допускают все функции (neg == 0)
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterable = iterable  # iterable - исходная последовательность
#         self.funcs = funcs  # funcs - допускающие функции
#         self.judge = judge  # judge - решающая функция
#
#     def __iter__(self):
#         for i in self.iterable:  # пробегаемся по каждому элементу списка
#             pos, neg = 0, 0
#             for funcs in self.funcs:  # пробегаемся по каждой функции
#                 if funcs(i):
#                     pos += 1
#                 else:
#                     neg += 1
#             if self.judge(pos, neg):
#                 yield i  # возвращает итератор по результирующей последовательности
#
#
# def mul2(x):
#     return x % 2 == 0
#
#
# def mul3(x):
#     return x % 3 == 0
#
#
# def mul5(x):
#     return x % 5 == 0
#
#
# a = [i for i in range(0, 31, 3)]
# print(list(multifilter(a, mul2, mul3, mul5)))
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))

2.3 / 5
# '''Целое положительное число называется простым, если оно имеет ровно два различных делителя, то есть делится
# только на единицу и на само себя. Например, число 2 является простым, так как делится только на 1 и 2. Также
# простыми являются, например, числа 3, 5, 31, и еще бесконечно много чисел. Число 4, например, не является простым,
# так как имеет три делителя – 1, 2, 4. Также простым не является число 1, так как оно имеет ровно один делитель – 1.
#   Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с 2.'''
#
# import itertools
#
# def is_primes(num):
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for _ in range(3, num // 2, 2):
#         if num % _ == 0:
#             return False
#     return True
#
#
# def primes():
#     num = 2
#     while True:
#         if is_primes(num):
#             yield num
#         num += 1
# print(list(itertools.takewhile(lambda x: x <= 31, primes())))
############################
# import itertools
#
#
# def primes():
#     n = 2
#     while True:
#         if (len([i for i in range(1, n + 1) if n % i == 0])) == 2:
#             yield n
#         n += 1
#
#
# print(list(itertools.takewhile(lambda x: x <= 31, primes())))
############################
# from sympy import isprime
#
#
# def primes():
#     x = 2
#     while True:
#         yield isprime(x)
#         x += 1
#
#
# print(list(itertools.takewhile(lambda x: x <= 31, primes())))
############################
# from itertools import takewhile
#
#
# def primes():
#     k = 2
#     while True:
#         if all(k % i for i in range(2, int(k ** 0.5) + 1)):
#             yield k
#         k += 1
#
#
# print(list(takewhile(lambda x: x <= 31, primes())))


2.4 / 4
# '''Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.'''
#
# with open('dataset_24465_4.txt', 'r') as r, open('new.txt', 'w') as w:
#     w.writelines(reversed(list(r)))
############################
# with open('dataset_24465_4.txt', 'r') as r, open('new.txt', 'w') as w:
#     w.writelines(r.readlines()[::-1])
############################
# with open('dataset_24465_4.txt', 'r') as r, open('new.txt', 'w') as w:
#     for line in reversed(list(r)):
#         w.write(line)

2.4 / 6
# '''Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.
#   Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть
# хотя бы один файл с расширением ".py". Ответом на данную задачу будет являться файл со списком таких директорий,
# отсортированных в лексикографическом порядке. '''
#
# import os.path
#
# with open('unzip.txt', 'w') as u_zip:
#     for current_dir, dirs, files in os.walk('main'):
#         for file in files:
#             if file.endswith(".py"):
#                 u_zip.write(current_dir + '\n')
#                 break
############################
# import os
#
# with open('unzip.txt', 'w') as u_zip:
#     res = sorted([c_dir for c_dir, _, fs in os.walk('main') if any((f.endswith(".py") for f in fs))])
#     u_zip.write('\n'.join(res))
############################
# import zipfile, os
#
# '''без распаковки зип файла, путем добавления только тех путей в котором есть искомый файл.py'''
# with zipfile.ZipFile('main.zip') as zip, open('unzip.txt', 'w') as u_zip:
#     pydirs = {os.path.dirname(path) for path in zip.namelist() if os.path.basename(path).endswith('.py')}
#     u_zip.write('\n'.join(sorted(pydirs)))
# print(type(pydirs))
# for i in pydirs:
#     print(i)


2.5 / 6
# '''Лямбда функции предоставляют нам удобный способ создать функцию «прямо на месте». Но иногда, когда нужно создавать
# много однотипных лямбда функций, еще удобнее будет создать функцию, которая будет их генерировать.
#   Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y, которая
# будет возвращать True, если остаток от деления y на x равен mod, и False иначе.
#   Пример использования:
#     mod_3 = mod_checker(3)
#     print(mod_3(3)) # True
#     print(mod_3(4)) # False
#     mod_3_1 = mod_checker(3, 1)
#     print(mod_3_1(4)) # True'''
#
# mod_checker = lambda x, mod=0: lambda y: y % x == mod


3.1 / 6
# '''Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
#   За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.
#   Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba",
# после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.
#   Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a.
# Если операций потребуется более 1000, выведите Impossible.
#   Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a,
# или Impossible, если операций потребуется более 1000.'''

# Симпатичная задачка и очень простая
# 9 строк через while, replace и счетчик
# спасибо подсказавшим ввод данных через  s, a, b = (input() for _ in range(3))

# s, a, b = (input() for _ in range(3))
# count = 0
# if a not in s:
#     print(0)
# elif a in b:
#     print('Impossible')
# else:
#     while a in s:
#         s = s.replace(a, b)
#         count += 1
#     print(count)
############################
# def counter(s, a, b, count=0):
#     for i in range(1000):
#         if s.find(a) == -1:
#             break
#         s = s.replace(a, b)
#     else:
#         return 'Impossible'
#     return i
#
# s, a, b = (input() for _ in range(3))
# print(counter(s, a, b))
############################
# s, a, b, i = [input() for _ in range(3)] + [0]
# while a in s:
#     if a in b:
#         i = 'Impossible'
#         break
#     s, i = s.replace(a, b), i + 1
# print(i)
############################
# def repl_gen(s, a, b):
#     while a in s: s = s.replace(a, b); yield True
#
#
# s, a, b = (input() for _ in range(3))
# print('Impossible' if a in b and a in s else sum(repl_gen(s, a, b)))

3.1 / 7
# '''Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв. Выведите одно число –
# количество вхождений строки t в строку s.'''

# s, t, i = [input() for _ in range(2)] + [0]
# while t in s:
# #     i = 'Impossible'
# #     break
# # s, i = s.replace(a, b), i + 1
# print(i)
# s, t = (input() for _ in range(2))
# s = 'abababa'
# t = 'aba'
# i = 0
# count = 0
# while t in s:
#     count += 1
#     s = s[i:].find(t)
#     i += 1
#     print(count)
############################
# s, t, count = [input() for _ in range(2)] + [0]
# for i in range(len(s)):
#     if s.find(t, i, i + len(t)) >= 0:
#         count += 1
#
# print(count)
############################
# s, t, count = [input() for _ in range(2)] + [0]
# for i in range(len(s)):
#     if s.startswith(t, i):
#         count += 1
# print(count)
############################
# s, t = [input() for _ in range(2)]
# print((sum(1 for i in range(len(s)) if s.startswith(t, i))))
############################
# import re  # поиск по шаблону
#
# s, t = input(), '(?=' + input() + ')'
# print(len(re.findall(t, s)))


3.2 / 7
# '''Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.'''

# import sys
# import re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r'cat.*cat', line):
#         print(line)

3.2 / 8
# '''Вам дана последовательность строк. Выведите строки, содержащие "cat" в качестве слова.
# Для работы со словами используйте группы символов \b и \B. Описание этих групп вы можете найти в документации.'''
#
# import sys
# import re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r'\bcat\b', line):
#         print(line)

3.2 / 9
# '''Вам дана последовательность строк. Выведите строки, содержащие две буквы "z", между которыми ровно три символа.'''
#
# import sys
# import re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r'z...z', line):
#         print(line)
############################
# import sys, re
# exp = re.compile("z...z")
# print(*filter(lambda line: exp.search(line), sys.stdin), sep='')

3.2 / 10
# '''Вам дана последовательность строк. Выведите строки, содержащие обратный слеш "\".'''
# import sys
# import re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r'\\', line):
#         print(line)

3.2 / 11
# '''Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).'''
#
# import sys
# import re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(r'\b(\w+)\1\b', line):  # "(\b.*\B)\1\b"
#         print(line)

3.2 / 12
# '''Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.'''
#
# import sys
# import re
#
# for line in sys.stdin:
#     line = line.rstrip()
#     line = re.sub(r'human', 'computer', line)
#     print(line)
# ############################
# print(re.sub(r'human', 'computer', sys.stdin.read()), end='')

3.2 / 13
# '''Вам дана последовательность строк. В каждой строке замените первое вхождение слова, состоящего только из латинских
# букв "a" (регистр не важен), на слово "argh".'''
#
# import sys
# import re
#
# for line in sys.stdin:
#     print(re.sub(r'\b[aA]+\b', 'argh', line.strip(), count=1))

3.2 / 14
# '''Вам дана последовательность строк. В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем
# хотя бы из двух букв. Буквой считается символ из группы \w.'''
#
# import sys
# import re
#
# for line in sys.stdin:
#     print(re.sub(r'\b(\w)(\w)', r'\2\1', line.strip()))

3.2 / 15
# '''Вам дана последовательность строк. В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.'''
#
# import sys
# import re
#
# sys.stdout.write(re.sub(r"(\w)\1+", r"\1", sys.stdin.read()))

3.2 / 16
# '''Вам дана последовательность строк. Выведите строки, содержащие двоичную запись числа, кратного 3.
# Двоичной записью числа называется его запись в двоичной системе счисления. Данная задача очень просто может быть решена
# приведением строки к целому числу и проверке остатка от деления на три, но мы все же предлагаем вам решить ее,
# не используя приведение к числу.'''


3.3 / 6
''''''
