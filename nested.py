state = input("Enter Yes or No : ")
age = int(input("Enter your age: "))
gender = str(input("Enter your gender: "))

if(age >= 18):
    if(state == "Yes"):
        if(gender == "Female"):
            print("graduated & 18 or above years old and female")
        else:
            print("Not graduated & 18 or above years old and male")
        
        
else:
    print("under 18 years")
        