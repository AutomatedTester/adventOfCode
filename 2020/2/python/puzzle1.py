

def valid():
    data = None
    with open("data.txt", "r") as file:
        data = file.readlines()

    valid = 0
    not_valid = 0
    for line in data:
        dat = line.split(" ")
        nums = dat[0].split("-")
        letter = dat[1][0]
        password = dat[2]
        if password.count(letter) >= int(nums[0]) and password.count(letter) <= int(nums[1]):
            valid += 1
        else:
            not_valid += 1

    print(
        f"There are {valid} valid passwords and {not_valid} invalid passwords")


if __name__ == "__main__":
    valid()
