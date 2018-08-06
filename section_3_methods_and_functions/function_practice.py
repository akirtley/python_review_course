def main():
    print(spy_game([1,2,3,4,5,6]))
    print(spy_game([1,2,3,4,0,0,7]))
    print(summer69([1,2,3,6,7,8,9,10]))
    print(summer69([1,2,6,9,1,2,6,7,9]))
    print(spy_game2([1,2,0,0,7]))
    print(spy_game2([1,2,0,3,4,0,5,7]))

    pass

def summer69(number_list):
    currentSum = 0
    add = True
    for value in number_list:
        if add:
            if value != 6:
                currentSum += value
            else:
                add = False
        if not add:
            if value != 9:
                continue
            else:
                add = True
    return currentSum
    pass

def spy_game(spy_numbers):
    count = 0
    while count < len(spy_numbers)-2:
        if spy_numbers[count] is 0:
            if spy_numbers[count+1] is 0:
                if spy_numbers[count+2] is 7:
                    return True
        count += 1
    return False
    pass

def spy_game2(spy_numbers):
    spy = False
    codeName = [0,0,7,'a']
    for value in spy_numbers:
        if value is codeName[0]:
            codeName.pop(0)
    if len(codeName) is 1:
        spy = True
    return spy

main()
