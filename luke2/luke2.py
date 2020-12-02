sum = 0
i = 0
def isPrime(num):
    if(num%2==0):
        return False
    for i in range(3, num, 2):
        if(num%i == 0):
            return False
    return True

while i<5433000:
    if '7' in str(i):
        for j in range(i, 0, -1):
            if(isPrime(j)):
                i+=j+1
                break
    else:
        i += 1
        sum+=1

print(sum)

