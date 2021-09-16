# write some rubbish
a = 1
b = 1
print(a)
print(b)
for i in range(0, 10):
    c = a + b
    print(c)
    a = b
    b = c
# when you finish a project, check it can you simply it?

# the smarter one
a, b = 1, 1
while a < 10:
    print(a, end=" ")
    a, b = b, a+b
