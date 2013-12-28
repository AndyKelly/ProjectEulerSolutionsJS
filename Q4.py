def is_palindrome(number):
    digitArray = str(number)
    if len(digitArray) % 2 != 0:
        #odd remove middle element as it wont impact palindropicness
        digitArray = digitArray[0:len(digitArray)/2] + digitArray[len(digitArray)/2 + 1:]
    length = len(digitArray)
    leftIndex = 0
    rightIndex = length -1
    while leftIndex < length -1 and rightIndex > 0:
        if digitArray[leftIndex] != digitArray[rightIndex]:
            return False
        leftIndex += 1
        rightIndex -= 1
    return True

upperLimit = 999
largestAnswer = 0
x = 0
y = 0
while x <= upperLimit:
    while y <= upperLimit:
        product = x * y
        if is_palindrome(product) and product > largestAnswer:
            largest = product
        y += 1
    x += 1
    y = 0 

print largest


