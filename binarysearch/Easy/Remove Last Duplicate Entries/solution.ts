class Solution {
    solve(nums: Array<number>): Array<number> { 

       if (!nums.length) return nums

       let occurences = {}
       for (let e of nums) !(e in occurences) ? occurences[e] = 1 : occurences[e]++ 

       let i: number = nums.length - 1
       let check: Array<number> = []
       while (i > -1)
       {
           if (occurences[nums[i]] > 1 && !check.includes(nums[i])) 
           {
                check.push(nums[i])
                nums.splice(i,1)
           } else {
               i--
           }
       }
       return nums
    }
}