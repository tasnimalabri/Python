
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = input(" Enter the text : ")
 

 
print("The reversed string is : ", end="")
print(reverse(s))