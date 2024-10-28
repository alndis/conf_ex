## Задание 0

Изучить основы языка утилиты make. Распаковать в созданный каталог make.zip, если у вас в в системе нет make.

Создать приведенный ниже Makefile и проверить его работоспособность.

![image](https://github.com/user-attachments/assets/ce081927-1ee4-488d-bcd0-27fdb0eef9fe)

## Визуализировать граф civgraph.txt.

Скрипт на Python:

```py
from graphviz import Source

file_path = 'civgraph.txt'

with open(file_path, 'r') as f:
    dot_data = f.read()

src = Source(dot_data)
src.render('civgraph', format='png')
```

Файл Makefile:

```bash
run:
        python3 gr0.py
```

![image](https://github.com/user-attachments/assets/c29f7b5b-74e4-47fd-b6b4-2aecd0b045c4)

![image](https://github.com/user-attachments/assets/83300fb3-9f61-43be-8ac0-a104bd4720bc)

## Задание 1

Файл gr1.py:

```py
import json

def generate_makefile(graph):
    with open('Makefile', 'w') as f:
        for target, deps in graph.items():
            deps_str = ' '.join(deps)
            f.write(f'{target}: {deps_str}\n')
            f.write(f'\t@echo "Building {target}"\n\n')

if __name__ == '__main__':
    with open('civgraph.json') as file:
        graph = json.load(file)
    generate_makefile(graph)
    print("Makefile создан.")
```
Файл civgraph.json:
```json
{"pottery": [], "irrigation": ["pottery"], "writing": ["pottery"], "animal_husbandry": [], "archery": ["animal_husbandry"], "mining": [], "masonry": ["mining"], "bronze_working": ["mining"], "the_wheel": ["mining"], "apprenticeship": ["mining", "currency", "horseback_riding"], "sailing": [], "celestial_navigation": ["sailing", "astrology"], "shipbuilding": ["sailing"], "astrology": [], "drama_poetry": ["astrology", "irrigation", "masonry", "early_empire", "mysticism"], "theology": ["astrology", "mysticism", "drama_poetry"], "horseback_riding": ["archery"], "machinery": ["archery", "iron_working", "engineering"], "currency": ["writing", "foreign_trade"], "state_workforce": ["writing", "bronze_working", "craftsmanship"], "recorded_history": ["writing", "political_philosophy", "drama_poetry"], "construction": ["masonry", "the_wheel", "horseback_riding"], "engineering": ["masonry", "the_wheel"], "iron_working": ["bronze_working"], "mathematics": ["bronze_working", "celestial_navigation", "currency", "drama_poetry"], "military_training": ["bronze_working", "military_tradition", "games_recreation"], "cartography": ["celestial_navigation", "shipbuilding"], "medieval_faires": ["currency", "feudalism"], "guilds": ["currency", "feudalism", "civil_service"], "mercantilism": ["currency", "humanism"], "stirrups": ["horseback_riding", "feudalism"], "mass_production": ["shipbuilding", "machinery", "education"], "naval_tradition": ["shipbuilding", "defensive_tactics"], "military_tactics": ["mathematics"], "education": ["mathematics", "apprenticeship"], "military_engineering": ["construction", "engineering"], "castles": ["construction", "divine_right", "exploration"], "games_recreation": ["construction", "state_workforce"], "gunpowder": ["apprenticeship", "stirrups", "military_engineering"], "printing": ["machinery", "education"], "metal_casting": ["machinery", "gunpowder"], "banking": ["education", "stirrups", "guilds"], "astronomy": ["education"], "military_science": ["stirrups", "printing", "siege_tactics"], "siege_tactics": ["castles", "metal_casting"], "square_rigging": ["cartography", "gunpowder"], "exploration": ["cartography", "mercenaries", "medieval_faires"], "industrialization": ["mass_production", "square_rigging"], "scientific_theory": ["banking", "astronomy", "the_enlightenment"], "colonialism": ["astronomy", "mercantilism"], "ballistics": ["metal_casting", "siege_tactics"], "economics": ["metal_casting", "scientific_theory"], "scorched_earth": ["metal_casting", "nationalism"], "steam_power": ["industrialization"], "flight": ["industrialization", "scientific_theory", "economics"], "steel": ["industrialization", "rifling"], "class_struggle": ["industrialization", "ideology"], "sanitation": ["scientific_theory", "urbanization"], "rifling": ["ballistics", "military_science"], "totalitarianism": ["military_science", "ideology"], "electricity": ["steam_power", "mercantilism"], "radio": ["steam_power", "flight", "conservation"], "chemistry": ["sanitation"], "suffrage": ["sanitation", "ideology"], "replaceable_parts": ["economics"], "capitalism": ["economics", "mass_media"], "combined_arms": ["flight", "combustion"], "synthetic_materials": ["flight", "plastics"], "rapid_deployment": ["flight", "cold_war"], "advanced_ballistics": ["replaceable_parts", "steel", "electricity"], "combustion": ["steel", "natural_history"], "computers": ["electricity", "radio", "suffrage", "totalitarianism", "class_struggle"], "advanced_flight": ["radio"], "rocketry": ["radio", "chemistry"], "nanotechnology": ["radio", "composites"], "mass_media": ["radio", "urbanization"], "nuclear_program": ["chemistry", "ideology"], "plastics": ["combustion"], "satellites": ["advanced_flight", "rocketry"], "globalization": ["advanced_flight", "rapid_deployment", "space_race"], "guidance_systems": ["rocketry", "advanced_ballistics"], "space_race": ["rocketry", "cold_war"], "nuclear_fission": ["advanced_ballistics", "combined_arms"], "telecommunications": ["computers"], "robotics": ["computers", "globalization"], "lasers": ["nuclear_fission"], "cold_war": ["nuclear_fission", "ideology"], "composites": ["synthetic_materials"], "stealth_technology": ["synthetic_materials"], "social_media": ["telecommunications", "professional_sports", "space_race"], "nuclear_fusion": ["lasers"], "code_of_laws": [], "craftsmanship": ["code_of_laws"], "foreign_trade": ["code_of_laws"], "military_tradition": ["craftsmanship"], "early_empire": ["foreign_trade"], "mysticism": ["foreign_trade"], "political_philosophy": ["state_workforce", "early_empire"], "defensive_tactics": ["games_recreation", "political_philosophy"], "humanism": ["drama_poetry", "medieval_faires"], "mercenaries": ["military_training", "feudalism"], "feudalism": ["defensive_tactics"], "civil_service": ["defensive_tactics", "recorded_history"], "divine_right": ["theology", "civil_service"], "diplomatic_service": ["guilds"], "reformed_church": ["guilds", "divine_right"], "the_enlightenment": ["humanism", "diplomatic_service"], "civil_engineering": ["mercantilism"], "nationalism": ["the_enlightenment"], "opera_ballet": ["the_enlightenment"], "natural_history": ["colonialism"], "urbanization": ["civil_engineering", "nationalism"], "conservation": ["natural_history", "urbanization"], "mobilization": ["urbanization"], "cultural_heritage": ["conservation"], "ideology": ["mass_media", "mobilization"], "professional_sports": ["ideology"]}
```
![image](https://github.com/user-attachments/assets/ce81f3e7-65d6-4a75-b240-517f1469cb64)

![image](https://github.com/user-attachments/assets/af502e24-1ee6-41ef-868a-b8ff78e74e1e)

## Задание 2

Файл ex3.py:

```py
import json
import os

completed_tasks_file = "task.txt"

def get_all_depends(graph, targetTech):
    depends = set(graph[targetTech])
    for depend in graph[targetTech]:
        for i in get_all_depends(graph, depend):
            depends.add(i)
    return depends


def generate_makefile(graph, targetTech):
    tasks = load_tasks()
    depends = get_all_depends(graph, targetTech)
    tasks.add(targetTech)
    with open('Makefile', 'w') as f:
        result_string = ""
        for target in depends:
            if target not in tasks:
                tasks.add(target)
                result_string += f'\t@echo "Building {target}"\n'
        if result_string != "":
            f.write(f'{target}:\n')
            f.write(result_string)
    save_tasks(tasks)

def load_tasks():
    if os.path.exists(completed_tasks_file):
        with open(completed_tasks_file, 'r') as f:
            return set(f.read().splitlines())
    return set()

def save_tasks(tasks):
    with open(completed_tasks_file, 'w') as f:
        f.write('\n'.join(tasks))

if __name__ == '__main__':
    with open('civgraph.json') as file:
        graph = json.load(file)
    target = input('Enter target: ')
    generate_makefile(graph, target)
    print("Makefile создан.")
```

![image](https://github.com/user-attachments/assets/096a79b4-0221-4d2d-a63b-05ca771fdd8a)

## Задание 3

Файл ex3.py:

```py
import json
import os

completed_tasks_file = "task.txt"

def get_all_depends(graph, targetTech):
    depends = set(graph[targetTech])
    for depend in graph[targetTech]:
        for i in get_all_depends(graph, depend):
            depends.add(i)
    return depends


def generate_makefile(graph, targetTech):
    tasks = load_tasks()
    depends = get_all_depends(graph, targetTech)
    tasks.add(targetTech)
    with open('Makefile', 'w') as f:
        result_string = ""
        for target in depends:
            if target not in tasks:
                tasks.add(target)
                result_string += f'\t@echo "Building {target}"\n'
        if result_string != "":
            f.write(f'{target}:\n')
            f.write(result_string)
    save_tasks(tasks)

def load_tasks():
    if os.path.exists(completed_tasks_file):
        with open(completed_tasks_file, 'r') as f:
            return set(f.read().splitlines())
    return set()

def save_tasks(tasks):
    with open(completed_tasks_file, 'w') as f:
        f.write('\n'.join(tasks))

def clean():
    if os.path.exists(completed_tasks_file):
        os.remove(completed_tasks_file)
        print("Cleaned completed tasks.")

if __name__ == '__main__':
    with open('civgraph.json') as file:
        graph = json.load(file)
    target = input('Enter target: ')
    if target == "clean":
        clean()
    else:
        generate_makefile(graph, target)
        print("Makefile создан.")
```

![image](https://github.com/user-attachments/assets/b743e370-af7f-4c86-8b8a-104fbb2aa44d)

## Задание 4

Файл prog.c:

```c
#include <stdio.h>
#include "data.h"

int main() {
    printf("Hello, World!\n");
    print_data();
    return 0;
}
```

Файл data.c:

```c
#include <stdio.h>

void print_data() {
    printf("This is data from data.c\n");
}
```

Файл data.h:

```c
#ifndef DATA_H
#define DATA_H

void print_data();

#endif
```

Файл Makefile:

```
CC = gcc

TARGET = prog

SOURCES = prog.c data.c
OBJECTS = $(SOURCES:.c=.o)

all: $(TARGET) files.lst archive

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@

files.lst:
	ls > files.lst

archive: files.lst
	zip distr.zip *.*

%.o: %.c
	$(CC) -c $< -o $@

clean:
	rm -f $(TARGET) $(OBJECTS) files.lst distr.zip
```
![image](https://github.com/user-attachments/assets/e3b40522-1a41-4f8a-a41e-21c44f3843c9)



