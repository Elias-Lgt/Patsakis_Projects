import random
def fib(n):
    return round((1/(5**(1/2)))*(((1+(5**(1/2)))/2)**(n+1))-(1/(5**(1/2)))*(((1-(5**(1/2)))/2)**(n+1)))

nth=input('Give the value of n: ')
k=0
p=fib(int(nth)-1)
for i in range(20):
    a=random.randint(0, 9999999999999999999999999)
    if ((a**p)-a)%p==0 :                                               #Fermat's little theorem
        continue
    else:
        print('The '+str(nth)+"th term of the fibonacci sequence("+ str(p) +") is not a prime number")
        k=1
        break
if k==0:
    print('The '+str(nth)+"th term of the fibonacci sequence("+ str(p) +") is a prime number")
