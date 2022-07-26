def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

print(loop1())
print(loop2())

def loop1Rec(num, odd_sum=0, val=0):
    val = val or 1
    if (val == num):
        return odd_sum
    elif (val % 2 == 1):
        odd_sum += val
    val+=1
    return loop1Rec(num, odd_sum, val)

print(loop1Rec(20))
    
def loop2Rec(num,even_sum=0, val=0):
    val = val or 1
    if (val == num):
        return even_sum
    elif (val % 2 == 0):
        even_sum += val
    val+=1
    return loop2Rec(num, even_sum, val)

print(loop2Rec(20))