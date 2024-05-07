// 2984 - Assuntos Pendentes
// https://judge.beecrowd.com/pt/problems/view/2984

use std::io;
use std::cmp::max;

fn main() -> io::Result<()> {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?;

    let mut pending = 0;
    for c in buffer.chars() {
        match c {
            '(' => pending += 1,
            ')' => pending -= 1,
            _   => continue,
        }
        pending = max(pending, 0);
    }

    if pending > 0 {
        println!("Ainda temos {} assunto(s) pendente(s)!", pending);	
    }

    else {
        println!("Partiu RU!");
    }

    Ok(())
}

