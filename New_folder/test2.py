s = input("")

alphabets = list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

def f(x):
    for char in x:
        if char not in alphabets:
            x = x.replace(char,"")
    return x
print(f(s))
