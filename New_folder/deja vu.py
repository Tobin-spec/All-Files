str1 = str(input())
count = {}
str2 = [2,3,4,5,6,7,8,9]
for i in str1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
val = count.values()
set1 = set(count.values())
if set1 == {1}:
    print ('Unique')
else:
    for s in str2:
        if s in val:
            print('Deja Vu')
