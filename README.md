# 6_password_strength

Скрипт для проверки вашего пароля на сложность. Оценивает по следующим параметрам:

* наличие букв из верхнего регистра +1
* наличие букв из нижнего регистра  +1
* наличие цифр +1
* наличие знаков пунктуации +1
* длина пароля от 4 до 7 знаков +1
* длина пароля от 8 до 13 +2
* длина пароля от 14 до 19 +3
* длина пароля от 20 и бесконечность +4

# Установка

```sh
git clone https://github.com/romanyakovlev/6_password_strength
```
Скачайте любой файл, содержащий самые ненадежные пароли, например из [этого](https://github.com/danielmiessler/SecLists/tree/master/Passwords) репозитория

Запускаем скрипт

```sh
python3 password_strength.py your_pass black_list_file_name
```

где your_pass - строка из твоего пароля , black_list_file_name - название файла, содержащего ненадежные пароли.
