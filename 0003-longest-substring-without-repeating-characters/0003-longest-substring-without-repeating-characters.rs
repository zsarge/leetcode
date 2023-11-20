use std::cmp::max;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut max_length = 0;
        let mut right = 0;
        let mut left = 0;
        let chars: Vec<char> = s.chars().collect();
        
        while right < s.len() {
            let mut first = right;
            for i in left..right {
                if chars[i] == chars[right] {
                    first = i;
                    break;
                }
            }
            if first != right {
                left = first + 1;
            }
            max_length = max(max_length, right - left + 1);
            right += 1;
        }

        return max_length as i32;
    }    
}
