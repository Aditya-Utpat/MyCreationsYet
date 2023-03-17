n = int(input('Enter no. of primes you want:'))
primes = [2]
x = 3
while len(primes)<n:
    for i in primes:
        if x%i==0:
            x+=2
            break
    else:
        primes.append(x)
        x+=2
print(primes)
