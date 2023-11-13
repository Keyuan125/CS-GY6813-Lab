# Naive solution: 
# Traverse the list
# For each element in the list, traverse the the list after the element,
# if the second element equals to the first one, set the second one to 0 
def remove_naive(input_list):
    length = len(input_list)
    if length <= 1: return input_list
    else:
        for i in range(length-1):
            first = input_list[i]
            if first == 0:
                continue
            for j in range(i+1, length):
                if input_list[j] == first:
                    input_list[j] = 0
    