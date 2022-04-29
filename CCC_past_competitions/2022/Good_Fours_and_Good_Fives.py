# Graphing the equation 4x + 5y = N where it becomes y = (N-4x)/5
# if x as a whole number has y as a whole number then counter++

def find_4s_and_5s(N):
	counter = 0
	x = 0
	while (N-4*x)/5 >= 0:
		if (N-4*x) % 5 == 0:
			counter+=1
		x += 1 
	return counter
N = int(input())
print(find_4s_and_5s(N))
