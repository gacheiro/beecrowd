// 2594 - Eachianos ||
// https://judge.beecrowd.com/pt/problems/view/2594

use std::io;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut buffer = String::new();
    stdin.read_line(&mut buffer)?;
    // format so the first and last word have a trailling
    // white space (avoid finding substrings)
    let text = format!(" {} ", buffer.trim()).to_string();

    stdin.read_line(&mut buffer)?;
    buffer.clear();
    stdin.read_line(&mut buffer)?;
    let words: Vec<String> = buffer.split_whitespace()
                        .map(|w| {
                            format!(" {} ", w.trim()).to_string()
                        }).collect();

    for word in &words {
        let mut idx = 0;
        let mut occurrences = Vec::new();
        while let Some(occurrence_idx) = text[idx..].find(word) {
            occurrences.push(idx + occurrence_idx);
            idx += occurrence_idx + word.len() - 1;
            //                                   ^ because the " " is shared
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

