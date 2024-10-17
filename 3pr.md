# Задача №1
Первым делом установим Jsonnet с помощью команды, приведенной ниже
```bash
pacman -S mingw-w64-x86_64-python-jsonnet
```
Далее создадим файл Ex1.jsonnet, запишем в него код из задания. Далее скомпилируем этот файл в Json.
```bash
jsonnet Ex1.jsonnet -o Ex1jn.json
```

```
local Group(digits) = 'ИКБО-' + digits;

local groups = [
  Group(i + '-20')
  for i in std.range(1, 24)
] + [
  Group('10-23'),
];

local Student(age, groupId, name) = {
  age: age,
  group: groups[groupId],
  name: name,
};

{
  groups: groups,
  students: [
    Student(19, 3, 'Иванов И.И.'),
    Student(18, 4, 'Петров П.П.'),
    Student(18, 4, 'Сидоров С.С.'),
    Student(19, std.length(groups) - 1, 'Бузин Б.А.'),
  ],
  subject: 'Конфигурационное управление',
}
```
Содержимое файла json (Ex1jn.json)

![image](https://github.com/user-attachments/assets/b141e4b1-ae51-45cf-addd-b8fa001d9416)

# Задание №2
Установим dhall
```
![image](https://github.com/user-attachments/assets/706e2eb4-d0cf-4e45-a100-6dec459ddf38)

```
Создадим файл Ex2.dhall, запишем в него код из задания. Скомпилируем файл в Json
```bash
dhall --output json --file Pr32.dhall > Pr3_2d.json
```

```
let List/map =
      https://prelude.dhall-lang.org/v23.0.0/List/map

let List/drop =
      https://prelude.dhall-lang.org/v23.0.0/List/drop

let List/index =
      https://prelude.dhall-lang.org/v23.0.0/List/index

let Natural/enumerate =
      https://prelude.dhall-lang.org/v23.0.0/Natural/enumerate

let Range =
      \(n : Natural) ->
      \(m : Natural) ->
        List/drop n Natural (Natural/enumerate (m + 1))

let Group = \(n : Text) -> "ИКБО-" ++ n

let groups =
        List/map
          Natural
          Text
          (\(i : Natural) -> Group (Natural/show i ++ "-20"))
          (Range 1 24)
      # [ Group "10-23" ]

let Student =
      \(age : Natural) ->
      \(groupId : Natural) ->
      \(name : Text) ->
        { age, group = List/index groupId Text groups, name }

in  { groups
    , students =
      [ Student 19 3 "Иванов И.И."
      , Student 18 4 "Петров П.П."
      , Student 18 4 "Сидоров С.С."
      , Student 19 (Natural/subtract 1 (List/length Text groups)) "Бузин Б.А."
      ]
    }
```

Содержимое файла json (Pe2_2.json)

![image](https://github.com/user-attachments/assets/9dda3ea5-8964-4375-8d6d-77ac3e7227ef)

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
Результат выполнения:

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

![image](https://github.com/user-attachments/assets/b91ce96a-1dc5-4dbe-84ef-eb95832f5d6f)


