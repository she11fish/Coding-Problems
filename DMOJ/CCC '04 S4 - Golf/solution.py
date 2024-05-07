import sys
sys.setrecursionlimit(5000)
def ans(target, clubs, memo={}):
    if target == 0:
        return 0
    if target < 0:
        return 100000
    if target in memo:
        return memo[target]
    result = 100000
    for club in clubs:
        if (target - club) < 0:
            current_result = 100000
        else:
            current_result = ans(target-club, clubs)
        if result > current_result:
            result = current_result
    if target in memo:
        return memo[target]
    memo[target] = result + 1
    return result + 1
    
    # memo[target] = min(ans(target-66, club), ans(target-33, club), ans(target-1, club)) + 1
    # return memo[target]
    
distance = int(input())
n = int(input())
clubs = []
for i in range(n):
    clubs.append(int(input()))
solution = ans(distance, clubs)
if solution >= 100000:
    print("Roberta acknowledges defeat.")
else:
    print(f"Roberta wins in {solution} strokes.")
# result = []
# for club in clubs:
#     ans(club, distance, result)