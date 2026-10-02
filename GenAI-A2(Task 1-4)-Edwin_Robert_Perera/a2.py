#File name-GenAI-A2(Task 1-4)-Edwin_Robert_Perera

#Task 1:Discount Rules(if.elif,else)
print("Task 1:Discount Rules(if.elif,else)\n")
order_amount = int(input("Enter the order amount: "))
if order_amount >= 2000:
    discount=0.15
elif order_amount < 2000 and order_amount >= 1500:
    discount=0.10       
elif order_amount < 1500 and order_amount >= 1000:
    discount=0.07
else:
    discount=0.00
tax=0.05
Subtotal=order_amount - (order_amount * discount)
print("Subtotal after discount: ", Subtotal)
final_amount= Subtotal+(Subtotal*tax)
print("Final amount after discount: ", final_amount)


#Task 2:Process Multiple Orders(for loop)
print("\n\nTask 2:Process Multiple Orders(for loop)")

order_amounts = [1250,2500, 800, 1750, 3000]
summary_table=[]
for order_amount in order_amounts:
    if order_amount >= 2000:
        discount=0.15
    elif order_amount < 2000 and order_amount >= 1500:
        discount=0.10       
    elif order_amount < 1500 and order_amount >= 1000:
        discount=0.07
    else:
        discount=0.00
    Subtotal=order_amount - (order_amount * discount)
    tax=0.05
    Final_Amount= Subtotal+(Subtotal*tax)
    summary_table.append([order_amount, int(discount*100), Subtotal, Final_Amount])
print("Order Amount\tDiscount\tFinal_Amount")
for order in summary_table:
    print(f"{order[0]}\t\t{order[1]}%\t\t{order[3]}")
total_final_amount =0
for order in summary_table:
    total_final_amount += order[3]
print("Total Final Amount: ", total_final_amount)

#Task 3:User Menu(while loop and break/continue )
order_amounts_list=[]
while(True):
    selected_option=input("Enter the option \n 1: Add a order amount \n 2: Show all orders and totals after applying discounts\n q: Quit \n \nEnter from above options : ")
    if selected_option=="1":
      amount=int(input("\nEnter the order amount : "))
      order_amounts_list.append(amount)
      continue
    elif selected_option=="2":
       print("Orders:",order_amounts_list)
       print("Total order amount:",sum(order_amounts_list))
       continue
    elif selected_option=="q":
       break
    else:
       print("\n\nChoose from options 1,2,q\n\n")

#Task 4 Loop control with conditions(break and continue)
final_amount=0
daily=[200,150,0,400,50,-1,300]
for a in daily:
    if a <0:
        print("Data is currupted Stoping the process......\n")
        break
    elif a == 0:
        print("This day had no sales skipping this day.....\n")
        continue
    elif a > 0:
        print("Adding",a,"to the final amounts\n")
        final_amount+=a
print("The final amount is ",final_amount)
