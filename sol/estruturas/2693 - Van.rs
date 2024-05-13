// 2693 - Van
// https://judge.beecrowd.com/pt/problems/view/2693

use std::io;

#[derive(Debug)]
struct Student {
    name: String,
    region: String,
    distance: i32,
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();

    loop {
        let mut buffer = String::new();
        match stdin.read_line(&mut buffer) {
            Ok(0) => break,
            _     => (),
        }

        let n: usize = buffer.trim().parse().unwrap();
        let mut students: Vec<Student> = Vec::new();

        for _ in 0..n {
            let mut buffer = String::new();
            stdin.read_line(&mut buffer)?;
            let data: Vec<_> = buffer.split_whitespace().collect();
            students.push(Student {
                name: String::from(data[0]),
                region: String::from(data[1]),
                distance: data[2].parse().unwrap(),
            });
        }

        students.sort_by(|a, b| {
            if a.distance != b.distance {
                a.distance.cmp(&b.distance)
            } else if a.region != b.region {
                a.region.cmp(&b.region)
            } else {
                a.name.cmp(&b.name)
            }
        });

        for i in 0..n {
            println!("{}", students[i].name);
        }
    }

    Ok(())
}

