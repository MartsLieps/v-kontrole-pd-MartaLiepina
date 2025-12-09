 fibonacci = [0, 1]
for i in range(2, 100):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
for num in reversed(fibonacci):
    print(num)