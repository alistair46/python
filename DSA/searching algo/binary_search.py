position =-1

def sort(list,n):
    l=0
    u=len(list)-1


    while l<+u:
        mid = (l+u)//2

        if list[mid]==n:
            globals()['position']=mid  
            return True
        
        else:
            if list[mid]<n:
                l=mid+1

            else: u=mid-1



list=[2,3,4,5,6,7,8,9]
n=2

if sort (list,n):
    print("found at",position +1)
else :
    print("not found")