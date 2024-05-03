list_1 = input("Enter the first tuple\n"
                    +"'put a space between them' :").split()
# change the value of list that have numbers or strings.
i=0
for x in list_1:
    if x.isnumeric():
        list_1[i]= int(x)
    i+=1
list_2 = input("Enter the second tuple\n"
                    +"'put a space between them' :").split()
i=0
for x in list_2:
    if x.isnumeric():
        list_2[i]= int(x)
    i+=1
list_3 = input("Enter the third tuple\n"
                    +"'put a space between them' :").split()
i=0
for x in list_3:
    if x.isnumeric():
        list_3[i]= int(x)
    i+=1
list_4 = input("Enter the fourth tuple\n"
                    +"'put a space between them' :").split()
i=0
for x in list_4:
    if x.isnumeric():
        list_4[i]= int(x)
    i+=1
list_5= input("Enter the fifth tuple\n"
                    +"'put a space between them' :").split()
i=0
for x in list_5:
    if x.isnumeric():
        list_5[i]= int(x)
    i+=1
    
new_list= [tuple(list_1), tuple(list_2), tuple(list_3), tuple(list_4), tuple(list_5)]

print(f"my_lst = {new_list}")
print(f"The ordered list is: {sorted(new_list, key=lambda tp: tp[-1])}")