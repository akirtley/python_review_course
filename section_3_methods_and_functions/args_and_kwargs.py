def main():

    # *args    -> treated as a tuple
    # **kwargs -> treated as a dictionary

    print(myFunc(1,2,3,4,5))

    myFunc2(Purdue='Boilermakers',Wisconsin='Badgers')

    myFunc3(1,2,3,meal='breakfast',fruit='banana')

    print(test('everyotherletterisuppercase'))


    pass

# example function using *args
def myFunc(*args):
    # Returns half of the sum of all input arguments
    for item in args:
        print(item)
    return sum(args) * 0.5

# example function using **kwargs
def myFunc2(**kwargs):
    if 'Purdue' in kwargs:
        print(f"Purdue's mascot is: {kwargs['Purdue']}")
    else:
        print('IU Sucks')

# example function using both
def myFunc3(*args,**kwargs):
    print(f"I would like {args[0]} {kwargs['fruit']}")

# exercise question
def test(word):
    newWord = []
    wordLower = word.lower()
    x = 1
    for letter in wordLower:
        if x%2 is not 0:
            newWord.append(letter)
        else:
            newWord.append(letter.upper())
        x+=1
    return ''.join(newWord)




main()
