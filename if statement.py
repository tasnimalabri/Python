mark = int(input("Enter your mark: "))
if mark > 90:
     print("A")
elif 90 <= mark < 80:
     print("B")
elif 80 <= mark < 60:
     print("C")
elif mark <= 60:
     print("D")
else:
    print("F")