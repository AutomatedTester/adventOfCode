import pdb


def calculate():

    lines = []
    with open("data.txt") as f:
        lines = f.readlines()

    mem: list = [0]*100000
    mask = ""
    for line in lines:
        if line.startswith("mask ="):
            mask = line.split(" ")[2].strip()
            continue
        splitted = line.split(" ")
        index = int(splitted[0][4:][:-1])
        number = "{0:b}".format(int(splitted[2]))
        number = "0"*(36 - len(number)) + number
        tmp = []
        for num in number:
            tmp.append(num)

        for i, num in enumerate(number):
            zeroes = False
            if mask[i] == "X":
                if zeroes:
                    tmp[i] = 0
                continue
            else:
                tmp[i] = mask[i]
                zeroes = True
        number = "".join(tmp)
        mem[index] = number

    sum = 0
    for im in mem:
        if im != 0:
            sum += int(im, 2)

    print(f"The sum is {sum}")


if __name__ == "__main__":
    calculate()
