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
