def sum(num1,num2):
    print(num1+num2)

def sub(num1,num2):
    print(num1-num2)

calc = input("Enter sum or sub : ")
n1=int(input("Enter num1 : "))
n2=int(input("Enter num2 : "))

if calc == "sub":
    sub(n1,n2)
else:
    sum(n1,n2)
