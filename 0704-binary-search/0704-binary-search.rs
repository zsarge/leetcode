impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut low = 0;
        let mut high = nums.len()-1;
        while low <= high {
            let midpoint = (low+high)/2;
            if nums[midpoint] == target {
                return midpoint as i32; // convert from usize
            } else if target < nums[midpoint] {
                if midpoint == 0 { // avoid overflow on usize
                    break;
                }
                high = midpoint - 1;
            } else { // target > nums[midpoint]
                low = midpoint + 1;
            }
        }
        return -1;
    }
}