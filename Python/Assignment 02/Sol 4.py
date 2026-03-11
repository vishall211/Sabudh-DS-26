# Given  an array of N integers, where each value represents the number of chocolates in a 
# packet.  Each packet can have a variable number of chocolates. There are m students, the 
# task is to distribute chocolate packets such that: 
#       a. Each student gets one packet. 
#       b. The difference between the number of chocolates in the packet with the maximum 
#          chocolates and the packet with the minimum chocolates given to the students is Minimum.


arr = list(map(int, input("Enter chocolates in packets: ").split()))
m = int(input("Enter number of students: "))

arr.sort()

n = len(arr)
min_diff = 999999

for i in range(n - m + 1):
    
    diff = arr[i + m - 1] - arr[i]
    
    if diff < min_diff:
        min_diff = diff

print("Minimum Difference is", min_diff)