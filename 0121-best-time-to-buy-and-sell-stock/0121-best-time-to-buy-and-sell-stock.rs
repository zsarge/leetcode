use std::cmp::{min, max};

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max_profit = 0;
        let mut min_price = prices[0];
        
        for price in prices {
            min_price = min(price, min_price);
            let current_profit = price - min_price;
            max_profit = max(current_profit, max_profit);
        }
        
        return max_profit; // could omit `return`
    }
}
