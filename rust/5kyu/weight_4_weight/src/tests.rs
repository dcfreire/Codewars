use super::*;

pub(crate) fn testing(s: &str, exp: &str) -> () {
    assert_eq!(order_weight(s), exp)
}

#[test]
pub(crate) fn basics_order_weight() {

    testing("103 123 4444 99 2000", "2000 103 123 4444 99");
    testing("2000 10003 1234000 44444444 9999 11 11 22 123",
        "11 11 2000 10003 22 123 1234000 44444444 9999");

}
