class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let m = new Set(nums)
        return nums.length > m.size
    }
}
