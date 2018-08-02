def main():

    ## LISTS
    print('\n=====')
    print('LISTS')
    print('=====')
    # make a list with square brackets
    # lists are mutable
    my_list = [1,2,3]
    print(my_list)
    my_list[0] = 2
    print(my_list)

    # can make a list with mixed types
    my_list = ['one',2,'three']
    my_list[0] = my_list[0].upper()
    print(my_list)
    print(len(my_list))

    # can concatenate with lists
    list_1 = ['one', 'two', 'three']
    list_2 = ['four']
    new_list = list_1 + list_2
    print(new_list)
    new_list.append('five'.upper())
    print(new_list)

    # remove item with pop
    # default index = end
    popped_item = new_list.pop()
    print(popped_item)
    print(new_list)
    popped_item = new_list.pop(1)
    print(popped_item)
    print(new_list)

    # built in sorting
    # in-place function (doesn't return, just sorts)
    number_list = [1,7,5,2,3]
    print(f'Pre-sort: {number_list}')
    number_list.sort()
    print(f'Post-sort: {number_list}')
    string_list = ['apple','orange','banana','avocado']
    print(f'Pre-sort: {string_list}')
    string_list.sort()
    print(f'Post-sort: {string_list}')
    string_list.reverse()
    print(f'Post-reverse: {string_list}')


    ## DICTIONARIES
    print('\n============')
    print('DICTIONARIES')
    print('============')

    # dictionaries cannot be sorted
    # dont need to know where items are located
    # make a dictionary with curly brackets
    my_dictionary = {'key1':'value1','key2':'value2'}
    print(my_dictionary)
    print(my_dictionary['key2'])
    prices = {'apple':2.99,'orange':1.99,'banana':0.99}
    print(f"Price of bananas: ${prices['banana']}")
    nested_dictionary = {'key1':1,'key2':[2,3,1],'key3':{'inner_key1':'nested value'}}
    nested_value = nested_dictionary['key3']['inner_key1']
    print(nested_value)
    print(f'Pre-sort: {nested_dictionary}')
    nested_dictionary['key2'].sort()
    print(f'Post-sort: {nested_dictionary}')

    # add to/overwrite existing dictionary
    my_dictionary['key3'] = 'value3'
    print(my_dictionary)
    my_dictionary['key3'] = 'value4'
    print(my_dictionary)

    # get all keys or values
    print(f'Keys in nested dictionary: {nested_dictionary.keys()}')
    print(f'Values in nested dictionary: {nested_dictionary.values()}')

    pass
main()
