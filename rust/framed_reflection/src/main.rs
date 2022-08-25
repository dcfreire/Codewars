fn mirror(text: &str) -> String {
    let words = text.split(" ");
    let max = match words.clone().map(|w| w.len()).max().ok_or("Err") {
        Ok(res) => res,
        Err(_) => 0,
    };
    let mut ret = Vec::new();
    ret.push("*".repeat(max + 4));
    for word in words {
        let rev = word.chars().rev().collect::<String>();
        let len = word.len();
        let mut line = String::new();
        line.push_str("* ");
        line.push_str(&rev);
        line.push_str(&" ".repeat(max-len + 1));
        line.push_str("*");

        ret.push(line);
    }
    ret.push("*".repeat(max + 4));
    ret.join("\n")
}
// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
    use super::mirror;

    fn dotest(s: &str, expected: &str) {
        let actual = mirror(s);
        assert!(actual == expected,
            "With text = \"{s}\"\nExpected \"{expected}\" but got \"{actual}\"")
    }

    #[test]
    fn fixed_tests() {
        dotest("Hello World", "*********\n* olleH *\n* dlroW *\n*********");
        dotest("Codewars", "************\n* srawedoC *\n************");
        dotest("emosewA !ataK", "***********\n* Awesome *\n* Kata!   *\n***********");
    }
}

fn main() {
    println!("Hello, world!");
}
