// 1047 - Tempo de Jogo com Minutos
// https://judge.beecrowd.com/pt/problems/view/1047

use std::io;

fn main() {
    let mut buffer = String::new();    
    io::stdin()
        .read_line(&mut buffer)
        .expect("Failed to read line!");
    let time: Vec<i32> = buffer.trim()
                               .split(" ")
                               .map(|x| x.parse().unwrap())
                               .collect();
    
    // same day
    let duration = if (time[0] < time[2]) || (time[0] == time[2] && time[1] < time[3]) {
        (time[2] * 60 + time[3]) - (time[0] * 60 + time[1])
    }
    // next day
    else {
        (24 * 60) + (time[2] * 60 + time[3]) - (time[0] * 60 + time[1])
    //              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ this sum is negative
    };

    println!("O JOGO DUROU {} HORA(S) E {} MINUTO(S)",
             duration/60,
             duration - (duration/60) * 60);
}

