S = int(input())
W = int(input())

if S > W:
    elapsed_time = W + 24 - S
else:
    elapsed_time = W - S

if S <= 23 and S >= 20 and W >= 6 and W <= 9 and elapsed_time <= 10 and elapsed_time >= 8:
    print("Healthy")
else:
    print("Unhealthy")