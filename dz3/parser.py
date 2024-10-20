import math
import json
import re

def parse_json_to_custom_config(data, indent=0):
    validate_json_structure(data)  # Проверяем структуру JSON
    if isinstance(data, dict):
        return parse_dict(data, indent)
    elif isinstance(data, list):
        return parse_list(data, indent)
    else:
        return str(data)

def parse_list(data, indent):
    return ', '.join(f'"{item}"' if isinstance(item, str) else str(item) for item in data)

def parse_dict(data, indent=0):
    config_lines = [" " * indent + "struct {"]
    for key, value in data.items():
        if key.startswith("CONST_"):
            const_name = key[6:]  # Удаляем CONST_ из имени
            const_value = parse_constant_expression(value)  # Вычисляем значение константы
            config_lines.append(" " * (indent + 4) + f"{const_name} <- {const_value},")
        else:
            key = parse_key(key)
            value = parse_value(value, indent + 4)  # Увеличиваем отступ для вложенных структур
            config_lines.append(" " * (indent + 4) + f"{key} = {value},")
    config_lines.append(" " * indent + "}")  # Закрываем основной блок
    return "\n".join(config_lines)

def parse_key(key):
    if not key.replace('_', '').isalpha() or not key.isupper():
        raise ValueError(f"Invalid key name: {key}")
    return key

def parse_value(value, indent=0):
    if isinstance(value, (int, float)):
        return value
    elif isinstance(value, dict):
        return parse_dict(value, indent)
    elif isinstance(value, bool):
        return "true" if value else "false"  # Булевы значения с маленькой буквы
    elif isinstance(value, str):
        return f'"{value}"'
    elif isinstance(value, list):
        return parse_list(value, indent)
    else:
        raise ValueError(f"Unsupported value type: {type(value)}")

def validate_json_structure(data):
    if not isinstance(data, dict):
        raise ValueError("Root element must be an object (dictionary)")

    for key, value in data.items():
        if not isinstance(key, str) or not key.isupper():
            raise ValueError(f"Invalid key name: {key}")
        if not isinstance(value, (str, int, float, bool, dict, list)):
            raise ValueError(f"Unsupported value type for key '{key}': {type(value)}")
        if isinstance(value, dict):
            validate_json_structure(value)

def validate_json(data):
    if 'VERSION' in data and not isinstance(data['VERSION'], (int, float)):
        raise ValueError(f"Expected a number for VERSION, got: {data['VERSION']}")

def evaluate_expression(expression):
    tokens = expression.split()
    if len(tokens) == 3 and tokens[1] == '+':
        return float(tokens[0]) + float(tokens[2])
    elif len(tokens) == 2 and tokens[0] == 'sqrt':
        return math.sqrt(float(tokens[1]))
    else:
        raise ValueError("Invalid expression")

def parse_constant_expression(expr):
    # Приводим выражение к строке, если это не строка
    if isinstance(expr, (int, float)):
        return expr
    expr = expr.strip()
    if expr.startswith('?'):
        return evaluate_expression(expr[1:])  # Убираем ?
    elif " " in expr:  # Поддержка выражений с пробелами
        return evaluate_expression(expr)  # Вычисляем sqrt и другие выражения
    else:
        return expr  # Если это просто значение, возвращаем его

def remove_multiline_comments(input_string):
    # Удаляем многострочные комментарии
    pattern = r'/\*.*?\*/'
    return re.sub(pattern, '', input_string, flags=re.DOTALL)



# if __name__ == "__main__":
#     json_input = """
#     /*
#     Это многострочный
#     комментарий
#     */
#     {
#         "PROJECT_NAME": "NewProject",
#         "VERSION": 0.1,
#         "CONST_SUM": "? 5 + 5",
#         "ENABLE_NOTIFICATIONS": false
#     }
#     """
#     cleaned_json_input = remove_multiline_comments(json_input)
#     data = json.loads(cleaned_json_input)  # Теперь загружаем JSON без комментариев
#     custom_config = parse_json_to_custom_config(data)
#     print(custom_config)