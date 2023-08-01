#print out the name of people who are above 22 years old

a_dec={1:{'name':'john','age':27,'sex':'Male'},
     2:{'name':'Marie','age':22,'sex':'Female'},
     3:{'name':'sali','age':23,'sex':'Female'}}


# Create a new empty dictionary
for key,item in a_dec.items():
     if item['age'] > 22:
        
        print(item['name'])
        
   
        
         


        