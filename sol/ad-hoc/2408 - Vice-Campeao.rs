// 2408 - Vice-Campeao
// https://judge.beecrowd.com/pt/problems/view/2408

use std::io;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();

    stdin.read_line(&mut buffer)?;
    let mut scores: Vec<i32> = buffer.trim().split(" ")
                                 .map(|x| x.parse().unwrap())
                                 .collect();
    scores.sort();
    println!("{}", scores[1]);
    Ok(())
}
