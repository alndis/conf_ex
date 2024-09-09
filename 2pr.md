# Задание №1
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
```bash
pip show matplotlib
```
![image](https://github.com/user-attachments/assets/1b2a1de6-0872-46bf-a26e-f80d3930fdd3)
Один из способов, чтобы получить пакет без менеджера пакетов, это клонировать репозиторий во временную директорию, а затем установить пакет из этой директории, затем использовать код python setup.py install

# Задание №2
```bash
npm show express
```
![image](https://github.com/user-attachments/assets/818bdea8-17c2-4245-aa2c-c70d3d6bb77e)

# Задание №3
Создадим файл md.dot ed.dot с указанием зависимостей между библиотеками
```bash
digraph G {
    rankdir=LR;
    node [shape=ellipse, style=filled, color=lightblue];

    "matplotlib" -> "numpy";
    "matplotlib" -> "pillow";
    "matplotlib" -> "cycler";
    "matplotlib" -> "kiwisolver";
    "matplotlib" -> "pyparsing";
    "matplotlib" -> "python-dateutil";
}
```

```bash
digraph G {
    rankdir=LR;
    node [shape=ellipse, style=filled, color=lightgreen];

    "express" -> "accepts";
    "express" -> "array-flatten";
    "express" -> "body-parser";
    "express" -> "content-disposition";
    "express" -> "cookie";
    "express" -> "cookie-signature";
    "express" -> "debug";
    "express" -> "depd";
    "express" -> "encodeurl";
    "express" -> "escape-html";
    "express" -> "etag";
    "express" -> "finalhandler";
    "express" -> "fresh";
    "express" -> "merge-descriptors";
    "express" -> "methods";
    "express" -> "on-finished";
    "express" -> "parseurl";
    "express" -> "path-to-regexp";
    "express" -> "proxy-addr";
    "express" -> "qs";
    "express" -> "range-parser";
    "express" -> "safe-buffer";
    "express" -> "send";
    "express" -> "serve-static";
    "express" -> "setprototypeof";
    "express" -> "statuses";
    "express" -> "type-is";
    "express" -> "utils-merge";
    "express" -> "vary";
}
```
 Генерация графика для matplotlib
