def binarysearch(list,number):
    l=0
    u=len(list)-1
    mid=0
    while l<=u:
        mid=(l+u)//2
        midnumber=list[mid]

        if midnumber==number:
            return mid
        elif mid<number:
            l=mid+1
        else:
            u=mid-1
    return -1

if __name__=='__main__':
    list=[1,2,3,4,5,6,7,8,9,10,11,11,11,12,13,14,15,16]
    number=14
    index=binarysearch(list,number)
    print("number found at",index,"index")


   
