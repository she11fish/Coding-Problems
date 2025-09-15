import math
# cook your dish here
T = int(input())
i = 0

def ans():
    finish, distance_to_bolt, tiger_accelaration, bolt_speed = [int(n) for n in input().split(" ")]
    bolt_time = finish / bolt_speed
    tiger_time = math.sqrt(((finish + distance_to_bolt) * 2) / tiger_accelaration)
    if bolt_time < tiger_time:
        print("Bolt")
    else:
        print("Tiger")
        
while i < T:
    ans()
    i += 1
