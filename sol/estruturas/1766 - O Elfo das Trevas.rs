// 1766 - O Elfo das Trevas
// https://judge.beecrowd.com/pt/problems/view/1766

use std::io;

#[derive(Debug)]
struct Reindeer {
    name: String,
    weight: i32,
    age: i32,
    height: f64,
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();

    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;
    let t: i32 = buffer.trim().parse().unwrap();
 
    for i in 1..=t {
        let mut buffer = String::new();
        stdin.read_line(&mut buffer)?;
        let nm: Vec<usize> = buffer.trim().split_whitespace()
                                   .map(|x| x.parse().unwrap())
                                   .collect();
        
        let mut reindeers: Vec<Reindeer> = Vec::new();
        for _ in 0..nm[0] {
            let mut buffer = String::new();
            stdin.read_line(&mut buffer)?;
            let data: Vec<_> = buffer.split_whitespace().collect();
            reindeers.push(
                Reindeer {
                    name: String::from(data[0]),
                    weight: data[1].parse::<i32>().unwrap(),
                    age: data[2].parse::<i32>().unwrap(),
                    height: data[3].parse::<f64>().unwrap(),
                }
            );
        }

        reindeers.sort_by(|a, b| {
            if a.weight != b.weight {
                b.weight.cmp(&a.weight)
            } else if a.age != b.age {
                a.age.cmp(&b.age)
            } else if a.height != b.height {
                a.height.partial_cmp(&b.height).unwrap()
            } else {
                a.name.cmp(&b.name)
            }
        });

        println!("CENARIO {{{}}}", i);
        for k in 0..nm[1] {
            println!("{} - {}", k + 1, reindeers[k].name);
        } 
    }

    Ok(())
}

