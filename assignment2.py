def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
print("Select which you want:-\n"\
      "1.Add\n"\
      "2.Sub\n"\
      "3.mul\n"\
      "4.div\n")
select=int(input("Select number 1 2 3 4 5 :"))
n1=int(input("Enter Frist number:"))
n2=int(input("Enter Second Number:"))

if select==1:
    print(add(n1,n2))
elif select==2:
    print(sub(n1,n2))
elif select==3:
    print(mul(n1,n2))
elif select==4:
    print(div(n1,n2))

else:
    print("Invalid Input....!!!")


  