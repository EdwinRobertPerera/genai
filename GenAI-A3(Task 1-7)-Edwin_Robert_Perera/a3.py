#GenAI-A3(Task 1-7)-Edwin_Robert_Perera.py

#Task1 - Basic Functions:Price After Discounts
def apply_discount(price,discount_percent=5):
        if discount_percent>=60:
            return("price cant be processed as the discount exceeded more than 60 percent")
        return(price-(price*(discount_percent/100)))  
print(apply_discount(1000,10))
print(apply_discount(500))
print(apply_discount(500,60))

#Task2 - Recursive Function: Factorial Utility
def factorial(num):
    if num<0:
        return "factorial cannot be determined for negative value" 
    
    elif num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))
print(factorial(0))
print(factorial(-3))


# Task3 - Lambda Function: GST Calculator
gst=lambda x : x+(x*0.18)
print(gst(100))

#Task4 - map(): Apply GST to list of prices
prices=[100,250,400,1200,50]
print(prices)
prices_after_gst=list(map(gst,prices))
print(prices_after_gst)

#Task5 - Using filter(): Filter expensive products

prices=[100,250,400,1200,50,2000,850]
prices_1=list(filter(lambda x:x>500,prices))
prices_2=list(filter(lambda x:x<=500,prices))
print("List of prices greater than 500 :",prices_1,"\nList of prices less than or equal to 500 : ",prices_2)

#Task6 - Combined Utility Function
process_prices=[100,500,900,50,750]
Discounted_list=(list(map(lambda x:x-(x*0.10),process_prices)))
print("Discounted Prices",Discounted_list)
print("List of filtered price",list(filter(lambda x: x>300,Discounted_list)))

#Task7 - Mini Problem: Menu Using Functions 

#add_price=lambda x,y : y.append(x)
def add_price(x,y):
    y.append(x)
#show_avg=lambda x : sum(x)/len(x)
def show_avg(x):
     return(sum(x)/len(x))
#show_highest=lambda x : max(x)
def show_highest(x):
    return max(x)
List=[]
while True:
        print("Selection Menu \n1.Add Price\n2.Show Average Price\n3.Show Highest price\n4.Quit")
        option=int(input("Enter your options Your choice are --> (1 , 2 , 3 , 4) :"))
        if option==1:
            price=int(input("Enter Your price"))
            add_price(price,List)
            print(List)
            continue
        elif option==2:
            print("your avg is ",show_avg(List))
            print(List)
            continue
        elif option==3:
            print(show_highest(List))
            print(List)
            continue
        elif option==4:
            break
        else:
            print("Enter a valid option")


