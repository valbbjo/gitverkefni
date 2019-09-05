#use while to prompt for number again as long as input is >=0
#if number is <0 print out the largest number
num_int = int(input("Input a number: "))    # Do not change this line

max_int = num_int

while num_int >=0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int
else:
    print("The maximum is", max_int)    # Do not change this line
