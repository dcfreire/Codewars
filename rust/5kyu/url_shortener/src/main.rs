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
mod tests {
    use super::UrlShortener;
    use crate::assert_valid_short_url;

    #[test]
    fn two_different_urls() {
        let mut url_shortener = UrlShortener::new();

        let short_url_1 =
            url_shortener.shorten("https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e");
        assert_valid_short_url!(&short_url_1);

        let short_url_2 =
            url_shortener.shorten("https://www.codewars.com/kata/5efae11e2d12df00331f91a6");
        assert_valid_short_url!(&short_url_2);

        let short_url_5 = url_shortener.shorten("aaaaaaaaaaaaaaaaaaaaaaaa");
        assert_valid_short_url!(&short_url_5);
        let short_url_6 = url_shortener.shorten("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb");
        assert_valid_short_url!(&short_url_6);
        let short_url_7 = url_shortener.shorten("cccccccccccccccccccccccccccccccccc");
        assert_valid_short_url!(&short_url_7);
        let short_url_8 = url_shortener.shorten("dddddddddddddddddddddddddd");
        assert_valid_short_url!(&short_url_8);

        assert_eq!(
            url_shortener.redirect(&short_url_1),
            "https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e"
        );
        assert_eq!(
            url_shortener.redirect(&short_url_2),
            "https://www.codewars.com/kata/5efae11e2d12df00331f91a6"
        );
        assert_eq!(
            url_shortener.redirect(&short_url_5),
            "aaaaaaaaaaaaaaaaaaaaaaaa"
        );
        assert_eq!(
            url_shortener.redirect(&short_url_6),
            "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        );
        assert_eq!(
            url_shortener.redirect(&short_url_7),
            "cccccccccccccccccccccccccccccccccc"
        );
        assert_eq!(
            url_shortener.redirect(&short_url_8),
            "dddddddddddddddddddddddddd"
        );
    }

    #[test]
    fn same_urls() {
        let mut url_shortener = UrlShortener::new();

        let short_url_1 =
            url_shortener.shorten("https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f");
        assert_valid_short_url!(&short_url_1);

        let short_url_2 =
            url_shortener.shorten("https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f");
        assert_valid_short_url!(&short_url_2);

        assert_eq!(
            short_url_1, short_url_2,
            "Should work with the same long URLs"
        );
        assert_eq!(
            url_shortener.redirect(&short_url_1),
            "https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f",
            "{} should redirect to https://www.codewars.com/kata/5ef9c85dc41b4e000f9a645f",
            &short_url_1,
        );
    }

    #[macro_export]
    macro_rules! assert_valid_short_url {
        ($url:expr) => {
            assert!(
                $url.starts_with("short.ly/"),
                "URL format is incorrect: should start with \"short.ly/\", got: {}",
                $url,
            );

            assert!(
                $url.len() < 14,
                "URL format is incorrect: length should be < 14 characters, got: {}",
                $url,
            );

            // As the URL contains "short.ly/", we can safely index using [9..]
            assert!(
                $url[9..].bytes().all(|b| b.is_ascii_lowercase()),
                "URL format is incorrect: should contain lowercase letters at the end, got: {}",
                $url,
            );
        };
    }
}

fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}

fn main() {
    /*let mut url_shortener = UrlShortener::new();
    let mut c = 0 as i128;
    loop {
        let ret = url_shortener.shorten(&c.to_string());
        println!("{:}", ret);
        c += 1;
        if ret.len() == 14 {
            println!("{c}");
            break;
        }
    }*/
    let a  = (0..=4)
    .map(|_| (97u8..=122u8).map(|x| x as char))
    .multi_cartesian_product()
    .chain(
        (0..=3)
            .map(|_| (97u8..=122u8).map(|x| x as char))
            .multi_cartesian_product(),
    )
    .chain(
        (0..=2)
            .map(|_| (97u8..=122u8).map(|x| x as char))
            .multi_cartesian_product(),
    )
    .chain(
        (0..=1)
            .map(|_| (97u8..=122u8).map(|x| x as char))
            .multi_cartesian_product(),
    ).map(|v| v.iter().join(""));
    print_type_of(&a);
}
