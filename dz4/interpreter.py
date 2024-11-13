import struct
import json
import sys

# Загрузка кода операций
COMMANDS = {
    58: 'LOAD_CONST',
    3: 'READ_MEM',
    30: 'WRITE_MEM',
    124: 'BITWISE_OR'
}

registers = [0] * 1024
memory = [0] * 1024

def load_const(binary_file):
    B, C = struct.unpack('<HI', binary_file.read(6))
    registers[C] = B

def read_mem(binary_file):
    B, C = struct.unpack('<BH', binary_file.read(3))
    registers[B] = memory[C]

def write_mem(binary_file):
    B, C, D = struct.unpack('<BBH', binary_file.read(4))
    addr = registers[C] + D
    memory[addr] = registers[B]
def bitwise_or(binary_file):
    B, C, D, E = struct.unpack('<BBBB', binary_file.read(4))
    addr=registers[E]+C
    memory[addr]=registers[D]|memory[registers[B]]


def execute(binary_path, result_path, memory_range):
    with open(binary_path, 'rb') as binary_file:
        while True:
            opcode_byte = binary_file.read(1)
            if not opcode_byte:
                break

            opcode = opcode_byte[0]

            if opcode == 58:  # LOAD_CONST
                load_const(binary_file)
            elif opcode == 3:  # READ_MEM
                read_mem(binary_file)
            elif opcode == 30:  # WRITE_MEM
                write_mem(binary_file)
            elif opcode == 124:  # BITWISE_OR
                bitwise_or(binary_file)
            else:
                raise ValueError(f"Неизвестная команда с кодом: {opcode}")

    # Сохранение указанного диапазона памяти в результат
    with open(result_path, 'w') as result_file:
        json.dump(memory[memory_range[0]:memory_range[1]], result_file)

if __name__ == "__main__":
    binary_path = sys.argv[1]
    result_path = sys.argv[2]
    memory_range = list(map(int, sys.argv[3].split(',')))
    execute(binary_path, result_path, memory_range)
