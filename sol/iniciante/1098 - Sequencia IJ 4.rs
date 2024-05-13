// 1098 - Sequencia IJ 4
// https://judge.beecrowd.com/pt/problems/view/1098

use std::io;

fn main() -> io::Result<()> {
    let mut x: f32 = 0.0;
    while x < 2.2 {
        for y in 1..=3 {
            if x.fract() > 0.1 {
                println!("I={:.1} J={:.1}", x, x + y as f32);
            } else {
                println!("I={:.0} J={:.0}", x, x + y as f32);
            }
        }
        x += 0.2;
    }

    Ok(())
}
