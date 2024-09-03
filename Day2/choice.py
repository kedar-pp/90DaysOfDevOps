# choice to do arthimetic operations

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))

choice= input("Enter the operation you want to perform: (Options +,-,*,/,%)")

if choice == "+":
    sum=num1 + num2
    print("Addition: ",sum)
elif choice =="-":
    diff=num1-num2
    print("subtraction: ",diff)
elif choice =="*":
    prod=num1*num2
    print("multiplication: ",prod)
elif choice =="/":
    div=num1/num2
    print("division: ",div)
elif choice=="%":
    mod=num1%num2
    print("remainder: ",mod)
else:
    print("Invalid choice")