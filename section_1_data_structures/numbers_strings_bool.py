def main():

    # Variables in python do not have a set type...
    # Can change variable type simply by assigning new type

    # Set testVar to be an int
    testVar = 1
    print(testVar)
    print(type(testVar))

    # Now set testVar to be a boolean
    testVar = False
    print(testVar)
    print(type(testVar))

    # Strings
    hello_world_string = 'Hello world!'
    print(hello_world_string)
    print(len(hello_world_string))

    # String slicing
    print(hello_world_string[10])
    print(hello_world_string[-2])
    print(hello_world_string[6:11])
    print(hello_world_string[::2]) # 3rd parameter = step size
    print(hello_world_string[::-1]) # reverse string quickly

    # String methods
    a = 'Hello'
    b = ' world!'
    c = a + b
    print(c)
    print(c.upper())
    print(c.lower())
    print(c.split()) # split defaults to splitting on white space

    # String formatting
    print('Hello {}'.format('world!'))
    print('The {} {} {}'.format('fox','brown','quick'))
    print('The {2} {1} {0}'.format('fox','brown','quick'))
    print('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

    # Float formatting
    # {value:width.precision f}
    result = 8/9
    print(result)
    print('The result was: {r}'.format(r=result))
    print('The result was: {r:1.4f}'.format(r=result))

    # Formatted strings "f-string"
    name = 'Alex'
    print(f'My name is {name}')

main()
