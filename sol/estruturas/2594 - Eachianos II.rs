// 2594 - Eachianos ||
// https://judge.beecrowd.com/pt/problems/view/2594

use std::io;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;
    let n: usize = buffer.trim().parse().unwrap();

    for _ in 0..n {
        let mut buffer = String::new();
        stdin.read_line(&mut buffer)?;
        // format so the first and last word have a trailling
        // white space (avoid finding substrings)
        let text = format!(" {} ", buffer.trim()).to_string();

        buffer.clear();
        stdin.read_line(&mut buffer)?;
        let word = format!(" {} ", buffer.trim()).to_string();

        let mut idx = 0;
        let mut occurrences = Vec::new();
        while let Some(occurrence_idx) = text[idx..].find(&word) {
            occurrences.push(idx + occurrence_idx);
            idx += occurrence_idx + word.len();
        }

        if occurrences.is_empty() {
            println!("-1");
        } else {
            println!("{}", occurrences.iter().map(usize::to_string)
                                      .collect::<Vec<_>>().join(" "));
        }
    }

    Ok(())
}

