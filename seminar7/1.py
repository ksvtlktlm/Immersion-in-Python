"""Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6]
берутся буквы с 3 по 6 из исходного имени файла.
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение."""

import os


__all__ = ['group_renaming']

def group_renaming(new_name, digits, source_extension, final_extension, range_name, path='.'):
    counter = 1
    for filename in os.listdir(path):
        if filename.endswith(source_extension):
            old_name = os.path.splitext(filename)[0]
            old_name_substring = old_name[range_name[0]:range_name[1]] if range_name else ""
            new_filename = f"{old_name_substring}{new_name}{str(counter).zfill(digits)}{final_extension}"
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
            counter += 1



group_renaming('new_file', 3, '.txt', '.md', [1, 3], './my_folder')