// 3358 - Sobrenome nao e Facil
// https://judge.beecrowd.com/pt/problems/view/3358

use std::io;
use std::collections::HashSet;

fn easy(name: &str) -> bool {
    let mut vowels = HashSet::new();
    vowels.extend("aeiouAEIOU".chars());
    let mut counter = 0;
    for c in name.chars() {
        counter = match vowels.contains(&c) {
            false => counter + 1,
            true => 0,
        };

        if counter == 3 {
            return false;
        }
    }
    true
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;
    let n: usize = buffer.trim().parse().unwrap();
    for _ in 0..n {
        buffer.clear();
        stdin.read_line(&mut buffer)?;
        buffer.pop(); // pop '\n'
        match easy(&buffer) {
            true => println!("{} eh facil", buffer),
            false => println!("{} nao eh facil", buffer),
        }
    }

    Ok(())
}

