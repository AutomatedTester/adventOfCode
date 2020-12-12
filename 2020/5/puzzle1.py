import math


def find_seat():
    lines = []
    with open("data.txt") as f:
        lines = [line.strip() for line in f]

    largest = 0
    for line in lines:
        row_data = line[:7]
        seat_data = line[7:]
        row_number = search(row_data, 0, 128)

        seat_number = search(seat_data, 0, 6)

        calc = row_number * 8 + seat_number
        if calc > largest:
            largest = calc

    print(largest)


def search(data, start, end):
    result = 0
    if data[0] in ["F", "B"]:
        search_criteria = "F"
    else:
        search_criteria = "L"

    for dat in data:
        mid = math.floor((start + end)/2)
        if dat == search_criteria:
            end = mid
        else:
            start = mid
        result = mid
    return result


if __name__ == "__main__":
    find_seat()
