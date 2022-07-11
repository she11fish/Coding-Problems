class Solution {
    solve(nums: Array<number>): number {
        let total_sum: number = nums.reduce((a,b) => a + b)
        let prefix_sum: number = 0
        let suffix_sum: number = total_sum
        for (let i = 0;i<nums.length;i++) {
            prefix_sum = !i ? i : prefix_sum + nums[i-1]  
            suffix_sum = i === nums.length-1 ? 0 : suffix_sum - nums[i]
            if (prefix_sum === suffix_sum) return i
        }
        return -1
    }
}