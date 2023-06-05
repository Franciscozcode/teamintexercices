
#Create an empty array for the values from user
number_list = []
#Create a loop, then inter the values from the user with append to the array. 
for i in range(5):
    number_list.append(int(input("Enter a number: ")))
    #finally print the current, the previous value and the max value of user nums.
    print(f"Current number: {number_list}, previous Number: {number_list[i]}, Max Value is : {max(number_list)}")



