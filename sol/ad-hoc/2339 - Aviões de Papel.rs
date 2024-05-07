// 2339 - Aviões de Papel
// https://judge.beecrowd.com/pt/problems/view/2339

use std::io;

fn main() -> io::Result<()> {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;
    let values: Vec<i32> = buffer.trim().split(" ")
                                 .map(|x| x.parse().unwrap())
                                 .collect();
    
    match values[1] >= values[0] * values[2] {
        true => println!("S"),
        false => println!("N"),
    }
    
    Ok(())
}
