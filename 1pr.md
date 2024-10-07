# Практическая работа №1.
## Задача №1
```bash
cut -d: -f1 /etc/passwd | sort
```
![image](https://github.com/user-attachments/assets/9c3027d3-51ae-45ea-a205-f4aabe749700)

## Задача №2
```bash
awk '{print $2, $1}' /etc/protocols | sort -rn | head -5
```
![image](https://github.com/user-attachments/assets/e0c5e715-bf31-4477-b58f-31305a8db4bf)


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

![image](https://github.com/user-attachments/assets/2c236cfb-f8bc-4973-b9b9-39e98903daf3)


## Задача №4
```bash
grep -o '\b[a-zA-Z_][a-zA-Z0-9_]*\b' main.cpp | sort | uniq
```
![image](https://github.com/user-attachments/assets/1b2403e7-7ccf-4005-8352-788086fc16a9)


## Задача №5

```bash
./pr5.sh banner2.sh
```
```bash
chmod +x "$1"
cp "$1" /usr/local/bin/
```
![image](https://github.com/user-attachments/assets/6fdfb880-c964-4fb2-ae50-ba68159217aa)

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
![image](https://github.com/user-attachments/assets/a7933d94-cb11-4771-a9db-fea6efbd84c6)

## Задача №7

```bash
#!/bin/bash
find "$1" -type f -exec md5sum {} + | sort | uniq -w32 -dD
```
![image](https://github.com/user-attachments/assets/050e4faf-5b01-428b-936d-dd422f843a24)

## Задача №8

```bash
#!/bin/bash
find . -name "*.$1" -print0 | tar -czvf archive.tar.gz --null -T -
```

![image](https://github.com/user-attachments/assets/7465ef37-95c8-484b-995e-fc585a31fc82)

![image](https://github.com/user-attachments/assets/4f04d113-9fd7-48ea-a211-3fb85c23349f)

## Задача №9

```bash
#!/bin/bash
sed -e 's/    /\t/g' "$1" > "$2"
```
![image](https://github.com/user-attachments/assets/99582a2e-46c5-4474-b1e0-516f861d10a7)

![image](https://github.com/user-attachments/assets/70e6d3d4-3625-45aa-bd38-f3dc9ffe898e)

![image](https://github.com/user-attachments/assets/860a71b2-38ad-42cc-84eb-20b187c0e1d1)

## Задача №10

```bash
#!/bin/bash
find "$1" -type f -empty -name "*.txt"
```
<img width="546" alt="Снимок экрана 2024-09-08" src="https://github.com/alndis/conf_ex/blob/Practice_1/folder_pr1/10.png">
