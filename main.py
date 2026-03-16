import itertools

BASE_FILE = 'obf-dict-base.txt'
OUTPUT_FILE = 'obf-dict.txt'
MAX_OUTPUT_COUNT = 500_000
REPEAT_COUNT = 14


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


def generate(lines, repeat=REPEAT_COUNT):
    if len(lines) < repeat:
        raise ValueError(f'基础字符数量不足：至少需要 {repeat} 个，当前只有 {len(lines)} 个')

    combinations = []
    for index, combination in enumerate(itertools.permutations(lines, repeat)):
        if index >= MAX_OUTPUT_COUNT:
            break
        combinations.append(''.join(combination))
    return combinations


def write_file(combinations, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(combinations))


if __name__ == '__main__':
    write_file(generate(read_file(BASE_FILE)), OUTPUT_FILE)
