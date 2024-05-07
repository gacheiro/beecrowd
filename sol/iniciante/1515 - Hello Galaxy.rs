// 1515 - Hello Galaxy
// https://judge.beecrowd.com/pt/problems/view/1515

use std::io;

fn main() -> io::Result<()> {
    
    let stdin = io::stdin();
    let mut buffer = String::new();

    loop {
        buffer.clear();
        stdin.read_line(&mut buffer)?;

        let n = buffer.trim().parse::<i32>().unwrap();
        if n == 0 {
            break;
        }

        let mut oldest_message = String::new();
        let mut oldest_message_date = i32::MAX;

        for _ in 0..n {
            buffer.clear();
            stdin.read_line(&mut buffer)?;
            let mut message_data = buffer.trim()
                                         .split(" ");
            let message = String::from(message_data.next().unwrap());
            let received = message_data.next().unwrap()
                                       .parse::<i32>().unwrap();
            let delay = message_data.next().unwrap()
                                    .parse::<i32>().unwrap();

            if received - delay < oldest_message_date {
                oldest_message = message.clone();
                oldest_message_date = received - delay;
            }
        }

        println!("{}", oldest_message);
    }
    Ok(())
}
