// 2482 - Etiquetas de Noel
// https://judge.beecrowd.com/pt/problems/view/2482

use std::io;
use std::collections::HashMap;

fn main() -> io::Result<()> {
    let stdin = io::stdin();

    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;
    let n: i32 = buffer.trim().parse().unwrap();

    let mut ts = HashMap::new();

    for _ in 0..n {
        let mut idiom_buffer = String::new();
        stdin.read_line(&mut idiom_buffer)?;

        let mut translation_buffer = String::new();
        stdin.read_line(&mut translation_buffer)?;

        ts.insert(
            String::from(idiom_buffer.trim()),
            String::from(translation_buffer.trim())  
        );
    }

    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;
    let m: i32 = buffer.trim().parse().unwrap();

    for _ in 0..m {
        let mut name_buffer = String::new();
        stdin.read_line(&mut name_buffer)?;

        let mut idiom_buffer = String::new();
        stdin.read_line(&mut idiom_buffer)?;

        match ts.get(idiom_buffer.trim()) {
            Some(&ref translation) => println!("{}\n{}\n", name_buffer.trim(),
                                                           translation),
            _ => continue,
        }
    }

    Ok(())
}
