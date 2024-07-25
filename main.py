import os


def categorize_files_by_type(folder_path):
    files_by_type = {} # словарь для хранения файлов по типам

    if not os.path.exists(folder_path): # Првоерка на действительность пути
        raise AssertionError(f"The folder path '{folder_path}' does not exist.")

    if not os.path.isdir(folder_path): # Проверка на действительность каталога
        raise AssertionError(f"The path '{folder_path}' is not a directory.")


    for item in os.listdir(folder_path): # Обход всех элементов в текущей директории
        item_path = os.path.join(folder_path, item)

        if os.path.isdir(item_path):   # Если элемент - каталог, рекурсивно обрабатываем её:
            subfiles = categorize_files_by_type(item_path)
            for extensions, files in subfiles.items(): # Объединение файлов по типам
                if extensions in files_by_type:
                    files_by_type[extensions].extend(files)
                else:
                    files_by_type[extensions] = files
        else:
            # Если элемент - файл, получаем его расширение игнорируя первую часть (название файла)
            _, extensions = os.path.splitext(item)
            extensions = extensions[1:]  # Убираем точку из расширения

            if extensions == '':
                extensions = ''  # Обработка файлов без расширения

            if extensions in files_by_type: # Добавление файла в словарь по его расширению
                files_by_type[extensions].append(item_path)
            else:
                files_by_type[extensions] = [item_path]

    return files_by_type


folder_path = "C:\\Users\\user\\Documents\\Adobe"

try: # Ловим ошибки в теле try и отдаем их except
    files_by_type = categorize_files_by_type(folder_path)
    for ext, files in files_by_type.items():
        print(f"Extension: {ext if ext else 'No extension'}")
        for file in files:
            print(f" - {file}")
except Exception as e:
    print(f"Error: {e}")
