def read_data():
    data = None
    with open("data.txt", "r") as f:
        data = [line.strip() for line in f]
    return data


def puzzle1():

    data = read_data()
    first = []
    second = []
    third = []
    forth = []
    fifth = []
    sixth = []
    seventh = []
    eighth = []
    nineth = []
    tenth = []
    eleventh = []
    twelth = []
    for line in data:
        first.append(line[0])
        second.append(line[1])
        third.append(line[2])
        forth.append(line[3])
        fifth.append(line[4])
        sixth.append(line[5])
        seventh.append(line[6])
        eighth.append(line[7])
        nineth.append(line[8])
        tenth.append(line[9])
        eleventh.append(line[10])
        twelth.append(line[11])

    g_frst, e_frst = calculate_gamma_epsilon(sorted(first))
    g_scnd, e_scnd = calculate_gamma_epsilon(sorted(second))
    g_thrd, e_thrd = calculate_gamma_epsilon(sorted(third))
    g_frth, e_frth = calculate_gamma_epsilon(sorted(forth))
    g_fifth, e_fifth = calculate_gamma_epsilon(sorted(fifth))
    g_sixth, e_sixth = calculate_gamma_epsilon(sorted(sixth))
    g_seventh, e_seventh = calculate_gamma_epsilon(sorted(seventh))
    g_eighth, e_eighth = calculate_gamma_epsilon(sorted(eighth))
    g_nineth, e_nineth = calculate_gamma_epsilon(sorted(nineth))
    g_tenth, e_tenth = calculate_gamma_epsilon(sorted(tenth))
    g_11th, e_11th = calculate_gamma_epsilon(sorted(eleventh))
    g_12th, e_12th = calculate_gamma_epsilon(sorted(twelth))

    gamma = g_frst+g_scnd+g_thrd+g_frth+g_fifth+g_sixth + \
        g_seventh+g_eighth+g_nineth+g_tenth+g_11th+g_12th
    epsilon = e_frst+e_scnd+e_thrd+e_frth+e_fifth+e_sixth + \
        e_seventh+e_eighth+e_nineth+e_tenth+e_11th+e_12th
    print(f"Gamma is {gamma} and the binary is {int(bin(int(gamma,2)), 2)}")
    print(
        f"Epsilon is {epsilon} and the binary is {int(bin(int(epsilon, 2)), 2)}")
    print(
        f"Power Consumption is {int(bin(int(gamma, 2)), 2) * int(bin(int(epsilon, 2)), 2)}")


def calculate_gamma_epsilon(arr):
    length = len(arr)
    ones = arr.index("1")

    gamma = None
    epsilon = None
    if ones > length/2:
        epsilon = "1"
        gamma = "0"
    else:
        epsilon = "0"
        gamma = "1"
    return gamma, epsilon


if __name__ == "__main__":
    puzzle1()
