// 2654 - Godofor
// https://judge.beecrowd.com/pt/problems/view/2654

use std::io;

struct God {
    name: String,
    power: i32,
    kills: i32,
    deaths: i32,
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;

    let n: usize = buffer.trim().parse().unwrap();
    let mut gods: Vec<God> = Vec::new();

    for _ in 0..n {
        let mut buffer = String::new();
        stdin.read_line(&mut buffer)?;
        let data: Vec<_> = buffer.split_whitespace().collect();
        gods.push(God {
            name: String::from(data[0]),
            power: data[1].parse().unwrap(),
            kills: data[2].parse().unwrap(),
            deaths: data[3].parse().unwrap(),
        });
    }

    gods.sort_by(|a, b| {
        if a.power != b.power {
            b.power.cmp(&a.power)
        } else if a.kills != b.kills {
            b.kills.cmp(&a.kills)
        } else if a.deaths != b.deaths {
            a.deaths.cmp(&b.deaths)
        } else {
            a.name.cmp(&b.name)
        }
    });

    println!("{}", gods[0].name);

    Ok(())
}

