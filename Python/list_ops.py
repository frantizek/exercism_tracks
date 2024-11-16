def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    flattened_list = []
    for list in lists:
        for item in list:
            flattened_list.append(item)
    return flattened_list
        

def filter(function, my_list):
    new_filtered_list = []
    for item in my_list:
        if function(item):
            new_filtered_list.append(item)
    return new_filtered_list


def length(list):
    length_of_the_list = 0
    for item in list:
        length_of_the_list += 1
    return length_of_the_list
        

def map(function, my_list):
    new_mapped_list = []
    for item in my_list:
        new_mapped_list.append(function(item))
    return new_mapped_list


def foldl(function, list, initial):
    final_value = initial
    for item in list:
        final_value = function(final_value, item)
    return final_value


def foldr(function, list, initial):
    if len(list) == 0:
        return initial
    head_of_the_list = list[0]
    tail_of_the_list = list[1::]
    return function(foldr(function, tail_of_the_list, initial), head_of_the_list) 


def reverse(list):
    reversed_list = []
    list.reverse()
    for item in list:
        reversed_list.append(item)
    return reversed_list
