def linear(list,number):
    for index, element in enumerate(list):
        if element == number:
            return index
    return -1



if __name__ == '__main__':
    list = [1,2,3,4,5,990,887,66,556,7878,435434] # list can be unsorted 
    number=435434

    index = linear(list,number)
    print("number found at ", index ," using linear search")