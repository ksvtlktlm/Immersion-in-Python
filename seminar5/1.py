"""Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла."""

def split_file_path(path):
    directory = '\\'.join(path.split('\\')[:-1])
    file_name = path.split("\\")[-1].split(".")[-2]
    file_extension = path.split("\\")[-1].split(".")[-1]
    return directory, file_name, file_extension

path = input()
directory, name, extension = split_file_path(path)
print(f'Директория: {directory}')
print(f'Имя файла: {name}')
print(f'Расширение файла: {extension}')