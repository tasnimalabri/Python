string = input("enter the statement")# count the number of uppercases in the string 
uppercase =0
for char in string:
    if char.isupper():
        uppercase += 1
print(uppercase)


string = input("enter the statement")
uppercase =0
for i in range (len(string)):
    if string[i].isupper():
        print(i) # output the index of the uppercase letters

string = "hel6o p6yth0n"
found = False
position = 0

while not found and position < len(string):
    if string[position].isdigit():
        found = True
    else: 
        position += 1
if found:
    print("the first digit occure in position", position)
else:
    print(" the string dose not contain a digit")


string = "hel6o p6yth0n"
found = False
position = len(string) - 1


while not found and position < len(string):
    if string[position].isdigit():
        found = True
    else: 
        position -= 1
if found:
    print("the first digit occure in position", position)
else:
    print(" the string dose not contain a digit")