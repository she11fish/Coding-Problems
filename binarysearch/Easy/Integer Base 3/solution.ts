function log_base_3(target: number): number {
    let low = 0
    let hi = Math.trunc(target/2)
    let mid
    while (low <= hi) {
        mid = Math.trunc((low + hi) / 2)
        if (3 ** mid  === target) return mid
        if (3 ** mid  < target) {
            low = mid + 1
        }
        if (3 ** mid > target) {
            hi = mid - 1
        }
    }
    return low - 1
}

class Solution {
    solve(n: number): string {
        if (!n) return n.toString()
        let occurences = {}
        let exp

        while (n > 0) {
            exp = log_base_3(n)
            occurences[exp] = !(exp in occurences) ? 1 : occurences[exp] + 1
            n = n - (3 ** exp)            
        }

        let digits = []
        let i = 0
        while (i < Object.keys(occurences).length) {
            if (!(i in occurences)) occurences[i] = 0
            digits.splice(i, 0, occurences[i])
            i++
        }
        
        digits.reverse()
        return digits.join('')
    }
}