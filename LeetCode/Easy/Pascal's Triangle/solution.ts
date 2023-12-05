function generate(numRows: number): number[][] {
  const results = [[1]]
  if (numRows == 1) return results
  function sum(arr: number[]) {
    const temp = []
    for (let i = 1; i < arr.length; i++) {
      temp.push(arr[i] + arr[i - 1])
    }
    return [1, ...temp, 1]
  }
  function ans(current: number[], n: number) {
    if (current.length >= n) return current
    results.push(current)
    const result = ans(sum(current), n) 
    return result
  }
  results.push(ans([1, 1], numRows))
  return results
};
