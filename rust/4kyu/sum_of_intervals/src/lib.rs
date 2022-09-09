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

mod tests;