fn dig_pow(n: i64, p: i32) -> i64 {
    let s = (n
        .to_string()
        .chars()
        .map(|c| c.to_digit(10).unwrap() as i64)
        .enumerate()
        .map(|x| x.1.pow((p as u32) + (x.0 as u32)))
        .sum::<i64>()) as i64;
    if s % n != 0 {-1} else {s/n}
}

#[cfg(test)]
mod tests {
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
}

fn main() {
    println!("Hello, world!");
}
