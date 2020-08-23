input_string = str(input())
nums = "0","1","2","3","4","5","6","7","8","9","10"
nums_letters = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
def no_numerals(input_string):
    for i in nums:
        if i in input_string:
            input_string.replace(i,nums_letters[input_string.index(i) - 1])
            print(input_string)

no_numerals(input_string)
