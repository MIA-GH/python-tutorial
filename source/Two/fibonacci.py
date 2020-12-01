# # # simple fibonacci series

a, b = 0, 1
while b < 1000:
    # print(b)
    print(b, end=' ', flush=True)
    a, b = b, a+b

print()