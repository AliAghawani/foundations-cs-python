n = int(input("Enter a number: "))
pattern_size = (n * 2) - 1
for i in range(1, pattern_size + 1):
    if i <= n:
        print("*" * i)
    else:
        print("*" * (pattern_size - i + 1))









