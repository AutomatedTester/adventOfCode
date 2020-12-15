def calculate():

    lines = []
    with open("data.txt") as f:
        lines = sorted([int(line) for line in f])

    position = 0
    current = 0
    three_volt = 0
    one_volt = 0
    while position < len(lines):
        if position == 0:
            current = lines[position]
            position += 1
            continue
        if current + 1 in lines:
            position = lines.index(current + 1)
            current += 1
            one_volt += 1
            continue
        if current + 2 in lines:
            position = lines.index(current + 2)
            current += 2
            continue
        if current + 3 in lines:
            position = lines.index(current + 3)
            current += 3
            three_volt += 1
            continue

        break
    print(f"We can handle voltage of {current} + 3 = {current + 3}")
    print(f"1-Volt: {one_volt}")
    print(f"3-Volt: {three_volt}")
    print(f"{one_volt * three_volt}")


if __name__ == "__main__":
    calculate()
