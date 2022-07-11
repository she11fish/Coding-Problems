/**
 * class LLNode {
 *   constructor(val, next=null) {
 *     this.val = val
 *     this.next = next
 *   }
 * }
 */
 class Solution {
    solve(node) {
        if (node === null) return true
        const start = node
        let current = node
        let prev = null
        while (current) {
            current.prev = prev
            prev = current
            if (current.next === null) break
            current = current.next
        }
        start.prev = null
        const end = current
        let p1 = start
        let p2 = end
        while (p1 !== p2) {
            if (p1.val !== p2.val) return false 
            p1 = p1.next
            p2 = p2.prev
        }
        return true
    }
}