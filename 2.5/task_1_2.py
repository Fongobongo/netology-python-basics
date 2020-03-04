from contextlib import contextmanager as cm
from datetime import datetime as dt


@cm
def my_open(file_path):
    try:
        start_time = dt.now()
        print(f"Время открытия файла: {start_time}")
        file = open(file_path)
        yield file
    finally:
        file.close()
        end_time = dt.now()
        print(f"Время закрытия файла: {end_time}")
        print(f"Время, затраченное на чтения файла: {end_time - start_time}")


with my_open("10TBfile.txt") as f:
    content = f.read()
