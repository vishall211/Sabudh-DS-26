
# Part A : Integer List Operations

def multiply_list(numbers) :
    result = 1
    for num in numbers :
        result = result * num
    return result


def find_largest(numbers) :
    largest = numbers[0]
    for num in numbers :
        if num > largest :
            largest = num
    return largest


def find_smallest(numbers) :
    smallest = numbers[0]
    for num in numbers :
        if num < smallest :
            smallest = num
    return smallest


def remove_duplicates(numbers) :
    new_list = []
    for num in numbers :
        if num not in new_list :
            new_list.append(num)
    return new_list


def check_empty(numbers) :
    if len(numbers) == 0 :
        return True
    else :
        return False


def largest_odd(numbers) :
    odd_numbers = []

    for num in numbers :
        if num % 2 != 0 :
            odd_numbers.append(num)

    if len(odd_numbers) == 0 :
        return "No odd numbers found"

    largest = odd_numbers[0]

    for num in odd_numbers :
        if num > largest :
            largest = num

    return largest


def remove_indices(numbers) :
    indices = [0,4,5]

    indices.sort(reverse = True)

    for i in indices :
        if i < len(numbers) :
            numbers.pop(i)

    return numbers



# Part B : Tuple List Sorting

def sort_tuples(tuple_list) :
    tuple_list.sort(key = lambda x : x[-1])
    return tuple_list



# Part C : Word List Analysis

def count_lowercase(words) :
    count = 0

    for word in words :
        for ch in word :
            if ch.islower() :
                count += 1

    return count



# Part D : Consecutive Element Extraction

def extract_k_consecutive(numbers, k) :
    result = []
    i = 0

    while i < len(numbers) :
        count = 1

        while i + 1 < len(numbers) and numbers[i] == numbers[i + 1] :
            count += 1
            i += 1

        if count == k :
            result.append(numbers[i])

        i += 1

    return result



if __name__ == "__main__" :

    # Input for Part A
    nums = list(map(int, input("\nEnter integers separated by space : ").split()))

    if not check_empty(nums) :

        print("Product of list :", multiply_list(nums))
        print("Largest number :", find_largest(nums))
        print("Smallest number :", find_smallest(nums))
        print("List without duplicates :", remove_duplicates(nums))
        print("Largest odd number :", largest_odd(nums))
        print("List after removing index 0,4,5 :", remove_indices(nums.copy()))

    else :
        print("The list is empty")


    # Input for Part B
    tuple_input = input("\n\nEnter tuples like (1,3) (2,1) (4,2) : ")
    tuple_list = eval("[" + tuple_input.replace(" ", ",") + "]")

    print("Sorted tuples :", sort_tuples(tuple_list))


    # Input for Part C
    words = input("\n\nEnter words separated by space : ").split()
    print("Total lowercase letters :", count_lowercase(words))


    # Input for Part D
    nums2 = list(map(int, input("\n\nEnter integers for consecutive check : ").split()))
    k = int(input("Enter value of k : "))

    print("Elements appearing exactly k times consecutively :", extract_k_consecutive(nums2, k))
    print("\n\nEnd of program")