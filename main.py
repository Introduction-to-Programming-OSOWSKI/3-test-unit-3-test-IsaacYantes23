def countB(w):
    letter = w[0]
    for i in range(0, len(w)):
        letter + w[i]
        if w[i] == "b":
            return w[i] + letter

        else:
            return "none"
print(countB("baseball"))

def removeLast(w):
    letter = w
    for i in range(0, len(w)-1):
        letter == w
        return letter
print(removeLast("winter"))

def sumBetweenOdd(x,y):
    number = x % y
    for i in range(x,y):
        number + i
        return number
print(sumBetweenOdd(4,13))

def firstLast(w):
    if w[0] == w[3]:
        return True
    else:
        return False

print(firstLast("roar"))

