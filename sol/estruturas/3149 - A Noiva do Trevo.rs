// 3149 - A Noiva do Trevo
// https://judge.beecrowd.com/pt/problems/view/3149

use std::io;

#[derive(Debug)]
struct Person {
    name: String,
    relative_time: i32,
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;

    let nm: Vec<i32> = buffer.trim().split_whitespace()
                             .map(|x| x.parse().unwrap())
                             .collect();

    let mut people: Vec<Person> = Vec::new();
    for _ in 0..nm[1] {
        let mut buffer = String::new();
        stdin.read_line(&mut buffer)?;
        let data: Vec<_> = buffer.trim().split_whitespace()
                                 .collect();
        let h: i32 = data[0][..2].parse().unwrap();
        let m: i32 = data[0][3..].parse().unwrap();

        let time = if h == 23 {
           m - 60
        } else {
           m
        };

        if time.abs() <= nm[0] {
            people.push(Person { name: String::from(data[1]),
                                 relative_time: time });
        }
    }

    people.sort_by_key(|x| x.relative_time);
    for p in people.iter() {
        println!("{}", p.name);
    }

    Ok(())
}

