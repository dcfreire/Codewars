#[cfg(test)]

use crate::next_smaller_number;

#[test]
fn example() {
    assert_eq!(Some(12), next_smaller_number(21));
    assert_eq!(Some(790), next_smaller_number(907));
    assert_eq!(Some(513), next_smaller_number(531));
    assert_eq!(None, next_smaller_number(1027));
    assert_eq!(Some(414), next_smaller_number(441));
}
