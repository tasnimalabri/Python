import random
counter = 1
x = random.randint(1,10)
while counter == 1:
    
    
    ans = input("your answer : ")
    if not (ans == "done"):
        if ans == str(x):
            print("your answer is correct!")
        elif ans <= str(x):
            print("go upper")
        else:
            print("go lower")
        break
