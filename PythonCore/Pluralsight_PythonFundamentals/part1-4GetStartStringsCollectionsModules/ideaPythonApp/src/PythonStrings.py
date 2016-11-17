__author__ = 'andrii'

norsk = "Hvis du bruker de røde kodene, trykk på";
data = norsk.encode('utf-8');
print(data) #encoded data: for example ø - becomes xc3\xb8

print(data == norsk) # false
print(norsk == data.decode('utf-8')) # true

print(type (norsk)) # 'str' - is String Class in Python