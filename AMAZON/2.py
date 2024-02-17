def function(s,a):
    b=min(a)
    a.remove(b)
    c=min(a)
    if(b+c<=s):
        return b*c
    else:
        return 0



if __name__ == "__main__":
    #s=int(input())
    #a=int(input())
    s=9
    a={5,2,4,3,9,7,1}