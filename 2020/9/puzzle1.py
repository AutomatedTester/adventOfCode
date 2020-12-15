PREAMBLE = 6


def calculate():

    with open("data.txt") as f:
        lines = f.readlines()

    position = 0
    data = []
    first = 0
    while position < len(lines):
        print(f"{position}")
        if position < PREAMBLE:
            data.append(int(lines[position]))
            position += 1
            continue
        else:
            calculated = False
            current = int(lines[position])
            first = int(lines[position - 1])
            if current - first in data:
                calculated = True
                break

            data.append(current)
            if not calculated:
                print(f"the number is {current}")
                break

        position += 1


if __name__ == "__main__":
    calculate()
