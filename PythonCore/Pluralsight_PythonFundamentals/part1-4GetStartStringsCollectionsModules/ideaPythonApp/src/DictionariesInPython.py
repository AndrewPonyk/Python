__author__ = 'andrii'

e = {}  # Empty dictionary
e['phone'] = '032234523';
e[1] = 111;

print(e)  # prints {'phone': '032234523'}

# display list
for item in e:
   print(item, "->", e[item]);