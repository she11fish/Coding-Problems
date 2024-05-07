class Solution {
    solve(s: string): string {
        let arr = s.split('')
        let i = 0
        while (i < arr.length - 1) {
            arr[i+1] === arr[i] ? arr.splice(i,1) : i++
        }
        return arr.join('')
    }
}