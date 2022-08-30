fn next_smaller_number(n: u64) -> Option<u64> {
    let mut digits: Vec<char> = n.to_string().chars().rev().collect();
    for i in 0..(digits.len() - 1) {
        if digits[i] < digits[i+1] {
            let mut imin = i;
            let mut c = 0;

            while c <= i {
                if digits[imin] < digits[c] && digits[c] < digits[i+1]{
                    imin = c;
                }
                c += 1;
            }
            digits.swap(imin, i + 1);
            digits[0..=i].sort();
            break;
        }
    }
    let ret = digits.iter().rev().collect::<String>().parse::<u64>().unwrap();
    if ret == n || digits.last().unwrap() == &'0' {
        return None;
    }
    Some(ret)

}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example() {
        assert_eq!(Some(12), next_smaller_number(21));
        assert_eq!(Some(790), next_smaller_number(907));
        assert_eq!(Some(513), next_smaller_number(531));
        assert_eq!(None, next_smaller_number(1027));
        assert_eq!(Some(414), next_smaller_number(441));
    }
}

fn main() {
    println!("Hello, world!");
}
