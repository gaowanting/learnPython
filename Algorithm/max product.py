import sys

lines = sys.stdin.readlines()
l = [int(i) for i in lines[1].split(" ")]
a = max(l)
l.remove(a)
b = max(l)
print(a*b)

