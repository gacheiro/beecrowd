// 2868 - Errrou!
// https://judge.beecrowd.com/pt/problems/view/2868

use std::io;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();

    stdin.read_line(&mut buffer)?;
    let n: i32 = buffer.trim().parse().unwrap();

    for _ in 0..n {
        buffer.clear();
        stdin.read_line(&mut buffer)?;

        let op: Vec<_> =  buffer.trim().split(" ").collect();
        let a = op[0].parse::<i32>().unwrap();
        let b = op[2].parse::<i32>().unwrap();
        let c = op[4].parse::<i32>().unwrap();

        let res: i32 = match op[1] {
            "+" => a + b,
            "-" => a - b,
            "x" => a * b,
            _ => panic!(),
        };

        print!("E");
        for _ in 0..(res - c).abs() {
            print!("r");
        }
        println!("ou!");
    }

    Ok(())
}
