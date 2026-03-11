
# Part A : Sorting a Dictionary by Value
def sort_by_value(d) :
    asc = dict(sorted(d.items(), key = lambda x : x[1]))
    desc = dict(sorted(d.items(), key = lambda x : x[1], reverse = True))
    return asc, desc

# Part B : Iterating Through a Dictionary
def iterate_dictionary(d) :

    keys_list = []
    values_list = []
    pairs_list = []

    for k in d.keys() :
        keys_list.append(k)

    for v in d.values() :
        values_list.append(v)

    for k, v in d.items() :
        pairs_list.append((k, v))

    return keys_list, values_list, pairs_list


# Part C : Merging Dictionaries
def merge_dictionaries(d1, d2) :
    merged = d1.copy()

    for k, v in d2.items() :
        merged[k] = v
    return merged


# Part D : Aggregation Operations
def sum_of_values(d) :

    if len(d) == 0 :
        return "Dictionary is empty"
    total = 0

    for v in d.values() :
        total += v
    return total


def product_of_values(d) :

    if len(d) == 0 :
        return "Dictionary is empty"

    product = 1
    for v in d.values() :
        product = product * v

    return product



# Part E : Sorting by Key
def sort_by_key(d) :
    sorted_dict = dict(sorted(d.items()))
    return sorted_dict


# Part F : Removing Duplicate Values

def remove_duplicate_values(d) :

    seen_values = []
    new_dict = {}

    for k, v in d.items() :
        if v not in seen_values :
            new_dict[k] = v
            seen_values.append(v)

    return new_dict



if __name__ == "__main__" :
    d = eval(input("Enter a dictionary : "))

    # Part A
    asc, desc = sort_by_value(d)
    print("Ascending order :", asc)
    print("Descending order :", desc)
    print("\n\n")


    # Part B
    keys_list, values_list, pairs_list = iterate_dictionary(d)
    print("Keys :", keys_list)
    print("Values :", values_list)
    print("Key-Value pairs :", pairs_list)
    print("\n\n")


    # Part C
    d2 = eval(input("Enter second dictionary : "))
    merged = merge_dictionaries(d, d2)
    print("Merged dictionary :", merged)
    print("\n\n")


    # Part D
    print("Sum of values :", sum_of_values(d))
    print("Product of values :", product_of_values(d))
    print("\n\n")


    # Part E
    print("Sorted dictionary by key :", sort_by_key(d))
    print("\n\n")

    # Part F
    print("Dictionary after removing duplicate values :", remove_duplicate_values(d))
    print("\n\n")