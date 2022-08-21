import random
sampleInput = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

def shuffle(list):
    #the time complexity is linear O(n) since it runs through a for loop once
    for num in list:
        rand = random.randint(0, len(list)-1)
        index = list.pop(rand)
        list.append(index)
    return list

print("Before Shuffle:")
print(sampleInput)

print("Shuffled:")
print(shuffle(sampleInput))
print(shuffle(sampleInput))
print(shuffle(sampleInput))
print(shuffle(sampleInput))
print(shuffle(sampleInput))