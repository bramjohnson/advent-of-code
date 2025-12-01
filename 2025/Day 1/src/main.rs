use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::path::Path;

enum DialInput {
    Right(u8),
    Left(u8),
}

struct Dial {
    rotated: u8
}


fn string_to_dialinput(src: String) -> Option<DialInput> {
    // Need at least a direction and an amount
    if src.len() < 2 {
        return None
    }

    let direction = src.chars().nth(0)?;
    let amount = src;

    match direction {
        'R' => Some(DialInput::Right(amount)),
        'L' => Some(DialInput::Left(amount)),
        _ => None
    }
}

fn read_input(path: &str) -> Vec<DialInput> {
    // Specify the path to your file
    let file_path = Path::new("input.txt"); 

    // Open the file
    let file = File::open(file_path)?; 

    // Create a BufReader for efficient line-by-line reading
    let reader = BufReader::new(file); 

    // Iterate over each line in the file
    return reader.lines().flatten().filter_map(string_to_dialinput).collect()
}

fn part_1() {
    let dial 
    let dial_inputs = read_input("input.txt");

}

fn main() -> io::Result<()> {
    // Specify the path to your file
    let file_path = Path::new("input.txt"); 

    // Open the file
    let file = File::open(file_path)?; 

    // Create a BufReader for efficient line-by-line reading
    let reader = BufReader::new(file); 

    // Iterate over each line in the file
    for line_result in reader.lines() {
        // Handle potential errors during line reading
        let line = line_result?; 
        println!("{}", line);
    }

    Ok(())
}