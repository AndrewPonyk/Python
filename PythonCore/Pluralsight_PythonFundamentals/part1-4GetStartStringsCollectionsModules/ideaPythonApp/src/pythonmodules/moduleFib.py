print("I'm a Fibonacci module");

def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    return n;


if __name__ == "__main__": # name is __main__ when execute from command line, if someone is import our file as module __name__ will be 'moduleFib'
    print("I am executing from command line, so I'll execute main function")
    print(fib(10))
