use std::fs::File;
use std::io::{self, BufRead, BufReader};
use std::path::Path;

struct IDRange {
    start: u64,
    end: u64,
}

fn string_to_range(src: String) -> Option<IDRange> {
    let split: Vec<&str> = src.split('-').collect();
    let start_str = split[0];
    let end_str = split[1];

    let start: u64 = start_str.parse().ok()?;
    let end: u64 = end_str.parse().ok()?;

    return Some(IDRange { start, end })
}

fn string_to_ranges(src: String) -> Vec<IDRange> {
    let ranges: Vec<&str> = src.split(',').collect();
    return ranges.into_iter().map(|x| x.to_owned()).map(string_to_range).flatten().collect()
}


fn read_input(path: &str) -> Option<Vec<IDRange>> {
    let file_path = Path::new(path);
    let file = File::open(file_path).ok()?;
    let reader = BufReader::new(file);
    let lines: Vec<String> = reader.lines().flatten().collect();
    let the_one_line_to_rule_them_all = lines[0].clone();

    return Some(string_to_ranges(the_one_line_to_rule_them_all));
}

fn is_boring_string(src: &String) -> bool {
    if src.len() < 2 {
        return true
    }

    let (_, first_c) = src.char_indices().nth(1).unwrap();
    for c in src.chars() {
        if c != first_c {
            return false
        }
    }

    return true
}

fn is_invalid_string_2(src: &String) -> bool {
    if src.len() < 2 {
        return false
    }

    // Uneven length strings cannot have only sequence repeated twice
    if src.len() % 2 != 0 {
        return false
    }

    let mid = src.len() / 2;
    let (fst, snd) = src.split_at(mid);
    return fst.eq(snd);
}

fn is_invalid_string_n(src: &String, n: usize) -> bool {
    if src.len() < (n * 2) {
        return false
    }

    // println!("{src} w/ {n}");
    let (canon_part, rest) = src.split_at(n);
    return is_string_a_repeat_of(rest, canon_part)
}

fn is_string_a_repeat_of(src: &str, pat: &str) -> bool {
    if src.len() == 0 {
        return true;
    }

    if src.len() < pat.len() {
        return false
    }

    // src length must be a multiple of the pattern length
    if src.len() % pat.len() != 0 {
        return false
    }

    let (front, rest) = src.split_at(pat.len());
    return front.eq(pat) && is_string_a_repeat_of(rest, pat);
}

fn is_invalid_string_wilder(src: &String) -> bool {
    if src.len() < 2 {
        return false
    }

    let half_length = src.len() / 2;
    for n in 1..=half_length {
        if is_invalid_string_n(src, n) {
            println!("Found invalid: {src} split into {n} parts");
            return true
        }
    }

    return false
}

fn part_1() -> Option<()> {
    let input = read_input("input.txt")?;
    let mut invalid_ids: Vec<String> = vec![];
    for range in input {
        for n in range.start..=range.end {
            let n_str = n.to_string();
            if is_invalid_string_2(&n_str) {
                invalid_ids.push(n_str);
            }
        }
    }

    let answer: u64 = invalid_ids.iter().map(|x| x.parse::<u64>()).flatten().sum();
    Some(println!("{answer:?}"))
}

fn part_2() -> Option<()> {
    let input = read_input("input.txt")?;
    let mut invalid_ids: Vec<String> = vec![];
    for range in input {
        for n in range.start..=range.end {
            let n_str = n.to_string();
            if is_invalid_string_wilder(&n_str) {
                invalid_ids.push(n_str);
            }
        }
    }

    let answer: u64 = invalid_ids.iter().map(|x| x.parse::<u64>()).flatten().sum();
    Some(println!("{answer:?}"))
}

fn main() -> io::Result<()> {
    part_1();
    part_2();
    Ok(())
}