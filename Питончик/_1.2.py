#coding=utf-8
number = int(input("введите число: "))

print("числа в интервале [-{}, {}]:".format(number, number + 1))
for i in range(-number, number + 2):
    print(i)
sum_negative = 0
sum_positive = 0
for i in range(-number, number + 2):
    if i < 0:
        sum_negative += i
    elif i > 0:
        sum_positive += i
print("сумма отрицательных чисел:", sum_negative)
print("сумма положительных чисел:", sum_positive)
