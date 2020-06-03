import sys

if int(sys.argv[1]) < 0:
    raise ValueError('Please provide a positive number for printing Hello World.')
    
print(f'Script Name is {sys.argv[0]}')

num1 = int(sys.argv[1])

i = 1

while i <= num1:
    print(f'Hello World... {i}')
    
    i+=1
