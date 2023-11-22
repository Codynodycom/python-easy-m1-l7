'''
Задача 1

Исправь ошибки в коде

После утечек данных, Бо пришлось написать новую программу для входа в аккаунт на сайте академии, Бо очень торопился с написанием, поэтому в программе оччень много ошибок.

Помоги Бо исправить ошибки в коде программы.

'''

right_login = "bo_accaunt"
right_password = "4_Ds2eKa"

login = input("Введите свой логин: ")
password = input("Введите свой пароль: ")

if login != right_login:

print("Логин неверный!")

else password != right_password;    print("Пароль неверный!")

elif login != right_login and password != right_password:
    print("Ваш пароль и логен неверны!")
else login == right_login and right_password == password:
print("Вы вошли в аккаунт академии!")

