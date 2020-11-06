#To find the prime number

x = int(input("Enter your data: "))

for i in range(2,x):

    if x%i==0:
        print(f'{x} is not a prime number')
        break

else:
    print(f'{x} is a prime number')