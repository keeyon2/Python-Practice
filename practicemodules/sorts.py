import random
import pdb


def insertion_sort(list):
    for j in range(1, len(list)):
        i = j - 1
        while list[i] > list[j] and i > 0:
            i = i - 1

        if (i == 0 and list[i] > list[j]):
            list = push_list_elements(list, i, j)
        else:
            list = push_list_elements(list, i + 1, j)
    return list


# list, replace location with List[j], push to J location
def push_list_elements(list, replaceInitialIndex, pushToIndex):

    # Catch if it is size 0 or 1
    if len(list) < 2:
        return list

    templist = list[:]
    i = replaceInitialIndex
    j = pushToIndex

    templist[i] = list[j]

    for x in range(i, j):
        templist[x+1] = list[x]
    return templist

if __name__ == '__main__':
    # Test push_list_elements
    list = push_list_elements(range(10), 8, 9)
    print list

    # Test Complete
    for x in range(3):
        list = random.sample(range(100), 20)
        print list
        print insertion_sort(list)
