def check_rsa(n):
    factors = 0
    for i in range(1, n+1):
        if n % i == 0:
            factors += 1
    if factors == 4:
        return 1
    return 0
low = int(input())
high = int(input())

counter = 0

for i in range(low, high+1):
    counter += check_rsa(i)
print(f"The number of RSA numbers between {low} and {high} is {counter}")
