// 2492 - Ilhas Isoladas
// https://judge.beecrowd.com/pt/problems/view/2492

use std::io;
use std::collections::HashMap;

fn main() -> io::Result<()> {
    let stdin = io::stdin();

    loop {
        let mut buffer = String::new();
        stdin.read_line(&mut buffer)?;
        let n: usize = buffer.trim().parse().unwrap();
        if n == 0 {
            break;
        }

        let mut f =  HashMap::new();
        let mut inv_f = HashMap::new();

        for _ in 0..n {
            let mut buffer = String::new();
            stdin.read_line(&mut buffer)?;
            let data: Vec<_> = buffer.split(" -> ").collect();
            f.insert(data[0].to_string(), data[1].to_string());
            inv_f.insert(data[1].to_string(), data[0].to_string());
        }

        if n > f.len() {
            println!("Not a function.");
        } else if f.len() > inv_f.len() {
            println!("Not invertible.");
        } else {
            println!("Invertible.");
        }
    }

    Ok(())
}

