function check_palindrome(s: string, start: number, end: number) {
    while (start < end) {
        if (s[start] !== s[end]) {
            return false
        }
        start++;
        end--;
    }
    return true
}


function longestPalindrome(s: string): string {
    let start = 0
    let end = s.length - 1
    let result: string = s[0]
    
    if (s.length === 1) {
        return s
    }
    
    while (start !== s.length - 1) {
        while (start !== end) {
            if (
                s[start] === s[end] 
                && check_palindrome(s, start, end) 
                && result.length < s.substring(start, end + 1).length
            ) {
                result = s.substring(start, end + 1) 
                break
            }
            end--;
        }
        start++;
        end = s.length - 1
    } 
    return result
};