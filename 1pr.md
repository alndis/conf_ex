# Практическая работа №1.
## Задача №1
```bash
cut -d: -f1 /etc/passwd | sort
```
<img width="535" height="600" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/1.jpg">

## Задача №2
```bash
awk '{print $2, $1}' /etc/protocols | sort -rn | head -5
```
<img width="649" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/2.jpg">

## Задача №3

```bash
line = input()
len = len(line)
print("+--", end='')
for i in range(0, len-1):
    print('-', end='')
print('--+')
print(f'|  {line}  |')
print("+--", end='')
for i in range(0, len-1):
    print('-', end='')
print('--+')
```

<img width="546" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/3.png">

## Задача №4
```bash
grep -o '\b[a-zA-Z_][a-zA-Z0-9_]*\b' main.cpp | sort | uniq
```
<img width="546" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/4.png">


## Задача №5

```bash
./pr5.sh banner2.sh
```
```bash
chmod +x "$1"
cp "$1" /usr/local/bin/
```
<img width="546" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/5.png">
## Задача №6

```bash
import os

def check_comment(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline().strip()
        if first_line.startswith(("//", "/*", "#")):
            return True
        else:
            return False

def main():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith((".c", ".js", ".py")):
                file_path = os.path.join(root, file)
                if check_comment(file_path):
                    print(f"Comment found in {file_path}")
                else:
                    print(f"No comment found in {file_path}")

if __name__ == "__main__":
    main()
```
<img width="546" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/6.png">
## Задача №7

```bash
#!/bin/bash
find "$1" -type f -exec md5sum {} + | sort | uniq -w32 -dD
```
<img width="546" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/7.png">
## Задача №8

```bash
#!/bin/bash
find . -name "*.$1" -print0 | tar -czvf archive.tar.gz --null -T -
```
<img width="546" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/8.1.png">
<img width="546" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/8.2.png">
## Задача №9

```bash
#!/bin/bash
sed -e 's/    /\t/g' "$1" > "$2"
```
<img width="546" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/9.1.png">
<img width="546" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/9.2.png">
<img width="546" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/9.3.png">
## Задача №10

```bash
#!/bin/bash
find "$1" -type f -empty -name "*.txt"
```
<img width="546" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/10.png">
