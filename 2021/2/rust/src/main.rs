use std::fs;
use std::path::Path;

fn main() {
    puzzle1();
    puzzle2();
}

fn puzzle1() {
    let data = Path::new("data.txt");
    let data_lines = fs::read_to_string(&data).expect("Should have read the file");
    let lines = data_lines.split("\n");
    let mut depth = 0;
    let mut distance = 0;
    for line in lines {
        let splits: Vec<&str> = line.split(" ").collect();
        match splits[0] {
            "forward" => distance += splits[1].parse::<i32>().unwrap(),
            "down" => depth += splits[1].parse::<i32>().unwrap(),
            "up" => depth -= splits[1].parse::<i32>().unwrap(),
            _ => {}
        }
    }

    println!("The depth * distance for puzzle 1 is {}", depth * distance)
}

fn puzzle2() {
    let data = Path::new("data.txt");
    let data_lines = fs::read_to_string(&data).expect("Should have read the file");
    let lines = data_lines.split("\n");
    let mut depth: i64 = 0;
    let mut distance: i64 = 0;
    let mut aim: i64 = 0;
    for line in lines {
        let splits: Vec<&str> = line.split(" ").collect();
        match splits[0] {
            "forward" => {
                distance += splits[1].parse::<i64>().unwrap();
                depth += aim * splits[1].parse::<i64>().unwrap();
            }
            "down" => aim += splits[1].parse::<i64>().unwrap(),
            "up" => aim -= splits[1].parse::<i64>().unwrap(),
            _ => {}
        }
    }

    println!("The depth * distance for puzzle 2 is {}", depth * distance)
}
