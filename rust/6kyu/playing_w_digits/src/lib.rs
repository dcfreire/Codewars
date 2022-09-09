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
mod tests;
