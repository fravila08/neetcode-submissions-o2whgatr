class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let past = {}
        for (let num of nums){
            if (past[num]){
                return true
            } else {
                past[num] = true
            }
        }
        return false
    }
}
