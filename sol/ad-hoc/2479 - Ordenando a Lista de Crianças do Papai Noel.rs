// 2479 - Ordenando a Lista de Crianças do Papai Noel
// https://judge.beecrowd.com/pt/problems/view/2479

use std::io;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();

    stdin.read_line(&mut buffer)?;
    let n: i32 = buffer.trim().parse().unwrap();

    // rust v1.48 no stdin.lines()
    buffer.clear();
    for _ in 0..n {
        stdin.read_line(&mut buffer)?;
    }

    let mut list: Vec<_> = buffer.split("\n").collect();
    list.sort_by(|a, b| a[2..].cmp(&b[2..]));

    for name in list.iter() {
        println!("{}", &name[2..]);
    }

    let good = list.iter().filter(|x| x.starts_with("+")).count();
    println!(
        "Se comportaram: {} | Nao se comportaram: {}",
        good,
        list.len() - good
    );

    Ok(())
}
