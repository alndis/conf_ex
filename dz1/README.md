# Эмулятор оболочки ОС

Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС. Эмулятор должен запускаться из реальной командной строки, а файл с виртуальной файловой системой не нужно распаковывать у пользователя. Эмулятор принимает образ виртуальной файловой системы в виде файла формата zip. Эмулятор должен работать в режиме CLI.


## Особенности

Конфигурационный файл имеет формат ini и содержит:
- Путь к архиву виртуальной файловой системы.
- Путь к лог-файлу.
- Путь к стартовому скрипту.
  
Лог-файл имеет формат csv и содержит все действия во время последнего
сеанса работы с эмулятором.

Стартовый скрипт служит для начального выполнения заданного списка
команд из файла.

Необходимо поддержать в эмуляторе команды ls, cd и exit, а также
следующие команды:
1. uname.
2. rmdir.

## Использование

Чтобы запустить эмулятор, выполните следующую команду в терминале:

```bash
python emulator.py
```

## Файл конфигурации

![image](https://github.com/user-attachments/assets/ca7e4a7e-1213-4c7a-b33e-e61067cc040a)

## Для запуска теста используйте 

Тест комманд:

```bash
python -m unittest test_commands.py 
```

Тест эмулятора:

```bash
python -m unittest test_vfs.py 
```
