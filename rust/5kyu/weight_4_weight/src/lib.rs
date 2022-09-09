use itertools::Itertools;

fn order_weight(s: &str) -> String {
    let s: Vec<_> = s.split(" ").collect();
    let mut idx: Vec<_> = s.iter().map(|w| w.chars().map(|c| c.to_digit(10).unwrap() as i32).sum::<i32>()).enumerate().collect();
    idx.sort_by_key(|x| (x.1, s[x.0]));
    idx.iter().map(|x| s[x.0]).intersperse(" ").collect()
}

mod tests;
