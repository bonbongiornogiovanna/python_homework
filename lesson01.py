# 1.

name = input('Введите Ваше имя: ')
age = int(input('Введите Ваш возраст: '))

print('Вас зовут %s' % name)
print('Вам %d лет' % age)

print(type(age))

# 2.

secs = int(input('Введите время в секундах: '))

secs = secs % (24 * 3600)
hours = secs // 3600
secs %= 3600
mins = secs // 60
secs %= 60

res = '{:02}:{:02}:{:02}'.format(hours, mins, secs)
print(res)

# 3.

n = input('Введите число: ')

print(int(n) + int(n*2) + int(n*3))

# 4.1 Возможно, не до конца понял задание, но решил показать использование цикла while,
# условий и математических операторов. Как получить максимальное число без того,
# чтобы использовать списки не смог придумать.

#
num = int(input('Введите целое положительное число: '))
num_list = []

while num > 0:
    last_0 = num % 10
    num //= 10
    last_1 = num % 10
    if last_0 > last_1:
        num_list.append(last_0)
    else:
        num_list.append(last_1)
print(max(num_list))

# 4.2 Вариант покороче, но без тренировки операторов и циклов

print(max(list(input('Введите целое положительное число: '))))

# 5, 6

rev = int(input('Введите значение выручки организации: '))
cost = int(input('Введите значение издержек организации: '))
profit = (rev - cost)
profitability = (profit / rev)

if rev > cost:
    print('Поздравляем, у Вас имеется прибыль!')
    print('Ваша рентабельность по выручке составила {:%}' .format(profitability))
    empl = int(input('Введите численность сотрудников Вашей организации: '))
    print('Прибыль организации в расчете на одного сотрудника составила', round((profit / empl), 2))
elif rev == cost:
    print('Неплохо, Вы работаете без убытка, но жаль, что нет прибыли.')
else:
    print('Пора заняться оптимизацией, у Вас убыток!')

# 7.

a = int(input('Введите количество километров в первый день (a): '))
b = int(input('Введите целевое количество километров (b): '))
day = 0

while a < b:
    a *= 1.1
    day += 1
print(day + 1)
