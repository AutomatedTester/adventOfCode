def read_data():
    data = None
    with open("data.txt", "r") as f:
        data = [line.strip() for line in f]
    return data


def calculate():
    data = read_data()
    depth = 0
    depth_1 = 0
    distance = 0
    aim = 0
    for movement in data:
        split = movement.split(' ')

        if split[0].lower() == "forward":
            distance += int(split[1])
            depth += aim * int(split[1])
            continue
        if split[0].lower() == "down":
            depth_1 += int(split[1])
            aim += int(split[1])
            continue
        if split[0].lower() == "up":
            depth_1 -= int(split[1])
            aim -= int(split[1])
            continue
    result1 = distance * depth_1
    result2 = distance * depth

    print(f"Puzzle 1: multiple is {result1}")
    print(f"Puzzle 2: multiple is {result2}")


if __name__ == "__main__":
    calculate()
