
try:
    list_1 = list(map(int, input("Enter some numbers to calculate the average!!\n"
                    +"'put a space between them' :").split()))
    sum_numbers=0
    for x in list_1:
        sum_numbers+= x
    avg= sum_numbers/len(list_1)
    print(f"The average is {avg:2}")
    
    # exercise 5.2
    new_num_added= 5 * (len(list_1) + 1) - sum_numbers
    print(f"The average was {avg}")
    list_1.append(new_num_added)
    print(f"Added {new_num_added}, new list is {list_1}")
    print(f"The average is now {(sum_numbers+new_num_added) / len(list_1)}")
except Exception as err:
    print(err.args[0])