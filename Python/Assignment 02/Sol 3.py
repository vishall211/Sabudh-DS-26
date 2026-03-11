# Given  an  array  of  N integers and a number K, the task is to find the number of pairs of integers in the array whose sum is equal to K.

arr = list(map(int, input("Enter numbers separated by space : ").split()))
k = int(input("Enter the sum value : "))

count = 0
n = len(arr)

for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == k:
            count += 1

print("Number of pairs :", count)