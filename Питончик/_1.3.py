#coding=utf-8
while True:
    user_input = input("введите трехзначное число: ")
    
    if user_input.lower() == 'exit':
        print("выход из программы.")
        break
    
    if not user_input.isdigit() or len(user_input) != 3:
        print("ошибка: Введено не трехзначное число.")
        continue
    if len(set(user_input)) != 3:
        print("ошибка: число должно состоять из различных цифр.")
        continue
    permutations = [user_input[0] + user_input[1] + user_input[2],
                    user_input[0] + user_input[2] + user_input[1],
                    user_input[1] + user_input[0] + user_input[2],
                    user_input[1] + user_input[2] + user_input[0],
                    user_input[2] + user_input[0] + user_input[1],
                    user_input[2] + user_input[1] + user_input[0]]
    
    print("перестановки числа:")
    for perm in permutations:
        print(perm)
