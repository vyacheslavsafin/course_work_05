# Курсовой проект №5
## Работа с базами данных

### Описание работы программы:

В файле ```main.py``` есть словарь ```companies```, в котором записаны 10 выбранных с сайта https://hh.ru компаний, в формате
```ID компании: Название компании```
Данные в словаре можно заменить своими. В дальнейшем будет производиться сортировка и фильтрация вакансий из этого словаря.
В процессе работы программа выполняет следующие действия:
* получает данные с сайта по API
* создает базу данных Postgres
* создает две таблицы и заполняет их

Так же в классе DBManager есть следующие методы:
* получение списка всех компаний и количества вакансий у каждой компании.
* получение списка всех вакансий с указанием названия компании, названия вакансии, зарплаты и ссылки на вакансию.
* получение средней зарплаты по вакансиям.
* получение списка всех вакансий, у которых зарплата выше средней по всем вакансиям.
* получение списка всех вакансий, в названии которых содержатся переданные в метод слова, например Python, Разработчик.


###  Как использовать:
1. Выполнить clone репозитория
2. Активировать виртуальное окружение и установить зависимости ```  pip install -r requirements.txt```
3. Добавить в файл database.ini данные для подключения к базе данных в формате:
```ini
[postgresql]
host=localhost
user=имя_пользователя
password=пароль
port=5432
```
4. Запустить main.py из корня проекта

### Критерии оценивания:
1. Проект выложен на GitHub.
2. Оформлен файл README.md с информацией, о чем проект, как его запустить и как с ним работать.
3. Есть Python-модуль для создания и заполнения данными таблиц БД.