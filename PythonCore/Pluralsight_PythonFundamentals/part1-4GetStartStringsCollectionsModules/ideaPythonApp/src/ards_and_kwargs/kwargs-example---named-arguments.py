def printall(param1, **kwargs):
    print("hello hello" + str(param1))
    print(kwargs["str1"])

printall(1, str1 = "іваіа", str2="аін")


#**kwargs  - means that we can pass named parameters