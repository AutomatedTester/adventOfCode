def calculate():
    data = None
    with open("data.txt", "r") as file:
        data = file.readlines()

    parsed = []
    for dat in data:
        parsed.append(int(dat))

    final = 0
    for exp in parsed:
        ma = 2020 - exp
        if ma in parsed:
            final = exp * ma

    print(f"The final answer is {final}")


if __name__ == "__main__":

    calculate()
