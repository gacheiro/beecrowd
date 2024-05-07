// 3160 - Amigos
// https://judge.beecrowd.com/pt/problems/view/3160

use std::io;

fn main() -> io::Result<()> {
    let stdin = io::stdin();

    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;

    let list: Vec<_> = buffer.trim()
                             .split_whitespace()
                             .collect();

    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;
    let new_list: Vec<_> = buffer.trim()
                                 .split_whitespace()
                                 .collect();

    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;
    let friend = buffer.trim();

    if friend == "nao" {
        println!("{} {}", &list.join(" "),
                          &new_list.join(" "));
    }

    else {
        let pos = list.iter().position(|&x| x == friend).unwrap();
        let fmt = format!("{} {} {}", &list[..pos].join(" "),
                                      &new_list.join(" "),
                                      &list[pos..].join(" "));
        println!("{}", fmt.trim());
        //                 ^^^^  remove trimming spaces (edge cases);
    }

    Ok(())
}

