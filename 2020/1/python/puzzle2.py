def calculate():
    data = None
    with open("data.txt", "r") as file:
        data = file.readlines()

    parsed = []
    for dat in data:
        parsed.append(int(dat))

    small_nums = [x for x in parsed if x < 1000]
    print(small_nums)

    final = 0

    for i, j in enumerate(small_nums):
        partial = 2020 - j
        for num in small_nums:
            ma = partial - num

            if ma in parsed:
                final = ma * num * j

    print(f"The final answer is {final}")


if __name__ == "__main__":

    calculate()
