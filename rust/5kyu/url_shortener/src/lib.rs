use itertools::Itertools;
use std::collections::HashMap;

struct UrlShortener {
    db: HashMap<String, String>,
    rdb: HashMap<String, String>,
    perms: Box<dyn Iterator<Item = String>>
}

struct Permutations {
    perms: Box<dyn Iterator<Item = String>>
}

impl Iterator for Permutations {
    type Item = String;
    fn next(&mut self) -> Option<Self::Item> {
        self.perms.next()
    }
}

impl Permutations {
    fn get_perm(n: i32) -> impl Iterator<Item = String> {
        (0..n)
        .map(|_| (97u8..=122u8).map(|x| x as char))
        .multi_cartesian_product().map(|v| v.iter().join(""))
    }

    fn new(n: i32) -> Self {
        Self {
            perms: Box::new((1..=n).flat_map(|i| Permutations::get_perm(i)))
        }
    }
}

impl UrlShortener {
    fn new() -> Self {
        Self {
            db: HashMap::new(),
            rdb: HashMap::new(),
            perms: Box::new(Permutations::new(4))
        }
    }

    fn shorten(&mut self, long_url: &str) -> String {
        if let Some(s) = self.rdb.get(long_url) {
            return s.to_string();
        }
        let short = format!("short.ly/{:}", self.perms.next().unwrap());
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
