#[cfg(test)]
use super::*;
const ERR_MSG: &str = "\nYour result (left) did not match expected output (right).";

#[test]
fn non_overlapping_intervals() {
    assert_eq!(sum_intervals(&[(1, 5)]), 4, "{}", ERR_MSG);
    assert_eq!(sum_intervals(&[(1, 5), (6, 10)]), 8, "{}", ERR_MSG);
}

#[test]
fn overlapping_intervals() {
    assert_eq!(
        sum_intervals(&[(1, 4), (3, 6), (5, 8), (7, 10), (9, 12)]),
        11,
        "{}",
        ERR_MSG
    );
}

#[test]
fn large_intervals() {
    assert_eq!(
        sum_intervals(&[(-1_000_000_000, 1_000_000_000)]),
        2_000_000_000,
        "{}",
        ERR_MSG
    );
    assert_eq!(
        sum_intervals(&[(0, 20), (-100_000_000, 10), (30, 40)]),
        100_000_030,
        "{}",
        ERR_MSG
    );
}
