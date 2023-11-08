from pythonmodules import moduleFib

#In Python, the equivalent of Java packages are called "modules" and "packages".

#A module is a single file that contains Python code, usually with a specific purpose or functionality. Modules can be imported and used in other Python code.
#A package is a collection of modules that are grouped together in a directory structure. Packages are used to organize and manage related modules in a project, and can be nested to create sub-packages.

temp = moduleFib.fib(10)
print(temp)