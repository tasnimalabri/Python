limit = 90
pos = 0
found = False
values=[1,2,30,90]
while pos < len(values) and not found :
    if values[pos] == limit :
        found = True
    else :
        pos = pos + 1
if found :
    print("Found at position:", pos)
else:
    print("Not found")