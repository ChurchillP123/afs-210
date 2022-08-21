import random
sampleInput = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

def shuffle(list):
    #the time complexity is linear O(n) since it runs through a for loop once
    #space is fine since it uses the same array in place
    for num in list:
        rand = random.randint(0, len(list)-1)
        #pop time complexity is O(n)
        index = list.pop(rand)
        #append time complexity is O(1)
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