use itertools::Itertools;

fn order_weight(s: &str) -> String {
    let s: Vec<_> = s.split(" ").collect();
    let mut idx: Vec<_> = s.iter().map(|w| w.chars().map(|c| c.to_digit(10).unwrap() as i32).sum::<i32>()).enumerate().collect();
    idx.sort_by_key(|x| (x.1, s[x.0]));
    idx.iter().map(|x| s[x.0]).intersperse(" ").collect()
}

fn testing(s: &str, exp: &str) -> () {
    assert_eq!(order_weight(s), exp)
}

#[test]
fn basics_order_weight() {

    testing("103 123 4444 99 2000", "2000 103 123 4444 99");
    testing("2000 10003 1234000 44444444 9999 11 11 22 123",
        "11 11 2000 10003 22 123 1234000 44444444 9999");

}

fn main() {
    println!("Hello, world!");
}
