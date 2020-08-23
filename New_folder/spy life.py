msg = input('')
alphabets = list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
def f(x):
    for char in x:
        if char not in alphabets:
            x = x.replace(char,'')
    return x
print(f(msg[::-1]))
