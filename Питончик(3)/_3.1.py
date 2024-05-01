class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("аргументы должны быть числами")
        if y == 0:
            raise ValueError("деление на ноль недопустимо")
        return x / y

    def power(self, x, y):
        return x ** y


def main():
    calc = Calculator()
    while True:
        print("выберите операцию:")
        print("1. сложение")
        print("2. вычитание")
        print("3. умножение")
        print("4. деление")
        print("5. возведение в степень")
        print("6. выход")

        choice = input("введите номер операции: ")

        if choice in ['1', '2', '3', '4', '5']:
            try:
                x = float(input("введите первое число: "))
                y = float(input("введите второе число: "))
            except ValueError:
                print("ошибка: введены некорректные данные.")
                continue

        if choice == '1':
            result = calc.add(x, y)
        elif choice == '2':
            result = calc.subtract(x, y)
        elif choice == '3':
            result = calc.multiply(x, y)
        elif choice == '4':
            try:
                result = calc.divide(x, y)
            except (ValueError, TypeError) as e:
                print(e)
                continue
        elif choice == '5':
            result = calc.power(x, y)
        elif choice == '6':
            print("программа завершена.")
            break
        else:
            print("некорректный выбор операции.")
            continue

        print("результат: ", result)


if __name__ == "__main__":
    main()
