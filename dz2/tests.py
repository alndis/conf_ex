import unittest
from visual import read_config, read_dependencies, get_transitive_dependencies, visualize_graph

class TestDependencyVisualizer(unittest.TestCase):

    def setUp(self):
        self.dependencies_content = """\
bs4==0.0.1
  - beautifulsoup4 [required: Any, installed: 4.11.1]
    - soupsieve [required: >1.2, installed: 2.3.2.post1]
cmd2==2.4.3
  - attrs [required: >=16.3.0, installed: 22.2.0]
  - pyperclip [required: >=1.6, installed: 1.9.0]
  - pyreadline3 [required: Any, installed: 3.5.2]
  - wcwidth [required: >=0.1.7, installed: 0.2.13]
requests==2.28.1
  - charset-normalizer [required: >=2, installed: 2.1.1]
  - idna [required: >=2.5,<4]
  - urllib3 [required: >=1.21.1,<1.27]
  - certifi [required: >=2017.4.17]
numpy==1.24.1
  - wheel [required: Any, installed: 0.40.0]
  - python [required: >=3.8,<3.11]
pandas==2.2.3
  - numpy [required: >=1.21.0, installed: 1.24.1]
  - python-dateutil [required: >=2.8.1, installed: 2.9.0.post0]
    - six [required: >=1.5, installed: 1.16.0]
  - pytz [required: >=2020.1, installed: 2024.2]
matplotlib==3.6.3
  - contourpy [required: >=1.0.1, installed: 1.0.6]
  - cycler [required: >=0.10, installed: 0.11.0]
  - kiwisolver [required: >=1.0.1, installed: 1.4.4]
  - numpy [required: >=1.17, installed: 1.24.1]
  - pillow [required: >=6.2.0, installed: 9.5.0]
  - pyparsing [required: >=2.3.1, installed: 3.0.9]
  - python [required: >=3.7, installed: 3.8.10]
  - packaging [required: >=20.0, installed: 24.1]
"""
        self.dependencies_file = 'test_dependencies.txt'
        with open(self.dependencies_file, 'w') as f:
            f.write(self.dependencies_content)

    def test_read_dependencies(self):
        dependencies = read_dependencies(self.dependencies_file)
        self.assertIn('matplotlib', dependencies)
        self.assertIn('numpy', dependencies['matplotlib'])
        self.assertIn('cycler', dependencies['matplotlib'])

    def test_get_transitive_dependencies(self):
        dependencies = read_dependencies(self.dependencies_file)
        transitive_deps = get_transitive_dependencies('matplotlib', dependencies)
        
        # Обновляем ожидаемый список транзитивных зависимостей
        expected_deps = {
            'numpy', 'contourpy', 'cycler', 'kiwisolver', 
            'pillow', 'pyparsing', 'packaging', 'wheel', 'python'
        }
        
        self.assertEqual(transitive_deps, expected_deps)

    def test_visualize_graph(self):
        dependencies = read_dependencies(self.dependencies_file)
        output = visualize_graph('matplotlib', dependencies)
        
        # Проверяем, что вывод содержит "graph TD"
        self.assertIn("graph TD", output)
        
        # Проверяем, что зависимости включены в вывод
        for dep in ['numpy', 'contourpy', 'cycler', 'kiwisolver', 'pillow', 'pyparsing', 'packaging', 'wheel', 'python']:
            self.assertIn(f"matplotlib --> {dep}", output)


    def tearDown(self):
        import os
        os.remove(self.dependencies_file)

if __name__ == '__main__':
    unittest.main()
