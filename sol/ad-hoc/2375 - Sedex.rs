// 2375 - Sedex
// https://judge.beecrowd.com/pt/problems/view/2375

use std::io;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();

    stdin.read_line(&mut buffer)?;
    let d: i32 = buffer.trim().parse().unwrap();

    buffer.clear();
    stdin.read_line(&mut buffer)?;
    let dimensions: Vec<i32> = buffer.trim().split(" ")
                                     .map(|x| x.parse().unwrap()).collect();

    let fit = dimensions.iter().all(|&l| l >= d);
    if fit {
        println!("S");
    }

    else {
        println!("N");
    }

    Ok(())
}