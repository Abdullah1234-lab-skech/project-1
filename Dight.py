Question=int(input("Enter a number: "))  
while Question > 0: 
    Digit=Question % 10 
    Question //= 10
    print("The reversed order is of the number is",Digit)          