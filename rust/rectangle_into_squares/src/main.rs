fn sq_in_rect(lng: i32, wdth: i32) -> Option<Vec<i32>> {
    let mut ret = Vec::new();
    let mut lng = lng;
    let mut wdth = wdth;

    if lng == wdth {
        return None;
    }

    while lng != wdth {
        ret.push(std::cmp::min(lng, wdth));
        if lng > wdth {
            lng -= wdth
        } else {
            wdth -= lng
        }
    }
    ret.push(lng);
    println!("{:?}", ret);
    Some(ret)
}

fn testing(lng: i32, wdth: i32, exp: Option<Vec<i32>>) -> () {
    assert_eq!(sq_in_rect(lng, wdth), exp)
}

#[test]
fn tests_sq_in_rect() {
    testing(5, 3, Some(vec![3, 2, 1, 1]));
    testing(3, 5, Some(vec![3, 2, 1, 1]));
    testing(5, 5, None);
}

fn main() {
    println!("Hello, world!");
}
