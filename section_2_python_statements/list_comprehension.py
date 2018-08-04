def main():

    # one method of splitting string
    my_string = 'hello'
    my_list = []
    for letter in my_string:
        my_list.append(letter)
    print(my_list)

    # same thing, one line
    my_list = [letter for letter in my_string]
    print(my_list)

    new_list = [num for num in range(0,11)]
    print(new_list)
    new_list = [num**2 for num in range(0,11)]
    print(new_list)

    # can have conditionals inside
    new_list = [num for num in range(0,11) if num%2==0]
    print(new_list)

    # can perform calculations inside
    degrees_C = [0,10,20,100]
    degrees_F = [((9/5)*temp+32) for temp in degrees_C]
    print(degrees_C)
    print(degrees_F)

    # get first letter of each work using list comprehension
    my_string = 'this is my string'
    my_list = [word[0] for word in my_string.split()]
    print(my_list)


    pass
main()
