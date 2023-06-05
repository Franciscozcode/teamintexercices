#Create a variable for save the user string
user_string = (input("Enter a string for reverse "))



reverse_string = user_string[::-1]

print(f"The reverse string is   {reverse_string} ")


def reverse_str(user_inp):
    return user_string[::-1]

print(reverse_str(user_string))