def main():

    # if-elif-else structure
    condition = True
    if condition is 1:
        print('Condition is 1')
    elif condition is False:
        print('Condition is false')
    else:
        print('Condition is true')

    # for loops
    my_list = [0,1,2,3,4,5]
    for value in my_list:
        print(value)

    # if you dont inted to use the value after for, use _
    for _ in my_list:
        print('Hello world')

    my_list = [(1,2),(3,4),(5,6)] # list of tuples
    for x in my_list:
        print(x)

    # tuple unpacking
    for a,b in my_list:
        print(f'Value 1: {a}')
        print(f'Value 2: {b}')

    # iterate through dictionary
    my_dictionary = {'k1':1,'k2':2,'k3':3}
    for item in my_dictionary.items():
        print(item)
    for key in my_dictionary.keys():
        print(my_dictionary[key])
    for key,value in my_dictionary.items():
        print(f'Key: {key} \tValue: {value}')


    # while loops
    x = 0
    while (x != 5):
        print(x)
        x = x+1

    # break -> breaks out of current loop
    # continue -> goes to top of current loop
    # pass -> does nothing

    pass
main()
