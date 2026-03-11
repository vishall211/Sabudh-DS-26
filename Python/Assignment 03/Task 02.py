
# Part A : Tuple Creation and Access

def create_mixed_tuple() :
    num = int(input("Enter an integer : "))
    fl = float(input("Enter a float : "))
    text = input("Enter a string : ")
    boolean_value = input("Enter True or False : ")

    if boolean_value.lower() == "true" :
        boolean_value = True
    else :
        boolean_value = False

    t = (num, fl, text, boolean_value)
    return t


def get_specific_element(numbers_tuple) :
    index = int(input("Enter index to print element : "))

    if index < len(numbers_tuple) :
        return numbers_tuple[index]
    else :
        return "Index out of range"


def fourth_from_end(t) :
    if len(t) < 4 :
        return "Tuple has fewer than 4 elements"
    else :
        return t[-4]



# Part B : Tuple Modification

def add_item_to_tuple(t) :
    new_item = input("Enter item to add to tuple : ")
    new_tuple = t + (new_item,)
    return new_tuple



# Part C : Tuple Conversion

def tuple_to_dictionary(t) :

    if isinstance(t[0], tuple) and len(t[0]) == 2 :
        d = dict(t)
    else :
        d = {}
        for i in range(len(t)) :
            d[i] = t[i]

    return d



# Part D : Tuple Transformation in a List

def replace_last_with_100(tuple_list) :
    new_list = []

    for t in tuple_list :
        if len(t) >= 1 :
            new_tuple = t[:-1] + (100,)
            new_list.append(new_tuple)

    return new_list



if __name__ == "__main__" :

    # Part A : Tuple Creation and Access
    mixed_tuple = create_mixed_tuple()
    print("Mixed tuple :", mixed_tuple)

    numbers = tuple(map(int, input("Enter at least 5 numbers separated by space : ").split()))
    print("Specific element :", get_specific_element(numbers))

    user_tuple = tuple(input("Enter tuple elements separated by space : ").split())
    print("4th element from end :", fourth_from_end(user_tuple))

    print("\n\n")


    # Part B : Tuple Modification
    original_tuple = tuple(input("Enter tuple elements separated by space : ").split())
    updated_tuple = add_item_to_tuple(original_tuple)

    print("Original tuple :", original_tuple)
    print("New tuple after adding item :", updated_tuple)

    print("\n\n")


    # Part C : Tuple Conversion
    tuple_input = eval(input("Enter a tuple (example ((\"a\",1),(\"b\",2)) or (10,20,30)) : "))
    dictionary_result = tuple_to_dictionary(tuple_input)
    print("Converted dictionary :", dictionary_result)

    print("\n\n")


    # Part D : Tuple Transformation in a List
    list_input = eval(input("Enter list of tuples like [(10,20,40),(40,50,60)] : "))
    result = replace_last_with_100(list_input)
    print("Updated list :", result)