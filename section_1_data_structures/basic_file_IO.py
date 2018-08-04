def main():

    myFile = open('basic_file_IO.txt')
    print(myFile.read())
    print(myFile.read()) # prints nothing becuase cursor is now at EOF
    myFile.seek(0) # resets cursor back to start
    print(myFile.read())
    myFile.seek(0)
    fileContents = myFile.read()
    myFile.seek(0)
    fileContentsByLine = myFile.readlines()
    print(fileContents)
    print(fileContentsByLine)

    myFile.close() # need to close file after opening to avoid errors

    ## Alternate to 'close' method
    # use with to grab data and then be done with file
    # dont need to worry about closing file
    with open('basic_file_IO.txt') as myNewFile:
        newFileContents = myNewFile.readlines()

    print(newFileContents)


    ## Writing to files
    # different modes when opening files
    # read = 'r'
    # write = 'w'
    # append = 'a'
    # read and write = 'r+'
    # write and read = 'w+'

    with open('basic_file_IO.txt',mode='r') as f:
        print(f.read())

    with open('basic_file_IO.txt',mode='a') as f:
        f.write('this is line four')

    with open('new_file.txt',mode='w') as f:
        f.write('Hello world!')

    pass

main()
