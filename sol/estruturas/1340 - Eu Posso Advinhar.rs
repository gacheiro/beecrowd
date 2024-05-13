// 1340 Eu Posso Adivinhar a Estrutura de Dados!
// https://judge.beecrowd.com/pt/problems/view/1340

use std::io;
use std::collections::BinaryHeap;

fn main() -> io::Result<()> {
    let stdin = io::stdin();

    loop {
        let mut buffer = String::new();
        match stdin.read_line(&mut buffer) {
            Ok(0) => break,
            _     => (),
        }

        let n: usize = buffer.trim().parse().unwrap();
        let (mut is_stack, mut is_queue, mut is_pqueue) = (true, true, true);
        let (mut stack, mut queue, mut pqueue) = (Vec::new(),
                                                  Vec::new(),
                                                  BinaryHeap::new());
        for _ in 0..n {
            buffer.clear();
            stdin.read_line(&mut buffer)?;
            let data: Vec<u32> = buffer.split_whitespace()
                                       .map(|x| x.parse().unwrap())
                                       .collect();

            if data[0] == 1 {
                stack.push(data[1]);
                queue.push(data[1]);
                pqueue.push(data[1]);
                continue;
            }

            is_stack &= match stack.pop() {
                Some(x) if x == data[1] => true,
                _ => false,
            };

            is_queue &= match queue.remove(0) {
                x if x == data[1] => true,
                _ => false,
            };

            is_pqueue &= match pqueue.pop() {
                Some(x) if x == data[1] => true,
                _ => false,
            };
        }

        if is_stack && !is_queue && !is_pqueue {
            println!("stack");
        } else if !is_stack && is_queue && !is_pqueue {
            println!("queue");
        } else if !is_stack && !is_queue && is_pqueue {
            println!("priority queue");
        } else if !is_stack && !is_queue && !is_pqueue {
            println!("impossible");
        } else {
            println!("not sure");
        }
    }

    Ok(())
}

