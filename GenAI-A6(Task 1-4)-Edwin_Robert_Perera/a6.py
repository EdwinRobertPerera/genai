#Task 1 Safe Division Utility 
try:
    numerator=int(input("Enter your numerator : "))
    denominator=int(input("Enter your denominator : "))
    print("The result is ",numerator//denominator)
except ValueError:
    print("please enter a number for denominator or numerator")
except ZeroDivisionError:
    print("Denominator shouldnt be zero")
finally:
    print("Operation compplete")


#Task 2 Bill caluclator with error handling 
prices = [120, 350, 'abc', 500, -200, 800]
total=0
for price in prices:
    try:
        if price >=0:
            total+=price
        elif price <0 :
            raise ValueError
    except TypeError:
        print(price,"is not a valid number ")
    except ValueError:
        print("Negative values are not allowed")
print(total)

#Task 3 Custom Exception : Age Validator
def check_age(age):
    try:
        if not (0<=age<=120):
            raise ValueError
    except ValueError:
        print("Enter a valid age")
age=int(input("Enter your age"))
check_age(age)

#Task 4 File reader with exception handling
filename=input("Enter your filename")
try:
    with open(filename,'r') as file:
        for _ in range(3):
            line = next(file, None)  
            if line is None:
                break
            print(line, end='') 
except PermissionError:
    print("no permission given")
except FileNotFoundError:
    print("no file found with this name")

#Task 5 Mini Program : Safe Shopping Cart
cart=[]
while True:
    try: 
        value=input("Enter your price")
        if value=="q":
            print("Total Items : ",cart,"Total Bill : ",sum(cart))
            break
        elif int(value)<0:
            raise Exception("Its a negative value")
        else:
            val=int(value)
            cart.append(int(value))
    except ValueError:
                print("Enter valid a number")
    except Exception:
            print("Negative value is not allowed ")

    
    
