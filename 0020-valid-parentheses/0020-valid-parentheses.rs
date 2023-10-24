impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();
        
        for c in s.chars() {
            let closes = match c {
                   ')' => '(',
                   ']' => '[',
                   '}' => '{',
                   _ => 'x' // has no opening 
            };
            match stack.last() {
                Some(&paren) if paren == closes => {
                    stack.pop();
                },
                _ => {
                    stack.push(c);
                }
            }
        }
        
        return stack.is_empty();
    }
}