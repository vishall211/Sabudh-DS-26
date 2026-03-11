# Question : Rotate a matrix by 90 degree in clockwise direction.

n = int(input("Enter size of matrix : "))

matrix = []

print("Enter matrix rows : ")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Step 1: transpose karna hai
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Step 2: reverse each row
for i in range(n):
    matrix[i].reverse()

print("Rotated matrix : ")
for row in matrix:
    print(row)