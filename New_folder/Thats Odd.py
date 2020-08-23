mix = list(input())
def split(mix):
    even_li = []
    odd_li = []
    for i in mix:
        if  int(i) % 2 == 0:
            even_li.append(i)
    return sum(even_li)
        
print(split(mix))

    
    
            
        
