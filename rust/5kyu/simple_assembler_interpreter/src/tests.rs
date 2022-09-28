// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html
use std::collections::HashMap;

#[cfg(test)]
use super::*;

macro_rules! map {
        ($($key:expr => $value:expr),*) => {{
            let mut map = HashMap::new();
            $(
                map.insert($key.to_string(), $value);
            )*
            map
        }};
    }

#[test]
fn short_tests() {
    let program = vec!["mov a 5", "inc a", "dec a", "dec a", "jnz a -1", "inc a"];
    let expected = map! { "a" => 1 };
    compare_registers(expected, simple_assembler(program));

    let program = vec![
        "mov c 12",
        "mov b 0",
        "mov a 200",
        "dec a",
        "inc b",
        "jnz a -2",
        "dec c",
        "mov a b",
        "jnz c -5",
        "jnz 0 1",
        "mov c a",
    ];
    let expected = map! { "a" => 409600, "c" => 409600, "b" => 409600};
    compare_registers(expected, simple_assembler(program));
}

fn compare_registers(expected: HashMap<String, i64>, actual: HashMap<String, i64>) {
    let result = expected
        .iter()
        .all(|(key, value)| actual.get(key).map(|v| v == value).unwrap_or(false));
    assert!(
        result,
        "Expected the registers to be like that:\n{:#?}\n\nBut got this:\n{:#?}\n",
        expected, actual
    )
}
