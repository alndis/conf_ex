import yaml
import os
from collections import defaultdict

# Чтение конфигурационного файла
def read_config(config_file='config.yaml'):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Чтение зависимостей из файла
def read_dependencies(dependencies_file):
    dependencies = defaultdict(list)
    with open(dependencies_file, 'r') as file:
        lines = file.readlines()
        current_package = None
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                if '==' in line:
                    current_package = line.split('==')[0].strip()
                elif current_package:
                    # Извлекаем только имя зависимости
                    dep_info = line.split('[')[0].strip()  # Извлекаем часть до '['
                    if dep_info:  # Убедимся, что зависимость не пустая
                        dep_name = dep_info.split(' ')[-1].strip()  # Извлекаем имя зависимости
                        dependencies[current_package].append(dep_name)

    return dependencies

# Получение транзитивных зависимостей
def get_transitive_dependencies(package_name, dependencies):
    transitive_deps = set()

    def recurse(package):
        for dep in dependencies.get(package, []):
            if dep not in transitive_deps:
                transitive_deps.add(dep)
                recurse(dep)  # Рекурсивный вызов для транзитивных зависимостей

    recurse(package_name)
    return transitive_deps

# Построение и визуализация графа в формате Mermaid
def visualize_graph(package_name, dependencies):
    transitive_deps = get_transitive_dependencies(package_name, dependencies)
    graph_lines = ["graph TD"]  # Начинаем с заголовка для Mermaid

    # Добавляем зависимости
    for dep in transitive_deps:
        graph_lines.append(f"    {package_name} --> {dep}")

    # Генерируем текст в формате Mermaid
    mermaid_code = "\n".join(graph_lines)

    # Сохраняем в файл
    with open("graph.mmd", "w") as f:
        f.write(mermaid_code)

    # Используем Mermaid CLI для генерации изображения
    os.system("mmdc -i graph.mmd -o graph.png")

    # Возвращаем граф в формате Mermaid
    return mermaid_code  # Вернем сгенерированный граф


# Основная функция запуска
def main():
    config = read_config()
    package_name = config['package_name']

    # Читаем зависимости из файла
    dependencies = read_dependencies('dependencies.txt')

    # Визуализируем граф
    graph_output = visualize_graph(package_name, dependencies)
    print(graph_output)

if __name__ == "__main__":
    main()
