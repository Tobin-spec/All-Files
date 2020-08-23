sentence = input().split()
average = sum(len(words) for words in sentence) // len(sentence)

if average == 3:
    print (average)
else:
    print (average + 1)

    
    
