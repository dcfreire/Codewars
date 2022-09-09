use itertools::sorted;
use itertools::equal;

fn comp(a: Vec<i64>, b: Vec<i64>) -> bool {
    equal(sorted(a.into_iter().map(|x| x.pow(2))), sorted(b))
}

mod tests;