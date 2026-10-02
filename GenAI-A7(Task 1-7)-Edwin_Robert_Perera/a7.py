#Task 1 : Basic Class and Object Creation
class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def get_info(self):
        print(f"Product name is {self.name} and it belongs to the category {self.category} and its price is {self.price} rps")
    
    # Task 6: Magic Methods & Operator Overloading
    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"
    
    def __add__(self, other):
        return self.price + other.price

lays = Product("Lays", "10", "Chips")
lays.get_info()


#Task 2 : Encapsulation 
class Product:
    def __init__(self, name, category):
        self.name = name
        self.__price = 120
        self.category = category
    
    def get_info(self):
        print(f"Product name is {self.name} and it belongs to the category {self.category} and its price is {self.get_price()} rps")
    
    def set_price(self, price):
        self.__price = price
    
    def get_price(self):
        return self.__price

lays = Product("lays", "chips")
print(lays.get_price())
lays.set_price(10)
print(lays.get_price())


#Task 3 : Inheritance(Single Level)
class ElectronicProducts(Product):
    def __init__(self, name, price, category, warranty_years):
        super().__init__(name, category)
        self.price = price
        self.warranty_years = warranty_years
    
    def get_info(self):
        print(f"product name is {self.name} it belongs to {self.category}, its price is {self.price} and it has a warranty for {self.warranty_years} year/years")

hpomen = ElectronicProducts("HP OMEN", "1,20,000", "Laptop", "2 Years")
hpomen.get_info()


#Task 4 : Polymorphism
class Laptop(Product):
    def __init__(self, name, price, category, ram, storage, gpu, cpu):
        super().__init__(name, category)
        self.price = price
        self.ram = ram
        self.storage = storage
        self.gpu = gpu
        self.cpu = cpu
    
    def get_info(self):
        print(f"{self.name} is from {self.category} category, its price is {self.price}, it has {self.ram} RAM, {self.storage} storage, {self.gpu} GPU and {self.cpu} CPU")


class Mobile(Product):
    def __init__(self, name, price, category, ram, storage, camera):
        super().__init__(name, category)
        self.price = price
        self.ram = ram
        self.storage = storage
        self.camera = camera
    
    def get_info(self):
        print(f"{self.name} is from {self.category} category, its price is {self.price}, it has {self.ram} RAM, {self.storage} storage and {self.camera} camera")

list = [Laptop("HP OMEN", "1,20,000", "Laptop", "16GB", "1TB SSD", "RTX 3060", "Intel i7"), Mobile("Samsung Galaxy S21", "70,000", "Mobile", "8GB", "256GB", "64MP")]

for i in list:
    i.get_info()


#Task 5 : Abstraction
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount} rps")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of {amount} rps")

# Test
card = CreditCardPayment()
upi = UPIPayment()

card.process_payment(500)
upi.process_payment(1000)


#Task 6: Magic Methods & Operator Overloading
class Product6:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"
    
    def __add__(self, other):
        return self.price + other.price

# Test
product1 = Product6("Lays", 10, "Chips")
product2 = Product6("Pepsi", 50, "Beverages")

print(str(product1))
print(str(product2))
print(f"Combined price: {product1 + product2} rps")


#Task 7: Mini Project - Simple Inventory System
class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def remove_product(self, name):
        self.products = [p for p in self.products if p.name != name]
    
    def get_total_value(self):
        return sum(int(str(p.price).replace(',', '')) for p in self.products)
    
    def show_all_products(self):
        for product in self.products:
            print(f"- {product.name}: {product.price} rps ({product.category})")

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()
    
    def add_new_product(self, name, price, category):
        product = Product6(name, price, category)
        self.inventory.add_product(product)
    
    def show_summary(self):
        total_items = len(self.inventory.products)
        total_value = self.inventory.get_total_value()
        print(f"\n=== {self.store_name} Summary ===")
        print(f"Total Items: {total_items}")
        print(f"Total Value: {total_value} rps")
        print("Products:")
        self.inventory.show_all_products()

# Test
store = Store("TechHub Store")
store.add_new_product("HP Laptop", 120000, "Electronics")
store.add_new_product("Samsung Mobile", 70000, "Electronics")
store.add_new_product("Lays Chips", 50, "Snacks")
store.show_summary()