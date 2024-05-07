n = input()
start = int(n.split(" ")[0])
days = int(n.split(" ")[1])

print("Sun Mon Tue Wed Thr Fri Sat")

day_shift = " " * 3
start_shift = " " * 2
longer_than_nine_days_shift = " " * 2 
print((start_shift * 2 * (start - 1)) + start_shift, end="")
if start != 1:
    for i in range(1, days + 1):
        if i == days:
            print(i)
            continue
        if i % 7 == (7 - (start - 1)):
            print(f"{i}") 
            if i >= 9:
                print(" ", end="")
            else:
                print(start_shift, end="")
        elif i >= 9:
            print(f"{i}" + start_shift, end="")
        else:
            print(f"{i}" + day_shift, end="")
else:
    for i in range(1, days + 1):
        if i == days:
            print(i)
            continue
        if i % 7 == 0:
            print(f"{i}") 
            if i >= 9:
                print(" ", end="")
            else:
                print(start_shift, end="")
        elif i >= 9:
            print(f"{i}" + start_shift, end="")
        else:
            print(f"{i}" + day_shift, end="")