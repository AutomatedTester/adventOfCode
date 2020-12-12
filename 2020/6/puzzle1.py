def calculate():
    lines = None
    with open("data.txt") as f:
        lines = f.readlines()

    tmp_data = []
    customs_forms = []
    for line in lines:
        if line.strip() == "":
            customs_forms.append([i for i in "".join(tmp_data)])
            tmp_data = []
        else:
            tmp_data.append(line.strip())
    if len(tmp_data) != 0:
        customs_forms.append([i for i in "".join(tmp_data)])
        tmp_data = []

    score = 0
    for counts_ in customs_forms:
        score += len(set(counts_))

    print(f"The Score is {score}")


if __name__ == "__main__":
    calculate()
