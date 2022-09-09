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
mod tests;
