__author__ = 'andrii'
from urllib.request import urlopen

with urlopen("https://raw.githubusercontent.com/scipy/scipy/master/INSTALL.rst.txt") as file :
    for line in file:
        print(line.decode("utf-8"));
