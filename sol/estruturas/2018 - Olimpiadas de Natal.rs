// 2018 - Olimpiadas de Natal
// https://judge.beecrowd.com/pt/problems/view/2018

use std::io;
use std::collections::HashMap;

#[derive(Debug)]
struct Score {
    name: String,
    gold: u32,
    silver: u32,
    bronze: u32,
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut scores: Vec<Score> = Vec::new();
    let mut scores_map = HashMap::new();

    loop {
        let mut buffer = String::new();
        match stdin.read_line(&mut buffer) {
            Ok(0) => break,
            _    => (),
        }

        for pos in 0..3 {
            let mut country = String::new();
            stdin.read_line(&mut country)?;
            country.pop();

            if !scores_map.contains_key(&country) {
                scores.push(Score { name: country.to_string(),
                                    gold: 0,
                                    silver: 0,
                                    bronze: 0 });
                scores_map.insert(country.to_string(), scores.len() - 1);
            }

            let idx = scores_map.get(&country).unwrap();
            let score = &mut scores[*idx];

            if pos == 0 {
                score.gold += 1;
            } else if pos == 1 {
                score.silver += 1;
            } else {
                score.bronze += 1;
            }
        }
    }

    scores.sort_by(|a, b| {
        if a.gold != b.gold {
            b.gold.cmp(&a.gold)
        } else if a.silver != b.silver {
            b.silver.cmp(&a.silver)
        } else if a.bronze != b.bronze {
            b.bronze.cmp(&a.bronze)
        } else {
            a.name.cmp(&b.name)
        }
    });

    println!("Quadro de Medalhas");
    for score in &scores {
        println!("{} {} {} {}", score.name, score.gold,
                                score.silver, score.bronze);
    }

    Ok(())
}

