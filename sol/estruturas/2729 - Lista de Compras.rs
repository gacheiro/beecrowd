// 2729 - Lista de Compras
// https://judge.beecrowd.com/pt/problems/view/2729

use std::io;
use std::collections::HashSet;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;
    let n: i32 = buffer.trim().parse().unwrap();

    for _ in 0..n {
        let mut buffer = String::new();
        stdin.read_line(&mut buffer)?;
        let list: Vec<&str> = buffer.trim().split_whitespace()
                                    .collect();
        let mut set: HashSet<&str> = HashSet::new();
        set.extend(list.iter());

        let mut sorted_items: Vec<&str> = set.into_iter().collect();
        sorted_items.sort();
        println!("{:}", sorted_items.join(" "));
    }

    Ok(())
}
