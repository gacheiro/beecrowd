// 1379 - Problema com Mediana e Média
// https://judge.beecrowd.com/pt/problems/view/1379

use std::io;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();

    loop {
        stdin.read_line(&mut buffer)?;

        let values: Vec<i32> = buffer.trim().split(" ")
                                     .map(|v| v.parse().unwrap())
                                     .collect();

        if values[0] == 0 && values[1] == 0 {
            break;
        }

        println!("{}", values[0] - (values[1] - values[0]));
        buffer.clear();
    }

    Ok(())
}
