def fizzBuzz(n):
    # Write your code here

    if(n%3)==1:
        print("Fizz")
    elif(n%5)==1:
        print("Buzz")
        
    else:
        print(n)

if __name__=='__main__':
    n=int(input())