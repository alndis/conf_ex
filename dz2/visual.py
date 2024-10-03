import importlib
import yaml
import subprocess

# Функция для парсинга зависимостей пакета
def parse_dependencies(package_path):
    """
    Парсит зависимости пакета из файла setup.py или requirements.txt
    """
    dependencies = {}
    try:
        # Попытка парсинга setup.py
        setup_file = open(package_path + '/setup.py', 'r')
        for line in setup_file:
            if 'install_requires' in line:
                dependencies_list = line.split('=')[1].strip().split(',')
                for dependency in dependencies_list:
                    dependencies[dependency.strip()] = []
        setup_file.close()
    except FileNotFoundError:
        # Если setup.py не найден, парсим requirements.txt
        try:
            requirements_file = open(package_path + '/requirements.txt', 'r')
            for line in requirements_file:
                dependency = line.strip()
                dependencies[dependency] = []
            requirements_file.close()
        except FileNotFoundError:
            print("Не найден файл setup.py или requirements.txt")
            return {}
    return dependencies

# Функция для построения графа зависимостей
def build_graph(dependencies):
    """
    Строит граф зависимостей из списка зависимостей
    """
    graph = {}
    for dependency, sub_dependencies in dependencies.items():
        graph[dependency] = []
        for sub_dependency in sub_dependencies:
            graph[dependency].append(sub_dependency)
    return graph

# Функция для генерации представления Mermaid
def generate_mermaid(graph):
    """
    Генерирует представление Mermaid для графа зависимостей
    """
    mermaid_representation = "graph LR\n"
    for node, edges in graph.items():
        mermaid_representation += f"  {node}\n"
        for edge in edges:
            mermaid_representation += f"  {node} --> {edge}\n"
    return mermaid_representation

# Функция для визуализации графа
def visualize_graph(mermaid_representation, graphviz_path):
    """
    Визуализирует граф зависимостей с помощью Graphviz
    """
    with open('graph.dot', 'w') as f:
        f.write(mermaid_representation)
    subprocess.run([graphviz_path, '-Tpng', 'graph.dot', '-o', 'graph.png'])

# Главная функция
def main():
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    package_path = config['package_path']
    graphviz_path = config['graphviz_path']
    dependencies = parse_dependencies(package_path)
    graph = build_graph(dependencies)
    mermaid_representation = generate_mermaid(graph)
    visualize_graph(mermaid_representation, graphviz_path)

if __name__ == '__main__':
    main()