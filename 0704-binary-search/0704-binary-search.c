int search(int* nums, int numsSize, int target) {
    int i = 0;
    int j = numsSize - 1;
    while (i <= j){
        int mid = i + ((int)(j - i) / 2);
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            i = mid + 1;
        } else { // nums[mid] > target
            j = mid - 1;
        }
    }
    return -1;
}