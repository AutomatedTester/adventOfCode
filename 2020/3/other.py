from math import prod


def split(word):
    return [char for char in word]


def count_trees(matrix, index, line_length, slope=1):
    count, pos = 0, 0
    for row in matrix[::slope]:
        if row[pos % line_length] == "#":
            count += 1
        pos += index
    return count


def part_one(matrix, line_length):
    print(count_trees(matrix, 3, line_length))


def part_two(matrix, line_length):
    terms = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    results = [count_trees(matrix, term[0], line_length, term[1])
               for term in terms]
    print(prod(results))


if __name__ == "__main__":
    with open("data.txt") as f:
        matrix = [split(line.strip()) for line in f]
    line_length = len(matrix[0])
    part_one(matrix, line_length)
    part_two(matrix, line_length)
