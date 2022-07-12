class Solution {
    solve(coordinates: Array<Array<number>>): boolean {
        if (coordinates.length <= 1) return false
        let ratio = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]) 
        let next_ratio
        for (let i = 0;i < coordinates.length - 1;i++) {
            next_ratio = (coordinates[i+1][1] - coordinates[i][1]) / (coordinates[i+1][0] - coordinates[i][0]) 
            if (next_ratio !== ratio) return false
        }
        return true
    }
}