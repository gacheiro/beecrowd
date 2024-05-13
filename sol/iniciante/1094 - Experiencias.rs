// 1094 - Experiências
// https://judge.beecrowd.com/pt/problems/view/1094

use std::io;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;
    let n: usize = buffer.trim().parse().unwrap();
    let (mut r, mut s, mut c) = (0, 0, 0);

    for _ in 0..n {
        buffer.clear();
        stdin.read_line(&mut buffer)?;
        let data: Vec<_> = buffer.split_whitespace().collect();
        let amount: u32 = data[0].parse().unwrap();
        if data[1] == "R" {
           r += amount;
        } else if data[1] == "S" {
           s += amount;
        } else {
           c += amount;
        }
    }

    let rsc = r + s + c;
    println!("Total: {} cobaias", c + r + s);
    println!("Total de coelhos: {}", c);
    println!("Total de ratos: {}", r);
    println!("Total de sapos: {}", s);
    println!("Percentual de coelhos: {:.2} %",
             100_f64 * (c as f64 / rsc as f64));
    println!("Percentual de ratos: {:.2} %",
             100_f64 * (r as f64 / rsc as f64));
    println!("Percentual de sapos: {:.2} %",
             100_f64 * (s as f64 / rsc as f64));
    Ok(())
}

