use std::collections::HashSet;
use std::cmp::max;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut char_set = HashSet::new();
        let mut left_index = 0;
        let mut max_substring = 0;
        let chars: Vec<char> = s.chars().collect(); // use Vec for O(1) lookup
        
        for right_index in 0..s.len() {
            let right = chars[right_index];
            while char_set.contains(&right) {
                char_set.remove(&chars[left_index]);
                left_index += 1;
            }
            char_set.insert(right);
            max_substring = max(max_substring, right_index - left_index + 1);
        }
        return max_substring as i32;
    }    
}
