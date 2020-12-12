def calculate():
    lines = None
    with open("data.txt") as f:
        lines = f.readlines()

    position = 0
    accumulation = 0
    where = []
    while position < len(lines):
        if lines[position].startswith("nop"):
            print("nop")
            if position in where:
                break
            where.append(position)
            position += 1
            continue
        elif lines[position].startswith("acc"):
            print("acc")
            if position in where:
                break
            accumulation += int(lines[position].strip()[4:])
            where.append(position)
            position += 1
        elif lines[position].startswith("jmp"):
            print("jmp")
            if position in where:
                break
            position += int(lines[position].strip()[4:])

    print(f"The accumulation is {accumulation}")


if __name__ == "__main__":
    calculate()
