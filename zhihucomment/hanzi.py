import random
import importlib,sys
importlib.reload(sys)
arr = []
for i in range(2000):
    arr.append(chr(random.randint(0x4e00, 0x9fa5)))
f = open('words.txt', 'w+')
for str in arr:
    f.write(str)
