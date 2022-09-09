use std::collections::HashMap;

fn duplicate_encode(word:&str)->String {
    let mut char_count: HashMap<char, u32> = HashMap::new();
    let word = word.to_lowercase();
    for c in word.chars(){
        char_count.insert(c, *(char_count.get(&c).unwrap_or(&0)) + 1);
    }
    let mut out = String::new();
    for c in word.chars(){
        out.push(if *(char_count.get(&c).unwrap()) > 1 {')'} else {'('});
    }
    out
}

mod tests;