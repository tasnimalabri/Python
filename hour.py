num1 = input("Enter hour : ")
num11 = input("Enter minute : ")
num2 = input("Enter hour : ")
num22 = input("Enter minute : ")
if(num1 < num2):
    print(" Time 1 comes first")
elif(num1 == num2):
    if(num11 <= num22):
        print("time1 come first")
    else:
        print("time 2 come first")   
else:
    print("Time 1 comes first")
