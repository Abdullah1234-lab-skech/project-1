n=int(input("Enter the number whose sum you want to find ")) 
sum=0
for i in range(1, n+1):
    sum=sum+i 
print("The sum =", sum) 
string=input("Enter a string: ")
string2=('') 
for i in string: 
    string2= i + string2 
print("/nThe Original String is=", string) 
print("The Reversed String is=", string2) 