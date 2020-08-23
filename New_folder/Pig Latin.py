
x = ""

for pig_latin in input().split():
    x += pig_latin[1:] + pig_latin[0:1] + "ay "

print(x)
    
