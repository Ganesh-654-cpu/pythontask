# Day 2 Task

# EF-ELSE
#Nested If-else
# ELIF



# 1) ATM Withdrawal System

balance = 5000
amount = int(input("Enter amount to withdraw: "))

if amount <= balance:
    print("Transaction Successful")
    print("Remaining Balance:", balance - amount)
else:
    print("Insufficient Balance")
    
    
    
    
    # 2) Login System (Authentication)

username =input("Enter Username:")
password =input("Enter Password:")

if username == "admin" and  password == "1224":
    print("Login Successful")
else:
    print("Invalid Credentials")
     
        


#3Login System

    password = input ("Enter Password:")

    if password =="admin222":
        print("Login Successful")
    else:
        print("Invalid Password")
    
            
                

#4Discount System

amount = int(input("Enter amount"))

if amount >= 1000:
    print("Discount applied")
else:
    print("No Discount")
    

                    
                    

#5) Voting Eligibility

age = int(input("Enter your age:"))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible")




#6) Largest Between Two Numbers

a= int(input("Enter first number:"))
b = int(input("Enter Second Number"))

if a > b:
    print("A is greter")
else:
    print("B is greter")
    
    
    

    # elif  programs

day = int(input("Enter day Number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Input")




#2) Simple Calculator

a = int(input("Enter first number: "))
b = int(input("Enter second number:"))
op = input("Enter operator(+,-,*,/): ")

if op =="+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op =="*":
    print(a*b)
elif op == "/":
    print(a/b)
else:
    print("Invalid operator")



#3) Income Tax Slabs

income = float(input("Enter your incomme in 100k"))

if income <= 2.5:
    print("No tax")
elif income <=5:
    print("Tax 5%")
elif income <10:
    print("Tax 20%")
else:
    print("Tax 30")


#4) Speeding Fine

speed = int(input("Enter vehicle speed (km/h): "))

if speed <= 60:
    print("No fine")
elif speed <= 80:
    print("Fine 50$")
elif speed <= 100:
    print("Fine 100$")
else:
    print("Fine $200 + License Suspended")



#5) Ticket Price Based On Age


age = int(input("Enter your age: "))

if age <=5:
    print("Free Ticket")
elif age <=18:
    print("Child Tcket")
elif age <=60:
    print("Adult ticket")
else:
    print("Senior citizen ticket")
    
    
#1)Nested If-else


num=8

if num > 0:
    if num % 2 == 0:
        print("Positive Even")
    else:
        print("positive Odd")
else:
    print("Negative Number")
    
    
    #2)Pass or Fail
    
    marks = 40 
    if marks >= 35:
        if marks >= 75:
            print("Distinction")
        else:
            print("Pass")
    else:
        print("Fail")
        
        
        
        #3) Bigest of Two (with Equlity)

    a = 10
    b = 10
    
    if a>= b:
        if a == b:
            print("Both Equal")
        else:
            print("A is bigger")
    else:
        print("B is bigger" )     
        
        
        #4)Age check
        
        age = 16
        
        if age >=18:
            if age >=21:
                print("Adult +Eligible for everything")
            else:
                print("Adult")
        else:
                 print("minor")
                 
                 
                 
        #5)Simple Divisio Check
        
        a=10
        b=2
        
        if b!= 0:
            if a>b:
                print("Division =", a/b)
            else:
                print("A should be greter than B")
        else:
            print("Cannot divide by zero")
            
            
    