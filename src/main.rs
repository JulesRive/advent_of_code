use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::fs::read_to_string;
use std::fs;

fn main() {
    for entry in fs::read_dir(".") {
        let entry = entry;
        let path = entry.path();
        
        // Get file name as string
        let name = path.file_name()
            .and_then(|n| n.to_str())
            .unwrap_or("Invalid filename");
            
        // Check if it's a directory
        let file_type = if path.is_dir() {
            "Directory"
        } else {
            "File"
        };
        
        // Print the entry
        println!("{}: {}", file_type, name);
    }
    
    let mut array1: Vec<i32> = Vec::new();
    let mut array2: Vec<i32> = Vec::new();

    let lines = read_lines("input.txt");
    // Consumes the iterator, returns an (Optional) String
    for line in lines {
        let numbers: Vec<i32> = line.split_whitespace().filter_map(|num| num.parse().ok()).collect();

        // If we have two numbers, add them to their respective arrays
        if numbers.len() == 2 {
            array1.push(numbers[0]);
            array2.push(numbers[1]);
        } else {
            eprintln!("Warning: Line doesn't contain exactly two numbers: {}", line);
        }        
    }
}

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename) 
        .unwrap()  // panic on possible file-reading errors
        .lines()  // split the string into an iterator of string slices
        .map(String::from)  // make each slice into a string
        .collect()  // gather them together into a vector
}
