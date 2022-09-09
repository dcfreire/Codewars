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

mod tests;
