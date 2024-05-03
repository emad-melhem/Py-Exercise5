list_1 = input("Enter some numbers !!\n"
                    +"'put a space between them' :").split()
list_2 = input("Enter some numbers !!\n"
                    +"'put a space between them' :").split()
list_3 = list_1 + list_2

print(f"tuple_1 = {tuple(map(int, list_1))}")
print(f"tuple_2 = {tuple(map(int, list_2))}")
print(f"The new tuple is: {tuple(map(int, list_3))}")