// 2633 - Churras no Yuri
// https://judge.beecrowd.com/pt/problems/view/2633

use std::io;

#[derive(Debug)]
struct Meat {
    name: String,
    val: i32,
}

// fn print_type_of<T>(_: &T) {
//     println!("{}", std::any::type_name::<T>())
// }

fn main() -> io::Result<()> {
    let stdin = io::stdin();

    loop {
        let mut buffer = String::new();
        match stdin.read_line(&mut buffer) {
            Ok(0) => break, // EOF
            _ => (),
        }

        let mut stock: Vec<Meat> = vec![];

        let n: i32 = buffer.trim().parse().unwrap();

        for _ in 0..n {
            let mut buffer = String::new();
            stdin.read_line(&mut buffer)?;

            let input_data: Vec<_> = buffer.trim()
                                        .split_whitespace()
                                        .collect();

            stock.push(Meat { name : String::from(input_data[0]), 
                              val : input_data[1].parse().unwrap() });
        }

        stock.sort_by_key(|x| x.val);
        println!(
            "{}",
            stock.into_iter().map(|x| x.name)
                        .collect::<Vec<_>>().join(" ")
        );
    }

    Ok(())
}
