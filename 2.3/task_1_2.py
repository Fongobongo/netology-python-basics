user_input = input("Введите польскую нотацию для двух положительных чисел: ").split()

operations = ['+', '-', '*', '/']


class NotANumberError(Exception):
    def __repr__(self):
        return print("По крайней мере одно из введённых значений не является положительным числом.")


def calculation(list_of_3):

    try:

        operation = user_input[0]
        number_1 = user_input[1].replace(".", "", 1)
        number_2 = user_input[2].replace(".", "", 1)

        assert operation in operations
        if number_1.isdigit() & number_2.isdigit():
            result = eval(number_1 + operation + number_2)
            return print(f"Ответ: {number_1} {operation} {number_2} = {result}.")
        else:
            raise NotANumberError
    except IndexError:
        return print("Число введённых элементов меньше трёх.")
    except AssertionError:
        return print(f"Операция '{operation}' не поддерживается.")
    except ZeroDivisionError:
        return print("На 0 делить нельзя. Не в мою смену.")
    except NotANumberError:
        return print("По крайней мере одно из введённых значений не является положительным числом.")


calculation(user_input)
