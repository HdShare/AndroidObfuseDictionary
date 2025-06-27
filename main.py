import itertools


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    return lines


def generate(lines, repeat=5):
    return [''.join(combination) for combination in itertools.product(lines, repeat=repeat)]


def write_file(combinations, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n'.join(combinations))


if __name__ == '__main__':
    write_file(generate(read_file('obf-dict-base.txt')), 'obf-dict.txt')
