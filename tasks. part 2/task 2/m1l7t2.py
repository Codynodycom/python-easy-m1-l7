'''
Задача 2

Исправь ошибки в коде

Бо после того как удалил файлы с вирусами, решил что нужно предотвратить их следующее появление, он написал программу, которая проверяет, какой файл пытаются загрузить в систему. Бо сделал пару ошибок в коде, найди их и исправь.

'''

files = "data_1.ini data_2.json data_3.txt data_4.db data_6.txt"

file = input("Какой файл вы хотите загрузить? ")

banned_files = "virus.exe virus.bat trojan.bat trojan.exe"

    if file ==  "virus.exe":
        print("Файл virus.exe был заблокирован!")

elif file == "virus.bat"
        print("Файл virus.bat был заблокирован!")

else if file == "trojan.bat":
    print("Файл trojan.bat был заблокирован!")

else file == "trojan.exe"
    print("Файл trojan.exe был заблокирован!")

else:
    print("Файл успешно загружен!")

