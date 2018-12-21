numData = [49, 51, 0, 0]       # The numbers can be between 48 and 58
tmpArray = []

for i in numData:
    if i > 47 and i < 59:
        i -= 48    # normalize to 0-9
        list.append(tmpArray, i)
print(tmpArray)

length = len(tmpArray)
final = 0
for i in tmpArray:
    final += i*10**(length-1)
    length -= 1

print(final)
