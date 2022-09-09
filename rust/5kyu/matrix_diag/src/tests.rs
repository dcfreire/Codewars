use super::sum_prod_diags;

fn dotest(m: &[Vec<i8>], expected: i128) {
    let actual = sum_prod_diags(m);
    assert!(
        actual == expected,
        "With matrix = {m:?}\nExpected {expected} but got {actual}"
    )
}

#[test]
fn fixed_tests() {
    dotest(
        &[
            vec![1, 4, 7, 6, 5],
            vec![-3, 2, 8, 1, 3],
            vec![6, 2, 9, 7, -4],
            vec![1, -2, 4, -2, 6],
            vec![3, 2, 2, -4, 7],
        ],
        1098,
    );
    dotest(
        &[
            vec![1, 4, 7, 6],
            vec![-3, 2, 8, 1],
            vec![6, 2, 9, 7],
            vec![1, -2, 4, -2],
        ],
        -11,
    );
    dotest(
        &[
            vec![1, 2, 3, 2, 1],
            vec![2, 3, 4, 3, 2],
            vec![3, 4, 5, 4, 3],
            vec![4, 5, 6, 5, 4],
            vec![5, 6, 7, 6, 5],
        ],
        0,
    );
}
