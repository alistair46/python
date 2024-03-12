'''write a function which will accept list [2,3,1,5,4,8,6,9,12,13] as input and 
calculate square for even numbers and cube for odd numbers and return as list.'''

lst=[2,3,1,5,4,8,6,9,12,13]
#lst=list(map(int,input().split()))
for i in lst:
    if (i%2)==0:
        print(i*i)
    else:
        print(i*i*i)
