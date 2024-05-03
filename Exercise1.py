my_lst = input("Enter some numbers 'more than tow numbers'\n"
                    +"'put a space between them' :").split()
"""
if len(my_lst) >= 4:
    my_lst.pop(3)
    my_lst.pop(2)
    my_lst.pop(0)
elif  len(my_lst) == 3:
    my_lst.pop(2)
    my_lst.pop(0)
else: 
    print("The number of list is less than 3!")
print(f"The new list is {list(map(int, my_lst))}")
"""
try:
    print(f"my_list = {list(map(int, my_lst))}")
    if len(my_lst) >= 3:
        new_list = [j for i, j in enumerate(my_lst) if i not in [0, 2, 3]]
        print(f"The new list is {list(map(int, new_list))}")
    else:
        print("The number of list is less than 3!")
except ValueError:
    print("Input error!!\nYou must enter numbers only.")