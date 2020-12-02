numbers = open("numbers.txt", "r").read().split(",")

for i in range(1, 100000):
    if str(i) not in numbers:
        print(i)
        break
