// 2374 - Pneu
// https://judge.beecrowd.com/pt/problems/view/2374

use std::io;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer_1 = String::new();
    let mut buffer_2 = String::new();

    stdin.read_line(&mut buffer_1)?;
    stdin.read_line(&mut buffer_2)?;

    let pressure_diff = buffer_1.trim().parse::<i32>().unwrap()
                        - buffer_2.trim().parse::<i32>().unwrap();
    println!("{}", pressure_diff);
    Ok(())
}
