Файл config.ini - конфигурационный файл 

Файл commands.py - файл с командами

Файл emulator.py - файл создания эмулятора

Файл start_script.txt - файл с начальными командами, которые выполняются при запуске эмулятора

Файл startup.sh - запуск эмулятора через cmd

Файл vfs.py - Файл с настройкой команд

Файл vfs_log.csv - файл с историей команд за последнюю сессию

Запуск системы 
```
sh startup.sh
```

Запуск тестов 
```
$ python -m unittest test_commands

$ python -m unittest test_vfs

```
