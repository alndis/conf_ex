import unittest
from parser import parse_json_to_custom_config

class TestCustomConfigParser(unittest.TestCase):

    # 1. Test basic key-value pairs
    def test_basic_key_value_pairs(self):
        json_data = {
            "NAME": "MyApp",
            "VERSION": 1.2
        }
        expected_output = """struct {
    NAME = "MyApp",
    VERSION = 1.2,
}"""
        self.assertEqual(parse_json_to_custom_config(json_data), expected_output)

    # 2. Test nested dictionaries (structs)
    def test_nested_structures(self):
        json_data = {
            "PROJECT": {
                "NAME": "ProjectX",
                "VERSION": 2.1
            },
            "DEBUG": True
        }
        expected_output = """struct {
    PROJECT =     struct {
        NAME = "ProjectX",
        VERSION = 2.1,
    },
    DEBUG = True,
}"""
        self.assertEqual(parse_json_to_custom_config(json_data), expected_output)

    # 3. Test boolean values in lowercase
    def test_boolean_values(self):
        json_data = {
            "ENABLE_FEATURE": True,
            "DEBUG": False
        }
        expected_output = """struct {
    ENABLE_FEATURE = True,
    DEBUG = False,
}"""
        self.assertEqual(parse_json_to_custom_config(json_data), expected_output)

    # 4. Test list handling
    def test_list_handling(self):
        json_data = {
            "MEMBERS": ["Alice", "Bob", "Charlie"],
            "VERSION": 1.0
        }
        expected_output = """struct {
    MEMBERS = "Alice", "Bob", "Charlie",
    VERSION = 1.0,
}"""
        self.assertEqual(parse_json_to_custom_config(json_data), expected_output)

    # 5. Test string values (with quotes)
    def test_string_values(self):
        json_data = {
            "APP_NAME": "TestApp"
        }
        expected_output = """struct {
    APP_NAME = "TestApp",
}"""
        self.assertEqual(parse_json_to_custom_config(json_data), expected_output)

    # 6. Test constant expression (constant assignment)
    def test_constant_expression(self):
        json_data = {
            "CONSTANT": 42,
            "VALUE": 5
        }
        expected_output = """struct {
    CONSTANT = 42,
    VALUE = 5,
}"""
        self.assertEqual(parse_json_to_custom_config(json_data), expected_output)

    # 7. Test invalid key (must be uppercase)
    def test_invalid_key(self):
        json_data = {
            "invalid_key": "value"
        }
        with self.assertRaises(ValueError):
            parse_json_to_custom_config(json_data)

    # 8. Test invalid value types (e.g., unsupported types like sets)
    def test_invalid_value_type(self):
        json_data = {
            "NAME": {"sub_name": set([1, 2, 3])}  # Sets are not supported
        }
        with self.assertRaises(ValueError):
            parse_json_to_custom_config(json_data)

    # 9. Test deeply nested structure
def test_deeply_nested_structure(self):
    json_data = {
        "CONFIG": {
            "LEVEL1": {
                "LEVEL2": {
                    "LEVEL3": {
                        "KEY": "value"
                    }
                }
            }
        }
    }
    expected_output = """struct {
    CONFIG =     struct {
        LEVEL1 =     struct {
            LEVEL2 =     struct {
                LEVEL3 =     struct {
                    KEY = "value",
                },
            },
        },
    },
}"""
    self.assertEqual(parse_json_to_custom_config(json_data), expected_output)


    # 10. Test numeric constants
    def test_numeric_constants(self):
        json_data = {
            "MAX_RETRIES": 3,
            "TIMEOUT": 1000
        }
        expected_output = """struct {
    MAX_RETRIES = 3,
    TIMEOUT = 1000,
}"""
        self.assertEqual(parse_json_to_custom_config(json_data), expected_output)

if __name__ == '__main__':
    unittest.main()
