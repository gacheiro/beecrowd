// 3176 - Time de Duendes
// https://judge.beecrowd.com/pt/problems/view/3176

use std::io;

#[derive(Debug)]
struct Elf {
    name: String,
    age: i32,
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;

    let nelfs: usize = buffer.trim().parse().unwrap();
    let nteams: usize = nelfs / 3;
    let mut elfs: Vec<Elf> = Vec::new();

    for _ in 0..nelfs {
        let mut buffer = String::new();
        stdin.read_line(&mut buffer)?;
        let data: Vec<_> = buffer.trim().split_whitespace().collect();
        elfs.push(Elf { name: String::from(data[0]),
                        age: data[1].parse::<i32>().unwrap() });
    }

    elfs.sort_by(|a, b| {
        if a.age != b.age {
            b.age.cmp(&a.age)
        } else {
            a.name.cmp(&b.name)
        }
    });

    for t in 0..nteams {
        println!("Time {}", t + 1);
        for i in (t..nelfs).step_by(nteams) {
            println!("{} {}", elfs[i].name, elfs[i].age);
        }
        println!("");
    }

    Ok(())
}

