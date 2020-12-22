use std::fs;
use std::path::Path;
use std::vec::Vec;

fn main() {
    let data = Path::new("data.txt");
    let data_lines = fs::read_to_string(&data).expect("Should have read the file");
    let lines = data_lines.split("\n").collect();
    puzzle1(&lines);
    puzzle2(&lines);
}

fn puzzle2(lines: &Vec<&str>) {
    let mut valid = 0;
    let mut not_valid = 0;
    for line in lines {
        if line == &"" {
            continue;
        }
        let dat: Vec<&str> = line.split(" ").collect();
        let nums: Vec<&str> = dat[0].split("-").collect();
        let letter = dat[1].chars().nth(0).unwrap();
        let password = dat[2];
        if (password
            .chars()
            .nth(nums[0].parse::<usize>().unwrap() - 1)
            .unwrap()
            == letter
            || password
                .chars()
                .nth(nums[1].parse::<usize>().unwrap() - 1)
                .unwrap()
                == letter)
            && (password
                .chars()
                .nth(nums[0].parse::<usize>().unwrap() - 1)
                .unwrap()
                != letter
                || password
                    .chars()
                    .nth(nums[1].parse::<usize>().unwrap() - 1)
                    .unwrap()
                    != letter)
        {
            valid += 1;
        } else {
            not_valid += 1;
        }
    }
    println!(
        "There are {} valid passwords and {} invalid passwords",
        valid, not_valid
    )
}

fn puzzle1(lines: &Vec<&str>) {
    let mut valid = 0;
    let mut not_valid = 0;
    for line in lines {
        if line == &"" {
            continue;
        }
        let dat: Vec<&str> = line.split(" ").collect();
        let nums: Vec<&str> = dat[0].split("-").collect();
        let letter = dat[1].chars().nth(0).unwrap();
        let password = dat[2];
        if password.matches(letter).count() >= nums[0].parse::<usize>().unwrap()
            && password.matches(letter).count() <= nums[1].parse::<usize>().unwrap()
        {
            valid += 1;
        } else {
            not_valid += 1;
        }
    }
    println!(
        "There are {} valid passwords and {} invalid passwords",
        valid, not_valid
    )
}
