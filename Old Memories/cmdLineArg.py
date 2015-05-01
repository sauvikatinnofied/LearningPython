import sys


print (len(sys.argv))
print (sys.argv)
for arg in sys.argv:
    print (arg)
print ("Hello" * 2)

for x in range(10, 20):
    print (x)
for char in "Python":
    if char == "h":  continue
    else: print ("Current Letter: ",char)

# the while loop
var = 10
while var > 0:
    print ("Current loop variable is ", var)
    var -= 1
number = 2
primeCount = 0
while number < 100:
    j = 2
    while j <= (number/j):
        if number % j == 0:
            break
        j = j + 1
        if (j >= number/j):
            print (number," is a prime")
            primeCount += 1

    number += 1

print ("Primes under 100 = ", primeCount + 1)

    
        
