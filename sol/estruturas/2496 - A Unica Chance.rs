// 2496 - A Unica Chance
// https://judge.beecrowd.com/pt/problems/view/2496

use std::io;

fn hamming(seq: &Vec<char>) -> i32 {
    let mut sorted_seq = seq.clone();
    sorted_seq.sort();
 
    seq.iter()
       .zip(sorted_seq.iter())
       .map(|(x, y)| {
            if x == y {0} else {1}
       })
       .sum::<i32>()
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();

    stdin.read_line(&mut buffer)?;
    let n: i32 = buffer.trim().parse().unwrap();

    for _ in 0..n {
        let mut buffer = String::new();
        stdin.read_line(&mut buffer)?;
        buffer.clear(); // not needed

        stdin.read_line(&mut buffer)?;
        let seq: Vec<char> = buffer.trim()
                                   .chars()
                                   .collect();

        let fmt = match hamming(&seq) {
            2 => "There are the chance.",
            _ => "There aren't the chance.",
        };

        println!("{}", fmt);
    }

    Ok(())
}

