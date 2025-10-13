print("Hello")

name="john"
age=30
height="6ft"
isStudent=False

print(name)
print(age,height)
print(type(name))
print(type(isStudent))


name1=input("Enter name : ")
age1=int(input("Enter age : "))
height1=float(input("Enter height : "))

print("Hi", name1, "you are", age1, "years old and is", height1, "ft tall")


#arithmetic operators

a=5
b=10
print(a+b)   #add
print(a-b)   #sub
print(a*b)   #multiply
print(a/b)   #div 
print(a//b)  #floor division
print(a%b)   #modulus
print(a**b)  #exponentiation

num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
print( num1,"+",num2,"=",num1+num2)  #add
print( num1,"-",num2,"=",num1-num2)  #sub
print( num1,"*",num2,"=",num1*num2)  #mult
print( num1,"/",num2,"=",num1/num2)  #div
print( num1,"exp",num2,"=",num1**num2)  #exp
print( num1,"%",num2,"=",num1%num2)  #modulus

#logical operators
x=2
print(x<5 and x>7)
print(x<5 or x>7)
print(not(x<5 and x>7))


weight=float(input("Enter Weight in kg : "))
height=float(input("Enter height in cm: "))/100
bmi = weight / (height ** 2)
print(bmi)