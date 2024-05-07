// 1794 - Lavanderia
// https://judge.beecrowd.com/pt/problems/view/1794

use std::io;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();

    stdin.read_line(&mut buffer)?;
    let n: i32 = buffer.trim().parse().unwrap();
    
    buffer.clear();
    stdin.read_line(&mut buffer)?;
    stdin.read_line(&mut buffer)?;
    let limits: Vec<i32> = buffer.trim().split(&[' ', '\n'][..])
                                 .map(|x| x.parse().unwrap())
                                 .collect();

    if limits[0] <= n && n <= limits[1] && limits[2] <= n && n <= limits[3] {
        println!("possivel");
    }

    else {
        println!("impossivel");
    }

    Ok(())
}
