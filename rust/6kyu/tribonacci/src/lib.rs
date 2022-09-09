

fn tribonacci_rec(signature: &[f64; 3], n: usize, mem: &mut Vec<f64>) -> f64 {
    if mem.len() > n {
        return mem[n];
    }
    let res = tribonacci_rec(signature, n-1, mem) + tribonacci_rec(signature, n-2, mem) + tribonacci_rec(signature, n-3, mem);
    mem.push(res);
    res
}

fn tribonacci(signature: &[f64; 3], n: usize) -> Vec<f64> {
    if n == 0{ return vec![];}
    let mut mem = vec![signature[0], signature[1], signature[2]];
    tribonacci_rec(signature, n-1, &mut mem);
    mem[..n].to_vec()
}

mod tests;