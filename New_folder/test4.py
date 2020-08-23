n = int(input())
def reverse():
    b = n
    rev = 0
    while(b > 0): 
        a = b % 10
        rev = rev * 10 + a
        b = b // 10
    return rev

if n == reverse():
    print("true")
else:
    print("false")


