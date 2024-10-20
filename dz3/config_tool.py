import json
import argparse
import sys
from parser import parse_json_to_custom_config, validate_json

def main():
    parser = argparse.ArgumentParser(description="Convert JSON to custom configuration language.")
    parser.add_argument("input_file", help="Path to the input JSON file.")
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r') as file:
            json_data = json.load(file)
            validate_json(json_data)  # Проверяем JSON перед преобразованием
            custom_config = parse_json_to_custom_config(json_data)
            print(custom_config)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as ve:
        print(f"Error parsing JSON: {ve}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
