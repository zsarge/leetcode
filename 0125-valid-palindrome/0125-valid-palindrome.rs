impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let filtered = s.chars()
            .filter_map(|c| 
                if c.is_alphanumeric() {
                    Some(c.to_ascii_lowercase())
                } else {
                    None
                }
            ).collect::<String>();
        filtered == filtered.chars().rev().collect::<String>()
    }
}