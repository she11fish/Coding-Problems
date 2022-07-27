def ans():
    info = input().split(' ')
    side_length = int(info[0])
    direction = info[1]
    rows = []
    answer = []
    for i in range(side_length):
        nums = input().split(' ')
        rows.append([int(chr) for chr in nums])
    if direction == "right" or direction == "left":
        for row in rows:
            if direction == "right":
                # removing zeroes
                index = 0
                while index < len(row):
                    if row[index] == 0:
                        del row[index]
                    else:
                        index += 1
                # merge numbers
                k = len(row) - 1 
                while (k > 0):
                    if row[k] == row[k-1]:
                        row[k-1] = str(row[k]*2)
                        del row[k]
                    k -= 1
                        
                # add zeroes
                while len(row) != side_length:
                    row.insert(0,0)
            elif direction == "left":
                # removing zeroes
                index = 0
                while index < len(row):
                    if row[index] == 0:
                        del row[index]
                    else:
                        index += 1
                # merge numbers
                k = 0
                while (k < (len(row)-1)):
                    if row[k] == row[k+1]:
                        row[k+1] = str(row[k]*2)
                        del row[k]
                    else:
                        k += 1
                        
                # add zeroes
                while len(row) != side_length:
                    row.insert(len(row), 0)
            answer.append(" ".join([str(e) for e in row]))
             
    if direction == "up":
        # create a list of numbers that form a column
        for j in range(side_length):
            column = []
            for k in range(len(rows)-1,-1,-1):
                column.append(rows[k][j])
            # removing zeroes
            index = 0
            while index < len(column):
                if column[index] == 0:
                    del column[index]
                else:
                    index += 1
            # merge numbers
            k = len(column)-1
            while (k > 0):
                if column[k] == column[k-1]:
                    column[k-1] = str(column[k]*2)
                    del column[k]
                k -= 1

            # add zeroes
            while len(column) != side_length:
                column.insert(0, 0)
            # change column values in rows 
            for i in range(len(column)-1,-1,-1):
                size = len(column)
                rows[i][j] = int(column[(size - i)- 1])
        for row in rows:
            answer.append(" ".join([str(e) for e in row]))
        
    elif direction == "down":
        # create a list of numbers that form a column
        for j in range(side_length):
            column = []
            for k in range(len(rows)):
                column.append(rows[k][j])
            # removing zeroes
            index = 0
            while index < len(column):
                if column[index] == 0:
                    del column[index]
                else:
                    index += 1
            # merge numbers
            k = len(column)-1
            while (k > 0):
                if column[k] == column[k-1]:
                    column[k-1] = str(column[k]*2)
                    del column[k]
                k -= 1

            # add zeroes
            while len(column) != side_length:
                column.insert(0, 0)
            # change column values in rows 
            for i in range(len(column)-1,-1,-1):
                rows[i][j] = int(column[i])
        for row in rows:
            answer.append(" ".join([str(e) for e in row]))
    return answer

T = int(input())
answers = []
for i in range(T):
    answers.append(ans())
for i, answer in enumerate(answers):
    print(f"Case #{i+1}:")
    for arr in answer:
        print(arr)