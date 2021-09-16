fibo = [0, 1]
n = int(input("which number do you wanna to know? "))
for i in range(2, n):
    fibo.append(fibo[i-1] + fibo[i-2])
print(fibo[n-1])