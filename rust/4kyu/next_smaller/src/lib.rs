mod tests;

fn next_smaller_number(n: u64) -> Option<u64> {
    let mut digits: Vec<char> = n.to_string().chars().rev().collect();
    for i in 0..(digits.len() - 1) {
        if digits[i] < digits[i + 1] {
            let imax = digits[0..=i]
                .iter()
                .enumerate()
                .fold((i, &digits[i]),|acc, x| {
                    if acc.1 < x.1 && x.1 < &digits[i + 1] {
                        x
                    } else {
                        acc
                    }
                }).0;
            digits.swap(imax, i + 1);
            digits[0..=i].sort();
            break;
        }
    }
    let ret = digits
        .iter()
        .rev()
        .collect::<String>()
        .parse::<u64>()
        .unwrap();
    if ret == n || digits.last().unwrap() == &'0' {
        return None;
    }
    Some(ret)
}
