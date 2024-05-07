// 2381 - Lista de Chamada
// https://judge.beecrowd.com/pt/problems/view/2381

use std::io;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();

    stdin.read_line(&mut buffer)?;
    let input_data: Vec<i32> = buffer.trim().split(" ")
                                .map(|x| x.parse().unwrap())
                                .collect();
    buffer.clear();
    for _ in 0..input_data[0] {
        stdin.read_line(&mut buffer)?;
    }

    let mut names: Vec<_> = buffer.trim().split("\n").collect();
    names.sort();

    println!("{}", names[(input_data[1] - 1) as usize]);
    Ok(())
}
