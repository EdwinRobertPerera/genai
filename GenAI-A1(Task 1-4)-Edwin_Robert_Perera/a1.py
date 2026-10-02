####Task 1 Products Collection(List and Tuples)
print("\n\nTask 1 Products Collection(List and Tuples))\n")

products=["apple","banana","orange","grape","kiwi","mango"]
_product=("apple",55,"fruits")
print("Second Product : "+products[1] +"  Last Product : " + products[-1])
products.extend(["watermelon","guava"])
print(products)
sample_product=list(_product)
sample_product.remove(55)
sample_product.append(100)
_product_new=tuple(sample_product)
print(sample_product)
print(_product_new)


#Task 2 Categories(Sets)
print("\n\nTask 2 Categories(Sets))\n")

categories_set={"fruits","fruits","vegetables","dairy","meat","grains", "beverages","snacks","frozen foods"}
print(categories_set)
categories_set.add("seafood")#added seafood to the set
categories_set.add("fruits")#added seafood to the set
print(categories_set)
print("fruits" in categories_set)#checking if fruits is present in the set
print("the number of unique categories in the set are : " + str(len(categories_set)))




#Task 3 Product Pricing(Dictionaries)
print("\n\nTask 3 Product Pricing(Dictionaries)\n")
price_dict={"apple":20,"banana":30,"orange":-40,"grape":60,"kiwi":80,"mango":20}
price_dict["watermelon"]=10
print(price_dict)
price_dict["apple"]=0
print(price_dict)
del price_dict["banana"]
print(price_dict)
Avg_price=(price_dict["apple"]+price_dict["orange"]+price_dict["grape"]+price_dict["kiwi"]+price_dict["mango"]+price_dict["watermelon"])/len(price_dict)
print(Avg_price)
minm,maxm=None,None
for value in price_dict.values():
    if minm==None:
        minm=value
    else:
        if value <minm:
            minm=value
    if maxm==None:
        maxm=value
    else:
        if value >maxm:
            maxm=value
print("Maximum price: " + str(maxm))
print("Minimum price: " + str(minm))

#Task 4 Combined Operation
print("\n\nTask 4 Combined Operation\n")

products=["apple","fish","chicken","cococola","chips","ketchup"]
price_dict={"apple":20,"fish":30,"chicken":40,"cococola":60,"chips":80,"ketchup":20}
catelog=[("apple",20,"fruits"),("fish",30,"meat"),("chicken",40,"meat"),("cococola",60,"snacks"),("chips",80,"snacks"),("ketchup",20,"snacks")]
print(catelog)
category_to_products={}
print(category_to_products)
for product in catelog:
    if product[2] not in category_to_products:
        category_to_products[product[2]]=[]
    category_to_products[product[2]].append(product[0])
mc,mp=None,None
print(category_to_products)
for category, products in category_to_products.items():
    if mc==None:
        mc=category
        mp=len(products)
    else:
        if len(products)>mp:
            mc=category
            mp=len(products)
print("Category with maximum products: " + mc + " with " + str(mp) +" products")


