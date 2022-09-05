// https://leetcode.com/problems/remove-duplicates-from-sorted-array

#include <iostream>
#include <vector>

using namespace std;

class Solution {
   public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() < 2)
            return nums.size();

        int endpoint = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[i - 1]) {
                nums[endpoint] = nums[i];
                endpoint++;
            }
        }

        return endpoint;
    }
};

int main() {
    Solution sol = Solution();

    // vector<int> nums = {0,0,1,1,1,2,2,3,3,4};
    vector<int> nums = {1, 1, 2};

    int end = sol.removeDuplicates(nums);

    for (size_t i = 0; i < end; i++) {
        cout << nums[i] << endl;
    }
}
