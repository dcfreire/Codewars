fn mult_diag(matrix: &[Vec<i8>], ofs: usize, axis: bool) -> (i128, i128) {
    let mut mul = 1_i128;
    let mut rev_mul = 1_i128;
    let len = matrix.len();
    for i in 0..(len - ofs) {
        mul *= matrix[i + (ofs*(!axis as usize))][i+(ofs*(axis as usize))] as i128;
        rev_mul *= matrix[i + (ofs*(!axis as usize))][len - i - 1 - (ofs*(axis as usize))] as i128;
    }
    (mul, rev_mul)
}

fn sum_prod_diags(matrix: &[Vec<i8>]) -> i128 {
    let mut sum_1 = Vec::new();
    let mut sum_2 = Vec::new();
    let n = matrix.len();
    for i in 0..n {
        let res = mult_diag(&matrix, i, false);

        sum_1.push(res.0);
        sum_2.push(res.1);
        if i != 0 {
            let res = mult_diag(&matrix, i, true);
            sum_1.push(res.0);
            sum_2.push(res.1);
        }
    }
    println!("{:?}", sum_2);
    sum_1.iter().sum::<i128>() - sum_2.iter().sum::<i128>()
}

// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
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
}

fn main() {
    println!("Hello, world!");
}
