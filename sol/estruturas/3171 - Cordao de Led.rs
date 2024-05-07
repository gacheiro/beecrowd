// 3171 - Cordão de Led
// https://judge.beecrowd.com/pt/problems/view/3171

use std::io;

fn main() -> io::Result<()> {
    let stdin = io::stdin();

    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;
    let nl: Vec<usize> =  buffer.trim().split(" ")
                                .map(|x| x.parse().unwrap())
                                .collect();
 
    let mut adj_m: Vec<Vec<usize>> = Vec::new(); 
    let mut lighted_up: Vec<bool> = vec![false; nl[0]];

    for _ in 0..nl[0] {
        adj_m.push(Vec::new());
    }
 
    for _ in 0..nl[1] {
        let mut buffer = String::new();
        stdin.read_line(&mut buffer)?;
        let uv: Vec<usize> = buffer.trim()
                                   .split(" ")
                                   .map(|x| x.parse::<usize>().unwrap())
                                   .map(|x| x - 1) // make index start at 0
                                   .collect();
        
        adj_m[uv[0]].push(uv[1]);
        adj_m[uv[1]].push(uv[0]);
    }

    let mut stack: Vec<usize> = vec![0];
    
    while let Some(led) = stack.pop() {
        lighted_up[led] = true;

        for &adj in &adj_m[led] {
            if !stack.contains(&adj) && !lighted_up[adj] {
                stack.push(adj);
            }
        }
    }

    match lighted_up.iter().all(|&l| l) {
        true => println!("COMPLETO"),
        false => println!("INCOMPLETO"),
    }

    println!("{:?}", lighted_up);

    Ok(())
}

