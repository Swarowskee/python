#coding=utf-8
числа = []
экспонента = int(input("введите степень: "))
количество_чисел = int(input("количество чисел в списке: "))

for i in range(количество_чисел):
    num = input("число, которое нужно возвести в степень: ")
    числа.append(num)


for num in числа:
    if num.isdigit() or (num.startswith('-') and num[1:].isdigit()):  
        num = float(num)  
        powered_num = num ** экспонента
        print(f"{num} в степени {экспонента} = {powered_num}")
    else:
        print(f"{num} * {экспонента} =", num * экспонента)  
