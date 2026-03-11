# Question : Given  an  array  of  positive  and  negative  numbers,  arrange  them  such  that  all  negative integers appear before all the positive integers in the array without using any additional data structure like a hash table, arrays, etc. The order of appearance should be maintained.


nums = list(map(int, input("Enter numbers separated by space: ").split()))

n = len(nums)

for i in range(1, n):

    key = nums[i]

    # if number is negative
    if key < 0:

        j = i - 1

        # shift positive numbers to right
        while j >= 0 and nums[j] > 0:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = key

print("Rearranged array:")
for x in nums:
    print(x, end=" ")