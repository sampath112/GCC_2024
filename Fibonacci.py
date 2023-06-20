def fibo(n):
    a=0
    b=1
    print(a,end=" ")
    for i in range(n):
        c=a+b
        b=a
        a=c
        if c>n:
            break
        print(c,end=" ")
n=int(input())
fibo(n)
