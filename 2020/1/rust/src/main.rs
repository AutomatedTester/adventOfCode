use std::fs;
use std::path::Path;

fn main() {
    puzzle1();
    puzzle2();
}

fn puzzle2() {
    let data = Path::new("data.txt");
    let data_lines = fs::read_to_string(&data).expect("Should have read the file");
    let mut parsed = vec![];
    let lines = data_lines.split("\n");
    for line in lines {
        if line != "" {
            parsed.push(line.parse::<i32>().unwrap());
        }
    }
    let mut small_nums = vec![];
    for nums in parsed {
        if nums < 1000 {
            small_nums.push(nums);
        }
    }

    let mut _final = 0;

    for nums in &small_nums {
        let parts = 2020 - nums;
        for nms in &small_nums {
            let ma = parts - nms;

            if small_nums.contains(&ma) {
                _final = ma * nms * nums;
            }
        }
    }
    println!("The final number for puzzle 2 is {}", _final)
}

fn puzzle1() {
    let data = Path::new("data.txt");
    let data_lines = fs::read_to_string(&data).expect("Should have read the file");
    let mut parsed = vec![];
    let lines = data_lines.split("\n");
    for line in lines {
        if line != "" {
            parsed.push(line.parse::<i32>().unwrap());
        }
    }

    let mut _final = 0;
    for exp in &parsed {
        let ma = 2020 - exp;
        if parsed.contains(&ma) {
            _final = ma * exp;
        }
    }
    println!("The final answer is is {:?}", _final)
}
