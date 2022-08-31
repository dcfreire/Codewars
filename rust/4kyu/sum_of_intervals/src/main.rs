use std::collections::VecDeque;
use itertools::Itertools;

fn merge_overlap(a: (i32, i32), b: (i32, i32)) -> Option<(i32, i32)>{
    if (a.1 <= b.0) || (a.0 >= b.1) {
        return None;
    }
    Some((if a.0 > b.0 {b.0} else {a.0}, if a.1 > b.1 {a.1} else {b.1}))
}

fn sum_intervals(intervals: &[(i32, i32)]) -> i32 {
    let mut queue = VecDeque::from_iter(
        intervals.iter().cloned().sorted_by(|a, b| a.1.cmp(&b.1))
    );
    let mut final_intervals = Vec::new();
    while queue.len() > 1 {
        let mut cur = queue.pop_back().unwrap();
        let it: Vec<_> = queue.iter().cloned().enumerate().rev().collect();
        for (i, elem) in it {
            match merge_overlap(cur, elem) {
                Some(t) => {
                    cur = t;
                    queue.remove(i);
                },
                None => ()
            }
        }
        final_intervals.push(cur);
    }
    match queue.pop_front() {
        Some(v) => final_intervals.push(v),
        None => ()
    }
    final_intervals.iter().fold(0,|acc, x| acc + (x.1 - x.0))
}

// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod sample_tests {
    use super::*;
    const ERR_MSG: &str = "\nYour result (left) did not match expected output (right).";

    #[test]
    fn non_overlapping_intervals() {
        assert_eq!(sum_intervals(&[(1, 5)]), 4, "{}", ERR_MSG);
        assert_eq!(sum_intervals(&[(1, 5), (6, 10)]), 8, "{}", ERR_MSG);
    }

    #[test]
    fn overlapping_intervals() {
        assert_eq!(sum_intervals(&[(1, 4), (3, 6), (5, 8), (7, 10), (9, 12)]), 11, "{}", ERR_MSG);
    }

    #[test]
    fn large_intervals() {
        assert_eq!(sum_intervals(&[(-1_000_000_000, 1_000_000_000)]), 2_000_000_000, "{}", ERR_MSG);
        assert_eq!(sum_intervals(&[(0, 20), (-100_000_000, 10), (30, 40)]), 100_000_030, "{}", ERR_MSG);
    }
}

fn main() {
    println!("Hello, world!");
}
