// 2370 - Times
// https://judge.beecrowd.com/pt/problems/view/2370

use std::io;

#[derive(Debug)]
struct Player {
    name: String,
    score: i32,
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;

    let nm: Vec<usize> = buffer.split_whitespace()
                               .map(|x| x.parse().unwrap())
                               .collect();

    let mut players: Vec<Player> = Vec::new();
    for _ in 0..nm[0] {
        let mut buffer = String::new();
        stdin.read_line(&mut buffer)?;
        let data: Vec<_> = buffer.trim().split_whitespace().collect();
        players.push(Player { name: String::from(data[0]),
                              score: data[1].parse::<i32>().unwrap() });
    }

    players.sort_by(|a, b| b.score.cmp(&a.score));

    for t in 0..nm[1] {
        println!("Time {}", t + 1);
        let mut names: Vec<&str> = Vec::new();
        for i in (t..nm[0]).step_by(nm[1]) {
            names.push(&players[i].name);
        }

        names.sort_by(|a, b| a.cmp(&b));
        println!("{}\n", &names.join("\n"));
    }

    Ok(())
}

