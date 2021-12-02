use std::path::Path;
use std::{env, fs};

const DATA_FILE: &str = "data.txt";
fn main() {
    let target_dir_path = env::var("OUT_DIR").unwrap();
    copy(&target_dir_path, DATA_FILE);
}

fn copy<S: AsRef<std::ffi::OsStr> + ?Sized, P: Copy + AsRef<Path>>(
    target_dir_path: &S,
    file_name: P,
) {
    fs::copy(
        file_name,
        Path::new(&target_dir_path).join("../../..").join(file_name),
    )
    .unwrap();
}
