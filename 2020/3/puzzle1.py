

def travel():
    raw_data = None
    data = []
    with open("data.txt", "r") as file:
        raw_data = file.readlines()
        for dat in raw_data:
            data.append(dat.replace("\n", ""))

    tree = 0
    not_tree = 0
    position = {"x": 3, "y": 1}
    for i, j in enumerate(data):

        try:

            if data[i+1][position["x"] % (len(data[i]) - 1)] == "#":
                if position["x"] > 30:
                    print(f'{position["x"]}')
                    print(f'{data[i+1]}')
                    print(f'{data[i+1][:position["x"] % (len(data[i]) - 1)]}')
                    print(
                        f'item is {data[i+1][position["x"]% (len(data[i]) - 1)]}')
                tree += 1
            else:
                not_tree += 1
        except IndexError:
            pass
        position["x"] += 3

    print(
        f"There are {tree} trees and {not_tree} not trees")


if __name__ == "__main__":
    travel()
