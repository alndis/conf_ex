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
Создадим файл md.dot и ed.dot с указанием зависимостей между библиотеками
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
 ```bash
$ dot -Tpng md.dot -o matplotlib_dependencies.png
```
![matplotlib_dependencies](https://github.com/user-attachments/assets/15cea608-bae9-48fb-8000-d300fe03473d)

 Генерация графика для express
 ```bash
$ dot -Tpng ed.dot -o express_dependencies.png
```
![express_dependencies](https://github.com/user-attachments/assets/cfebff75-21c5-4c6b-9541-b9d105fe2ef6)
# Задание №4
```bash
include "alldifferent.mzn";

var 1..9: d1;  
var 0..9: d2; 
var 0..9: d3; 
var 0..9: d4; 
var 0..9: d5;  
var 0..9: d6; 

constraint alldifferent([d1, d2, d3, d4, d5, d6]);

constraint d1 + d2 + d3 = d4 + d5 + d6;

solve minimize d1 + d2 + d3; 
```
![image](https://github.com/user-attachments/assets/1fa59667-fffd-4374-a629-8467fb04d00c)
