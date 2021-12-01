def calculate():
    data = None
    with open("data.txt", "r") as file:
        data = file.readlines()

    parsed = []
    for dat in data:
        parsed.append(int(dat))

    increased = 0
    previous = None
    for depth in parsed:
        if previous is None:
            previous = depth
            continue
        if depth > previous:
            increased += 1
        previous = depth

    print("We had %s increases" % increased)


if __name__ == "__main__":
    calculate()
