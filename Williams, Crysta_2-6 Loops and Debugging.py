#Keeps track of the amount of prime numbers the user enters
num = int(input("Enter a positive value: -1 to quit"))
primeCount = 0

while num > 0:
   #reset isPrime for each new number.
   isPrime = True

   if num > 1:
    for i in range(2, num):
      if num % i == 0:
        isPrime = False
    
    else:
      isPrime = False #Numbers<1 are not prime
    
    if isPrime:
      print(num, "is prime")
      primeCount += 1
    else:
        print(num, "is not prime")
        num = int(input("Enter a positive value: -1 to quit"))

print("Prime Count: ", primeCount)