import math

list_1 = input("Enter a list 'more than one!!\n"
                    +"'put a space between them' :").split()
      # Exercise 3.1
# creat new list that have numbers and strings.
new_list=[]
for x in list_1:
    if x.isnumeric():
        new_list.append(int(x))
    else:
        new_list.append(x)
        
if len(new_list) > 1:
    new_list_length= math.ceil(len(new_list) / 2)
    new_list1= new_list[:new_list_length:]
    new_list2= new_list[new_list_length::]
    print(f"my_lst = {new_list}")
    print(f"Tuple 1 is: {tuple(new_list1)}")
    print(f"Tuple 2 is: {tuple(new_list2)}")
    
      # begin for Exercise 3.2
    odd_index_list = new_list[1::2]
    even_index_list = new_list[::2]
    
    print(f"Tuple with even index is: {tuple(even_index_list)}")
    print(f"Tuple with odd index is: {tuple(odd_index_list)}")
    
    # end for exercise 3.2
    
else:
    print("The length of list must contain at least two element!")