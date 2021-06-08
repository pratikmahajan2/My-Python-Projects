def fib(sum,num):
    if num<10:
        print(sum)
        fib(sum+num,sum)


fib(0,1)