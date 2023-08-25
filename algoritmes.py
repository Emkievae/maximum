# анализ сложности алгоритмов

# счетчик уникальных символов в строке
# на вход ф-ции подается строка. И ф-ция считает сколько раз в строке встретился каждый из символов

import time

# создаем ф-цию для подсчета уникальных символов
def count_sym(line):
    for sym in line:
        count = 0
        for sub_sym in line:
            if sym == sub_sym:
                count += 1
        print(sym, count)

def count_sym1(line):
    for sym in set(line):
        count = 0
        for sub_sym in line:
            if sym == sub_sym:
                count += 1
        print(sym, count)

start = time.time()
count_sym1('abcdefgh' * 100000)
end = time.time()
time_work = end - start
print(time_work)