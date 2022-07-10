function is_in_check(num: number, check: Array<number>): Boolean { 
    if (!check.length) return false  
    for (let e of check) if (e === num) return true 
    return false
}

class Solution {
    solve(nums: Array<number>): Array<number> { 

       if (!nums.length) return nums

       let occurences: Object = {}
       for (let e of nums) !(e in occurences) ? occurences[e] = 1 : occurences[e]++ 

       let i: number = nums.length - 1
       let check: Array<number> = []

       while (i > -1)
       {
           if (occurences[nums[i]] > 1 && !is_in_check(nums[i], check)) 
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