fn tower_builder(n_floors: usize) -> Vec<String> {
    let mut res = Vec::new();
    let len = 2*n_floors-1;
    for i in 0..n_floors {
        let mut line = String::new();
        let n = i*2 + 1;
        for j in 0..len {
            let ch;
            if j >= (len - n)/2 && j < (len + n)/2 {
                ch = '*';
            } else {
                ch = ' ';
            };
            line.push(ch);
        }
        res.push(line);
    }
    res
}
