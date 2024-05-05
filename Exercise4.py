
#change type from string to int.
def ChangeStrToInt(lsts):
    for lst in lsts:
        i=0
        for x in lst:
            if x.isnumeric():
                lst[i]= int(x)
            i+=1

list_1 = input("Enter the first tuple\n"
                    +"'put a space between them' :").split()
list_2 = input("Enter the second tuple\n"
                    +"'put a space between them' :").split()
list_3 = input("Enter the third tuple\n"
                    +"'put a space between them' :").split()
list_4 = input("Enter the fourth tuple\n"
                    +"'put a space between them' :").split()
list_5= input("Enter the fifth tuple\n"
                    +"'put a space between them' :").split()
ChangeStrToInt([list_1, list_2, list_3, list_4, list_5])
    
new_list= [tuple(list_1), tuple(list_2), tuple(list_3), tuple(list_4), tuple(list_5)]

print(f"my_lst = {new_list}")
print(f"The ordered list is: {sorted(new_list, key=lambda tp: (isinstance(tp[-1], int), tp[-1]))}")