// assume a sorted array
int search(int* nums, int numsSize, int target) {
    int *i = nums;
    int *j = nums + (numsSize-1);
    while (i <= j) {
        int *midpoint = i + ((int)(j-i) / 2);
        if (*midpoint == target) {
            return (int)(midpoint-nums);
        } else if (*midpoint > target) {
            j = midpoint - 1;
        } else { // *midpoint < target
            i = midpoint + 1;
        }
    }
    return -1;
}
