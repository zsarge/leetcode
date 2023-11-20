use std::collections::HashSet;
use std::cmp::max;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut char_set = HashSet::new();
        let mut left_index = 0;
        let mut max_substring = 0;
        
        for (right_index, right) in s.chars().enumerate() {
            while char_set.contains(&right) {
                char_set.remove(&s.chars().nth(left_index).unwrap());
                left_index += 1;
            }
            char_set.insert(right);
            max_substring = max(max_substring, right_index - left_index + 1);
        }
        return max_substring as i32;
    }    
}
