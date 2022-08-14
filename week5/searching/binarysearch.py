def binarySearch(sortedList, searchTerm):
    low = 0
    high = len(sortedList)-1
    mid = len(sortedList)//2

    while low <= high:
        mid = low + (high - low)//2
        if sortedList[mid] == searchTerm:
            return True
        elif sortedList[mid] < searchTerm:
            low = mid + 1
        else:
            high = mid - 1
    return False
    
list1 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
list2 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

print(binarySearch(list1, 31))
print(binarySearch(list1, 77))
print(binarySearch(list2, "Delta"))