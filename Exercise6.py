# exercise with additional methods

try:
    num_1 = int(input("Enter ur number: "))
    num_2 = int(input("Enter the length of array: "))
    num_3 = int(input("Enter the length of the matrix array: "))

    # here is the exercise.
    list_1 = [[num_1]* num_2] * num_3
    print(list_1)

except ValueError:
    print("Input error!!\nYou must enter numbers only.")