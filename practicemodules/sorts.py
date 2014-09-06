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


def merge_sort(list):
    if len(list) == 1:
        return list

    half = len(list)/2
    list1 = merge_sort(list[:half])
    list2 = merge_sort(list[half:])
    return merge(list1, list2)


def merge(list1, list2):
    i = 0
    j = 0
    finalList = []
    while (i < len(list1) or j < len(list2)):
        if i == len(list1):
            finalList.append(list2[j])
            j = j + 1
            continue

        elif j == len(list2):
            finalList.append(list1[i])
            i = i + 1
            continue

        if (list1[i] < list2[j]):
            finalList.append(list1[i])
            i = i + 1
        else:
            finalList.append(list2[j])
            j = j + 1
    return finalList


if __name__ == '__main__':
    # Test push_list_elements
    # list = push_list_elements(range(10), 8, 9)
    # print list

    # Test merge
    list1 = [0, 3, 5, 8, 34]
    list2 = [2, 10, 12, 45]
    print list1
    print list2
    print "After merge"
    print merge(list1, list2)

    # Test Complete
    # for x in range(3):
    #     list = random.sample(range(100), 20)
    #     print list
    #     print merge_sort(list)
