def fibonocci(x):
    fib_list = [0, 1]
    for i in range(1,x-1):
        y = fib_list[i] + fib_list[i-1]
        fib_list.insert(i+1, y)
    print(fib_list)

fibonocci(30)



