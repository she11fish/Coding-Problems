/**
 * class LLNode {
 *     val: number;
 *     next: LLNode | null;
 * 
 *     constructor(val: number, next: LLNode | null) {
 *         this.val = val
 *         this.next = next
 *     }
 * }
 */
 class Solution {
    solve(node: LLNode): LLNode {
        let l_nodes = []
        let i = 1
        if (node === null) return node
        let start = node
        while (node) { 
            l_nodes.push(node)
            node = node.next 
        }
        i = l_nodes.length
        console.log(i)
        console.log(node)
        if (i <= 1) return start
        let k = i - 1
        while (k >= 0) {
            l_nodes[k].next = l_nodes[k-1]
            k--
        }
        l_nodes[0].next = null
        node = l_nodes[l_nodes.length-1]
        return node
    }
}