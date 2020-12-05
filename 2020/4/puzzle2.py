def process() -> None:
    lines = []
    with open("data.txt") as f:
        lines = [line.strip() for line in f]

    passports: list = []
    position = 0
    while position < len(lines):
        if lines[position] == "":
            position += 1
            continue
        passport = lines[position].split(" ")
        next_position = 1
        while position + next_position < len(lines) and lines[position + next_position] != "":
            passport += lines[position + next_position].split(" ")
            next_position += 1

        passports.append(create_passport(passport))
        position += next_position
    validate_passports(passports)


def validate_passports(passports: list) -> None:
    valid = 0
    invalid = 0
    VALID_KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    # import pdb
    # pdb.set_trace()
    for passport in passports:
        keys = passport.keys()
        if "cid" in keys:
            if len(keys) == 8:
                invld = False
                for key in VALID_KEYS:
                    if key not in keys:
                        invalid += 1
                        invld = True
                        break
                if not invld:
                    if deeper_checks(passport):
                        valid += 1
                    else:
                        invalid += 1
                    continue
            else:
                invld = False
                for key in VALID_KEYS:
                    if key not in keys:
                        invalid += 1
                        invld = True
                        break
                if not invld:
                    if deeper_checks(passport):
                        valid += 1
                    else:
                        invalid += 1
                    continue
        else:
            ALT_VALID_KEYS = VALID_KEYS.copy()
            ALT_VALID_KEYS.remove("cid")
            invld = False
            for key in ALT_VALID_KEYS:
                if key not in keys:
                    invalid += 1
                    invld = True
                    break
            if not invld:
                if deeper_checks(passport):
                    valid += 1
                else:
                    invalid += 1
                continue

    print(f"Valid Passports: {valid}\nInvalid Passports: {invalid}")


def deeper_checks(passport) -> bool:
    byr = int(passport.get("byr"))
    if byr < 1920 or byr > 2002:
        return False
    iyr = int(passport.get("iyr"))
    if iyr < 2010 or iyr > 2020:
        return False
    eyr = int(passport.get("eyr"))
    if eyr < 2020 or eyr > 2030:
        return False
    hgt = passport.get("hgt")
    unit = hgt[-2:]
    try:
        height = int(hgt[:-2])
    except:
        return False
    if unit == "cm":
        if height < 150 or height > 193:
            return False
    elif unit == "in":
        if height < 59 or height > 76:
            return False
    else:
        return False
    hcl = passport.get("hcl")
    if hcl[0] != "#":
        return False
    else:
        if len(hcl) != 7:
            return False
    valid_eye_colour = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    ecl = passport.get("ecl")
    if ecl not in valid_eye_colour:
        return False
    pid = passport.get("pid")
    if len(pid) != 9:
        return False
    else:
        try:
            int(pid)
        except:
            return False
    return True


def create_passport(passport: list) -> dict:
    processed = {}
    for item in passport:
        data = item.split(":")
        processed[data[0]] = data[1]
    return processed


if __name__ == "__main__":
    process()
