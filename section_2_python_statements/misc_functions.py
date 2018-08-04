def main():

    # range
    for num in range(10):
        print(num)
    print('\n')
    for num in range(2,11,2):
        print(num)
    print('\n')
    x = list(range(2,11,2))
    print(x)
    print('\n')

    # enumerate
    my_list = ['one','two','three']
    for index,item in enumerate(my_list):
        print(f'{index}: {item}')
    print('\n')

    # zip
    list1 = [1,2,3,4]
    list2 = ['a','b','c','d']
    for item in zip(list1,list2):
        print(item)
    print('\n')
    newList = list(zip(list1,list2))
    print(newList)
    print('\n')

    # in keyword
    print(2 in list1)
    print('\n')
    my_dictionary = {'k1':1,'k2':2,'k3':3}
    print('k1' in my_dictionary) # check if key exists in dictionary
    print('\n')

    # min,max, and random
    print(f'Min: {min(list1)}')
    print(f'Max: {max(list1)}')
    from random import shuffle
    shuffle(list1)
    print(list1)
    from random import randint
    x = randint(0,100)
    print(x)

    # input
    userInput = input('enter a number: ')
    print(f'You entered: {userInput}')
    print(type(userInput)) # input alwyas casts input to string
    userInput = int(userInput)
    print(type(userInput))

    pass
main()
