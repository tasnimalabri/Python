def find(list, n):
    longer = [word for word in list if len(word) > n]
    return longer
user = ['Tasnim', 'saif','Mubarak' , 'alabri']
n = int(input("Enter the minimum length of word"))
result = find(user, n)
print("word longer than" , n , "characters:" , result)