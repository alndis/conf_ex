import yaml
import os
import requests
from collections import defaultdict

# Чтение конфигурационного файла
def read_config(config_file='config.yaml'):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config

# Получение зависимостей пакета с сайта PyPI
def fetch_dependencies_from_pypi(package_name):
    url = f"https://pypi.org/pypi/{package_name}/json"
    response = requests.get(url)
    if response.status_code == 200:
        package_info = response.json()
        dependencies = package_info.get('info', {}).get('requires_dist', [])
        parsed_dependencies = []
        for dep in dependencies:
            dep_name = dep.split(';')[0].strip().split(' ')[0]
            parsed_dependencies.append(dep_name)
        return parsed_dependencies
    else:
        print(f"Ошибка при получении данных для {package_name}")
        return []

# Запись зависимостей в файл
def write_dependencies_to_file(dependencies, filename='dependencies.txt'):
    with open(filename, 'w') as file:
        for package, deps in dependencies.items():
            file.write(f"{package}==\n")
            for dep in deps:
                file.write(f"  - {dep}\n")

# Чтение зависимостей из файла
def read_dependencies(dependencies_file='dependencies.txt'):
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
                    dep_info = line.split('[')[0].strip()
                    if dep_info:
                        dep_name = dep_info.split(' ')[-1].strip()
                        dependencies[current_package].append(dep_name)
    return dependencies

# Получение транзитивных зависимостей
def get_transitive_dependencies(package_name, dependencies):
    transitive_deps = set()

    def recurse(package):
        for dep in dependencies.get(package, []):
            if dep not in transitive_deps:
                transitive_deps.add(dep)
                recurse(dep)

    recurse(package_name)
    return transitive_deps

# Построение и визуализация графа в формате Mermaid
def visualize_graph(package_name, dependencies):
    transitive_deps = get_transitive_dependencies(package_name, dependencies)
    graph_lines = ["graph TD"]

    for dep in transitive_deps:
        graph_lines.append(f"    {package_name} --> {dep}")

    mermaid_code = "\n".join(graph_lines)

    with open("graph.mmd", "w") as f:
        f.write(mermaid_code)

    os.system("mmdc -i graph.mmd -o graph.png")
    return mermaid_code


# Основная функция запуска
def main():
    config = read_config()
    package_name = config['package_name']

    dependencies = defaultdict(list)
    # Парсим зависимости для matplotlib и записываем их в файл
    dependencies[package_name] = fetch_dependencies_from_pypi(package_name)
    write_dependencies_to_file(dependencies)

    # Читаем зависимости из файла и строим граф
    dependencies = read_dependencies()
    graph_output = visualize_graph(package_name, dependencies)
    print(graph_output)

if __name__ == "__main__":
    main()
