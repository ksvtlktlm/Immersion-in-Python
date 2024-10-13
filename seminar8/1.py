"""Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий."""

import os
import json
import csv
import pickle

def get_size(path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                total += os.path.getsize(fp)
            except OSError as e:
                print(f"Ошибка доступа к файлу {fp}: {e}")
    return total

def directory_walker(dir_path):
    results = []

    for root, dirs, files in os.walk(dir_path):
        for name in files:
            full_path = os.path.join(root, name)
            try:
                size = os.path.getsize(full_path)
            except OSError as e:
                print(f"Ошибка доступа к файлу {full_path}: {e}")
                size = None

            results.append({
                "parent_directory": os.path.relpath(root, dir_path),
                "is_file": True,
                "name": name,
                "size_in_bytes": size
            })

        for name in dirs:
            full_path = os.path.join(root, name)
            dir_size = get_size(full_path)
            results.append({
                "parent_directory": os.path.relpath(root, dir_path),
                "is_file": False,
                "name": name,
                "size_in_bytes": dir_size
            })

    try:
        with open("output.json", "w", encoding='utf-8') as json_file:
            json.dump(results, json_file, ensure_ascii=False, indent=4)
    except IOError as e:
        print(f"Ошибка при записи JSON файла: {e}")

    try:
        with open("output.csv", "w", newline='', encoding='utf-8') as csv_file:
            fieldnames = ["parent_directory", "is_file", "name", "size_in_bytes"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)
    except IOError as e:
        print(f"Ошибка при записи CSV файла: {e}")

    try:
        with open("output.pickle", "wb") as pickle_file:
            pickle.dump(results, pickle_file)
    except IOError as e:
        print(f"Ошибка при записи Pickle файла: {e}")

directory_walker("./my_folder")