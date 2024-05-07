// 1040 - Média 3
// https://judge.beecrowd.com/pt/problems/view/1040

use std::io;

fn main() {
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer).expect("Failed to read line!");
    let weights: [f64; 4] = [2.0, 3.0, 4.0, 1.0];
    let grades: Vec<f64> = buffer
                           .trim()
                           .split(" ")
                           .map(|x| x.parse::<f64>().unwrap())
                           .collect();
    
    
    let avg = grades.iter()
                    .zip(weights.iter()).map(|(x, y)| x * y)
                    .sum::<f64>()
                    / 10.0;
    
    println!("Media: {:.1}", avg);

    if avg >= 7.0 {
        println!("Aluno aprovado.");
    }

    else if avg >= 5.0 {
        buffer.clear();
        io::stdin().read_line(&mut buffer).expect("Failed to read line!");
        let last_grade = buffer.trim().parse::<f64>().unwrap();
        println!("Aluno em exame.\nNota do exame: {:.1}", last_grade);

        let final_grade = (avg + last_grade) / 2.0;
        if final_grade >= 5.0 {
            println!("Aluno aprovado.");
        }

        else {
            println!("Aluno reprovado.");
        }

        println!("Media final: {:.1}", final_grade);
    }

    else {
        println!("Aluno reprovado.");
    }
}
