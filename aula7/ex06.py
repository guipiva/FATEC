n = int(input("digite o valor de n: "))
e = 0
for k in range(1, n+1):
    e = e + 2**k
print(f"O valor de E é igual: {e}")
