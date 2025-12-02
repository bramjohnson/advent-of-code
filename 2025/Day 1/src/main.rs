use std::fmt::Display;
use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;

enum DialDirection {
    Right,
    Left,
}

struct DialInstruction {
    direction: DialDirection,
    amount: usize,
}

#[derive(Clone, Copy)]
enum DialCountingMethod {
    LandOnZero,
    PassByZero,
}

#[derive(Clone, Copy)]
struct Dial {
    rotation: u32,
    clicks: usize,
    counting_method: DialCountingMethod,
}

impl Dial {
    fn start(counting_method: DialCountingMethod) -> Dial {
        return Dial {
            rotation: 50,
            clicks: 0,
            counting_method,
        };
    }

    fn update_dial(&self, rotation: u32, clicks: usize) -> Dial {
        return Dial {
            rotation,
            clicks,
            counting_method: self.counting_method,
        };
    }

    fn rotate_tick(&self, direction: &DialDirection) -> Dial {
        let rotation = match (direction, self.rotation) {
            (DialDirection::Left, 0) => 99,
            (DialDirection::Right, 99) => 0,
            (DialDirection::Left, _) => self.rotation - 1,
            (DialDirection::Right, _) => self.rotation + 1,
        };

        let clicks = match (self.counting_method, rotation) {
            (DialCountingMethod::PassByZero, 0) => self.clicks + 1,
            _ => self.clicks,
        };

        return self.update_dial(rotation, clicks);
    }

    fn rotate(&self, direction: &DialDirection, amount: usize) -> Dial {
        // If amount is 0, then the dial landed on the number it is currently pointing to.
        if amount == 0 {
            // Check for land on zero bonus!
            let clicks = match (self.counting_method, self.rotation) {
                (DialCountingMethod::LandOnZero, 0) => self.clicks + 1,
                _ => self.clicks,
            };

            return self.update_dial(self.rotation, clicks);
        }

        // Dial is mid-spin.
        let rotate_tick = self.rotate_tick(direction);
        return rotate_tick.rotate(direction, amount - 1);
    }
}

impl Display for Dial {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let rotation = self.rotation;
        let clicks = self.clicks;
        write!(f, "-> {rotation} [{clicks}]")
    }
}

fn char_to_dial_direction(src: char) -> Option<DialDirection> {
    match src {
        'R' => Some(DialDirection::Right),
        'L' => Some(DialDirection::Left),
        _ => None,
    }
}

fn string_to_dialinput(src: String) -> Option<DialInstruction> {
    // Need at least a direction and an amount
    if src.len() < 2 {
        return None;
    }

    let direction_char = src.chars().nth(0)?;
    let direction = char_to_dial_direction(direction_char)?;
    let amount: usize = src[1..].parse().unwrap();

    return Some(DialInstruction { direction, amount });
}

fn read_input(path: &str) -> Option<Vec<DialInstruction>> {
    let file_path = Path::new(path);
    let file = File::open(file_path).ok()?;
    let reader = BufReader::new(file);

    return Some(
        reader
            .lines()
            .flatten()
            .filter_map(string_to_dialinput)
            .collect(),
    );
}

fn main() -> Result<(), String> {
    let dial_instructions = read_input("input.txt").ok_or("Could not open input")?;

    let mut part1 = Dial::start(DialCountingMethod::LandOnZero);
    let mut part2 = Dial::start(DialCountingMethod::PassByZero);
    for instruction in dial_instructions {
        part1 = part1.rotate(&instruction.direction, instruction.amount);
        part2 = part2.rotate(&instruction.direction, instruction.amount);
    }

    println!("{part1}");
    println!("{part2}");
    Ok(())
}
