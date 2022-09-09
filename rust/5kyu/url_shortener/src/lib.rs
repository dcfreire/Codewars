use itertools::Itertools;
use std::collections::HashMap;

struct UrlShortener {
    db: HashMap<String, String>,
    rdb: HashMap<String, String>,
    a: Box<dyn Iterator<Item = String>>
}


fn get_permutations(n: i32) -> Box<dyn Iterator<Item = String>> {
    Box::new((0..n)
    .map(|_| (97u8..=122u8).map(|x| x as char))
    .multi_cartesian_product().map(|v| v.iter().join("")))
}

impl UrlShortener {
    fn new() -> Self {
        Self {
            db: HashMap::new(),
            rdb: HashMap::new(),
            a: Box::new(get_permutations(4)
            .chain(
                get_permutations(3)
            )
            .chain(
                get_permutations(2)
            )
            .chain(
                get_permutations(1)
            ))
        }
    }

    fn shorten(&mut self, long_url: &str) -> String {
        if let Some(s) = self.rdb.get(long_url) {
            return s.to_string();
        }
        let short = format!("short.ly/{:}", self.a.next().unwrap());
        self.db.insert(short.clone(), long_url.to_string());
        self.rdb.insert(long_url.to_string(), short.clone());
        short
    }

    fn redirect(&self, short_url: &str) -> String {
        self.db.get(short_url).unwrap().to_string()
    }
}

#[cfg(test)]
mod tests;
