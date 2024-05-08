
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
#first way
print(f"The ordered list is: {sorted(new_list, key=lambda tp: (isinstance(tp[-1], int), tp[-1]))}")

'''
#second way

new_list=[[7,2], [5, 9], [9, 1], [2, 7, 3], [7, 8]]
sorted_lst=[0] * len(new_list)

for i1, j1 in enumerate(new_list):
    index=0
    for i2, j2 in enumerate(new_list):
        if i1 != i2 :
            if (j1[-1] > j2[-1]) or (j1[-1] == j2[-1] and i1 > i2):
                index += 1
    sorted_lst[index] = j1
print(sorted_lst)

'''