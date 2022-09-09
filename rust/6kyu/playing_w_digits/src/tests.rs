use super::*;

fn dotest(n: i64, p: i32, exp: i64) -> () {
    println!(" n: {:?};", n);
    println!("p: {:?};", p);
    let ans = dig_pow(n, p);
    println!(" actual:\n{:?};", ans);
    println!("expect:\n{:?};", exp);
    println!(" {};", ans == exp);
    assert_eq!(ans, exp);
    println!("{};", "-");
}

#[test]
fn basic_tests() {
    dotest(89, 1, 1);
    dotest(92, 1, -1);
    dotest(46288, 3, 51);
}
