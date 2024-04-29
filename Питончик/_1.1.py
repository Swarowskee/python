#coding=utf-8
while True:
    user_input = input("введите число или 'exit' для выхода: ")
    
    if user_input.lower() == 'exit':
        print("выход из программы.")
        break
    
    if not user_input.isdigit():
        print("ошибка: введено не число.")
        continue
    
    number_length = len(user_input)
    print(f"длина числа: {number_length}")
