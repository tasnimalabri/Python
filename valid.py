num=input("enter number:")
length=len(num)
if length == 8 and num[4] == " " and num[5:9].isdigit():
    print("valid")
else:
    print("invlid")
