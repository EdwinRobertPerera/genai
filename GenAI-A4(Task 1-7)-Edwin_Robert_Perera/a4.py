import os
# Task 1: Write Sales Records to a File

sales=[1200,450,980,1500,3000]
with open("sales_data.txt","w") as file:
    for sale in sales:
        content=str(sale)+"\n"
        print(content)
        file.write(content)
    file.close()
with open("sales_data.txt","r") as file:
    print(file.read())
    file.close()

# Task 2: Read File in Different Ways

with open("sales_data.txt","r") as file:
    print("The data in the file: \n")
    print(file.read())
    file.close()

with open("sales_data.txt","r") as file:
    print("The data in the first line of file: \n")
    print(file.readline())
    file.close()

with open("sales_data.txt","r") as file:
    print("The data in the all lines of file using readlines(): \n")
    content=(file.readlines())
    
    list_of_int=list(map(int,content))
    print(list_of_int)
    file.close()

# Task 3: Append New Sales
new_sales = [5000,2500,1700]

with open("sales_data.txt","a") as file:
    for sale in new_sales:
        file.write(str(sale) + "\n")
    file.close()
with open("sales_data.txt","r") as file:
    print(file.read())

# Task 4: Generate Summary Report from File
with open("sales_data.txt","r") as file:
    print("The data in the all lines of file using int list(): \n")
    content=(file.readlines())
    
    list_of_int=list(map(int,content))
    print("Total sales : ",sum(list_of_int),"Highest sale : ",max(list_of_int),"Lowest sale : ",min(list_of_int),"Avg sale : ",sum(list_of_int)/len(list_of_int))
    file.close()

# Task 5: Create Product Info File (User Input)


with open("products.txt","w") as file:
    for i in range(3):
        product=input("Enter your product")
        price=input("Enter your products Price")
        content=product+" | "+price+"\n"
        file.write(content)
file.close()
with open("products.txt","r") as file:
    print("The data in the all lines of file using readlines(): \n")
    print(file.read())  
    file.close()



# Task 6: Read File Safely (Error Handling Inside File Handling Only)
filename=input("Enter Filename")
if os.path.exists(filename):

    with open(filename, "r") as file:
        print(file.read())

else:
    print("File not found. Please check the filename.")

# Task 7

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = float(input("Enter discount percentage: "))

with open("discount_report.txt", "w") as file:

    file.write("Product | Original Price | Discounted Price\n")

    total = 0

    for product in prices:

        original = prices[product]
        discounted = original - (original * discount / 100)

        total += discounted

        file.write(product + " | " +
                   str(original) + " | " +
                   str(discounted) + "\n")

    average = total / len(prices)

    file.write("\n")
    file.write("Total Items: " + str(len(prices)) + "\n")
    file.write("Average Discounted Price: " + str(average))

print("\nDiscount Report")

with open("discount_report.txt", "r") as file:
    print(file.read())