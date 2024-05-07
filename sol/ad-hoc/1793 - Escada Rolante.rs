// 1793 - Escada Rolante
// https://judge.beecrowd.com/pt/problems/view/1793

use std::io;
use std::cmp::min;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();

    loop {
        buffer.clear();
        stdin.read_line(&mut buffer)?;
        let n: i32 = buffer.trim().parse().unwrap();

        if n == 0 {
            break;
        }

        buffer.clear();
        stdin.read_line(&mut buffer)?;
        let times: Vec<i32> = buffer.trim().split(" ")
                                    .map(|t| t.parse().unwrap()).collect();

        let active: i32 = times.iter().zip(times.iter().skip(1))
                            .map(|(t1, t2)| min(t2 - t1, 10))
                            .sum::<i32>() + 10; // add 10s for the last person

        println!("{}", active);
    }
    Ok(())
}
