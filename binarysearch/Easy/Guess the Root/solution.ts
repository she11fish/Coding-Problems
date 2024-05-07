class Solution {
    solve(n: number): number {
        let low: number = 0
        let hi: number = n
        let mid: number
        while (low <= hi)
        {
            mid = Math.trunc((low + hi) / 2)
            if (mid ** 2 > n) {
                hi = mid - 1
            }
            if (mid ** 2 < n) {
                low = mid + 1
            } 
            if (mid ** 2 === n) return mid
        }   
        return low - 1
    }
}