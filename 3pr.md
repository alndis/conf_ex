# Задача №1
Первым делом установим Jsonnet с помощью команды, приведенной ниже
```bash
pacman -S mingw-w64-x86_64-python-jsonnet
```
Далее создадим файл Ex1.jsonnet, запишем в него код из задания. Далее скомпилируем этот файл в Json.
```bash
jsonnet Ex1.jsonnet -o Ex1jn.json
```
Содержимое файла json (Ex1jn.json)
![image](https://github.com/user-attachments/assets/b141e4b1-ae51-45cf-addd-b8fa001d9416)

# Задание №2
Установим dhall
```bash

```
Создадим файл Ex2.dhall, запишем в него код из задания. Скомпилируем файл в Json
```bash

```
Слдержимое файла json (Exjn.json)

# Задание №3
Создадим файл Ex3.py и реализуем в нем грамматику языка нулей и единиц
```bash
import random

def parse_bnf(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start):
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join(generate_phrase(grammar, name) for name in seq)
    return str(start)

BNF = """
E = S1 | S2 
S1 = "0"
S2 = "1"
"""

for i in range(10):
    phrase = generate_phrase(parse_bnf(BNF), 'E')
    if phrase:
        print(phrase.replace('"', ''))

```
Результат запуска:
![image](https://github.com/user-attachments/assets/41050778-b0c9-4f5e-a277-48ba0fb9c5dc)
# Задание №4
```bash
import random

def parse_bnf(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start, max_depth=10, current_depth=0):
    if current_depth > max_depth:
        return ""
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join(generate_phrase(grammar, name, max_depth, current_depth + 1) for name in seq)
    return str(start)

BNF = """
E = P E | F E | P | F 
P = "(" P ")" | "(" ")" 
F = "{" F "}" | "{}"
"""

for i in range(10):
    phrase = generate_phrase(parse_bnf(BNF), 'E')
    if phrase:
        print(phrase.replace('"', ''))
```
Результат выполнения
![image](https://github.com/user-attachments/assets/df30775b-76a0-4d9f-b272-310267c81c5f)

# Задание №5
```bash
import random

def parse_bnf(text):
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar

def generate_phrase(grammar, start, max_depth=10, current_depth=0):
    if current_depth > max_depth:
        return ""
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join(generate_phrase(grammar, name, max_depth, current_depth + 1) for name in seq)
    return str(start)

BNF = """
E = L | E & L | E | E | E
L = x | y | "(" E ")" | "~" L | "(" E ")" | "~" L
"""

def format_phrase(phrase):
    output = []
    prev_char = None
    open_count = 0

    for char in phrase:
        if char in ['x', 'y']:
            if prev_char in ['x', 'y']:
                continue
            output.append(char)
        elif char in ['&', '|']:
            if len(output) < 2 or output[-1] in ['&', '|'] or (prev_char in ['(', ')']):
                continue
            output.append(char)
        elif char == '(':
            if prev_char == '(':
                continue
            output.append(char)
            open_count += 1
        elif char == ')':
            if output and output[-1] == '(':
                output.pop()
                open_count -= 1
                continue
            if open_count > 0:
                output.append(char)
                open_count -= 1

        prev_char = char

    output = [c for c in output if not (c == '(' and (prev_char == '(' or (len(output) > 1 and output[-2] == '(')))]

    return ''.join(output)

for i in range(10):
    phrase = generate_phrase(parse_bnf(BNF), 'E')
    if phrase:
        formatted_phrase = format_phrase(phrase)
        if formatted_phrase:
            print(formatted_phrase.replace('"', ''))
```
Результат:
![image](https://github.com/user-attachments/assets/ecd5a849-89b1-4e0f-b561-0b4300ba501d)

