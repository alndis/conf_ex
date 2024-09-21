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
# Задание №5
```bash
% Use this editor as a MiniZinc scratch book
set of int: MenuVersions = 1..6;
set of int: DropdownVersions = 1..5;
set of int: IconVersions = 1..2;

array[MenuVersions] of int: menu = [150, 140, 130, 120, 110, 100];
array[DropdownVersions] of int: dropdown = [230, 220, 210, 200, 180];
array[IconVersions] of int: icons = [200, 100];

var MenuVersions: selected_menu;
var DropdownVersions: selected_dropdown;
var IconVersions: selected_icons;

constraint
    (selected_menu = 1 -> selected_dropdown in 1..3) /\
    (selected_menu = 2 -> selected_dropdown in 2..4) /\
    (selected_menu = 3 -> selected_dropdown in 3..5) /\
    (selected_menu = 4 -> selected_dropdown in 4..5) /\
    (selected_menu = 5 -> selected_dropdown = 5) /\
    (selected_dropdown = 1 -> selected_icons = 1) /\
    (selected_dropdown = 2 -> selected_icons in 1..2) /\
    (selected_dropdown = 3 -> selected_icons in 1..2) /\
    (selected_dropdown = 4 -> selected_icons in 1..2) /\
    (selected_dropdown = 5 -> selected_icons in 1..2);

solve satisfy;

output [
    "Selected menu version: \(menu[selected_menu])\n",
    "Selected dropdown version: \(dropdown[selected_dropdown])\n",
    "Selected icon version: \(icons[selected_icons])\n"
];
```
![image](https://github.com/user-attachments/assets/3ee0fac7-4870-4666-8615-7ee1be3d71eb)

# Задание №6
```bash
include "alldifferent.mzn";

% Пакеты и их версии
var 1..1: root_version;  % версия пакета root
var 1..2: foo_version;  % версия пакета foo
var 1..2: left_version;  % версия пакета left
var 1..2: right_version;  % версия пакета right
var 1..2: shared_version;  % версия пакета shared
var 1..2: target_version;  % версия пакета target

% Зависимости между пакетами
constraint (root_version == 1) -> (foo_version == 1 \/ foo_version == 2);
constraint (root_version == 1) -> (target_version == 2);
constraint (foo_version == 2) -> (left_version == 1);
constraint (foo_version == 2) -> (right_version == 1);
constraint (left_version == 1) -> (shared_version == 1 \/ shared_version == 2);
constraint (right_version == 1) -> (shared_version == 1);
constraint (shared_version == 1) -> (target_version == 1 \/ target_version == 2);

% Решение
solve satisfy;
```
![image](https://github.com/user-attachments/assets/495f307d-1b5a-40fd-9ff1-7c93bb7dfdab)

# Задание №7
```bash
int: num_packages;

set of int: Packages = 1..num_packages;

array[Packages] of set of int: Versions;

array[Packages] of var int: selected_version;

array[Packages] of set of int: dependencies;

array[Packages, Packages] of int: min_version;

array[Packages, Packages] of int: max_version;

constraint
  forall(i in Packages) (
    forall(dep in dependencies[i]) (
      selected_version[dep] >= min_version[i, dep] /\
      selected_version[dep] <= max_version[i, dep]
    )
  );

solve satisfy;
```
