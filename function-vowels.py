# function for vowels

from collections import Counter



def count_vowls(sentence):
    sentence = sentence.lower()
    arr=[]
    count_arr = 0
    vowels ="a","i","o","u","e"
    for i in sentence:
        if(i in vowels):
            print(i) 
        
            arr.append(i)  

    count_arr = Counter(arr)
    return count_arr

sentence =input("Enter the sentence") 
s = count_vowels(sentence)
print(s)