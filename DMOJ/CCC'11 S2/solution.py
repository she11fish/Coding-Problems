N = int(input())

counter = 0
student_answers = []
correct_answers = []
for i in range(N):
    student_answers.append(input())
for i in range(N):
    correct_answers.append(input())
for i in range(N):
    if (student_answers[i] == correct_answers[i]):
        counter += 1 
print(counter)