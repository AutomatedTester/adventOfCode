def calculate():

    lines = []
    with open("data.txt") as f:
        lines = f.readlines()

    north_south = 0
    east_west = 0
    direction = "east"
    all_directions = ["north", "east", "south", "west"]
    for line in lines:
        stripped = line.strip()
        if stripped[0] == "N":
            if direction in ["east", "west", "north"]:
                north_south += int(stripped[1:])
            if direction == "south":
                north_south -= int(stripped[1:])
        if stripped[0] == "E":
            if direction in ["east", "south", "north"]:
                east_west += int(stripped[1:])
            if direction == "west":
                east_west -= int(stripped[1:])
        if stripped[0] == "S":
            if direction in ["east", "west", "south"]:
                north_south -= int(stripped[1:])
            if direction == "north":
                north_south += int(stripped[1:])
        if stripped[0] == "W":
            if direction in ["west", "south", "north"]:
                east_west -= int(stripped[1:])
            if direction == "east":
                east_west += int(stripped[1:])

        if stripped[0] == "F":
            if direction == "north":
                north_south += int(stripped[1:])
            elif direction == "south":
                north_south -= int(stripped[1:])
            elif direction == "east":
                east_west += int(stripped[1:])
            else:
                east_west -= int(stripped[1:])

        if stripped[0] == "L":
            move_by = int(stripped[1:])/90
            direction = all_directions[int((all_directions.index(
                direction) - move_by) % len(all_directions))]
        elif stripped[0] == "R":
            move_by = int(stripped[1:])/90
            direction = all_directions[int((all_directions.index(
                direction) + move_by) % len(all_directions))]

    print(f"the North_south value is {north_south}")
    print(f"the east west value is {east_west}")


if __name__ == "__main__":
    calculate()
