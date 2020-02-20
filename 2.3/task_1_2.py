user_input = input("Введите польскую нотацию для двух положительных чисел: ").split()

operations = ['+', '-', '*', '/']


def calculation(list_of_3):
    try:
        try:
            assert len(user_input) == 3
        except AssertionError:
            return print("Число введённых элементов не равно трём.")

        try:
            assert user_input[0] in operations
        except AssertionError:
            return print(f"Операция '{user_input[0]}' не поддерживается.")

        try:
            assert user_input[1].replace(".", "", 1).isdigit() & user_input[2].replace(".", "", 1).isdigit()
        except AssertionError:
            return print("По крайней мере одно из введённых значений не является положительным числом.")

        return print(f"Ответ: {eval(user_input[1] + user_input[0] + user_input[2])}.")

    except ZeroDivisionError:
        return print("На 0 делить нельзя. Не в мою смену.")


calculation(user_input)
