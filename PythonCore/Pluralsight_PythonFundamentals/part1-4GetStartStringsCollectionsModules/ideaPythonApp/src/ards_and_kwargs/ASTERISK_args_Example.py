def myPrint(val):
    print(str(val) + "-----")

def myPrintAll(myVal, *args):
    for v in args:
        print(v)
    print(args[0]) # args with * its just positional parameters!

myPrint(134)
myPrintAll(1,2,3,4)
