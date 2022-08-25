fn clean_string(s: &str) -> String {
    let mut ret = String::new();
    let rev = s.chars().rev();
    let mut del = 0;
    for c in rev{
        if c == '#' {
            del += 1;
            continue;
        }
        if del > 0 {
            del -= 1;
            continue;
        }
        if del == 0{
            ret.push(c);
        }

    }
    ret.chars().rev().collect::<String>()
}

fn main() {
    println!("Hello, world!");
}
