class Solution {
    solve(n: string): number {
        while (n.length !== 1) {
            let sum = 0 
            for (let digit of String(n)) sum += Number(digit)
            n = String(sum)
        }
        return Number(n)
    }
}