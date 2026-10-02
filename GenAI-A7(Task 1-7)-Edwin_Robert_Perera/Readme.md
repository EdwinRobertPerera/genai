# GenAI-A7 (Tasks 1–7) - Edwin Robert Perera

## File Name
`a7.py`

---

## Description

This Python program demonstrates the use of:

- Object-Oriented Programming (OOP)
- Classes and Objects
- Encapsulation (Private Attributes)
- Inheritance (Single Level)
- Polymorphism (Method Overriding)
- Abstraction (Abstract Base Classes)
- Magic Methods (`__str__`, `__add__`)
- Operator Overloading
- Real-world Integration (Inventory System)

The program contains seven independent tasks that showcase different Object-Oriented Programming concepts.

---

## Prerequisites

- Python 3.6 or higher installed on your computer.

To verify Python installation, run:

```bash
python --version
```

or

```bash
python3 --version
```

---

## How to Run the Program

### Step 1: Open Terminal / Command Prompt

Navigate to the folder containing the Python file.

Example (Linux/macOS):

```bash
cd ~/Documents/genai/GenAI-A7(Task\ 1-7)-Edwin_Robert_Perera
```

Example (Windows):

```bash
cd "C:\Users\YourUsername\Documents\genai\GenAI-A7(Task 1-7)-Edwin_Robert_Perera"
```

---

### Step 2: Run the Program

**Windows**

```bash
python a7.py
```

**Linux / macOS**

```bash
python3 a7.py
```

---

### Alternative Methods

#### Method 1: Using Absolute Path

```bash
python /home/edwin-robert-perera/Documents/genai/GenAI-A7(Task\ 1-7)-Edwin_Robert_Perera/a7.py
```

#### Method 2: VS Code Integrated Terminal

1. Open `a7.py` in VS Code
2. Press `Ctrl + ` ` (backtick) to open terminal
3. Type: `python a7.py`
4. Press Enter

#### Method 3: Run in Python Interactive Shell

```bash
python
>>> exec(open('a7.py').read())
```

---

## Program Contents

### Task 1 – Basic Class and Object Creation

- Creates a `Product` class with attributes: `name`, `price`, `category`
- Implements `get_info()` method to display product details
- Demonstrates object instantiation and method calling
- **Example Output**:
  ```
  Product name is Lays and it belongs to the category Chips and its price is 10 rps
  ```

---

### Task 2 – Encapsulation

- Implements private attribute `__price` using name mangling
- Creates getter method `get_price()` to access private attribute
- Creates setter method `set_price()` to modify private attribute
- Demonstrates controlled access to class data
- **Example Output**:
  ```
  120
  10
  ```

---

### Task 3 – Inheritance (Single Level)

- Creates `ElectronicProducts` class inheriting from `Product`
- Uses `super().__init__()` to call parent class constructor
- Adds new attribute `warranty_years`
- Overrides parent's `get_info()` method with extended functionality
- **Example Output**:
  ```
  product name is HP OMEN it belongs to Laptop, its price is 1,20,000 and it has a warranty for 2 Years year/years
  ```

---

### Task 4 – Polymorphism

- Creates two child classes: `Laptop` and `Mobile`
- Both inherit from `Product` but override `get_info()` differently
- Demonstrates same method name with different implementations
- Iterates through a list of objects, calling the same method with different outputs
- **Example Output**:
  ```
  HP OMEN is from Laptop category, its price is 1,20,000, it has 16GB RAM, 1TB SSD storage, RTX 3060 GPU and Intel i7 CPU
  Samsung Galaxy S21 is from Mobile category, its price is 70,000, it has 8GB RAM, 256GB storage and 64MP camera
  ```

---

### Task 5 – Abstraction

- Creates abstract base class `Payment` using `ABC` module
- Defines abstract method `process_payment(amount)`
- Implements two concrete classes:
  - `CreditCardPayment`: Processes credit card payments
  - `UPIPayment`: Processes UPI payments
- Demonstrates interface definition without implementation details
- **Example Output**:
  ```
  Processing credit card payment of 500 rps
  Processing UPI payment of 1000 rps
  ```

---

### Task 6 – Magic Methods & Operator Overloading

- Implements `__str__()` magic method for readable string representation
- Implements `__add__()` magic method to overload the `+` operator
- Allows combining product prices: `product1 + product2`
- Demonstrates special method definitions
- **Example Output**:
  ```
  Product(Lays, 10, Chips)
  Product(Pepsi, 50, Beverages)
  Combined price: 60 rps
  ```

---

### Task 7 – Mini Project: Simple Inventory System

Demonstrates integration of all OOP concepts through two classes:

#### Inventory Class
- **Attributes**: `products` (list of Product objects)
- **Methods**:
  - `add_product(product)` - Adds product to inventory
  - `remove_product(name)` - Removes product by name
  - `get_total_value()` - Calculates sum of all product prices
  - `show_all_products()` - Displays all products in inventory

#### Store Class
- **Attributes**: `store_name`, `inventory` (Inventory object)
- **Methods**:
  - `add_new_product(name, price, category)` - Creates Product and adds to inventory
  - `show_summary()` - Displays store statistics

#### How the System Works

1. Create a Store object with a store name
2. Add products using `add_new_product()`
3. View inventory details with `show_summary()`

- **Example Code**:
  ```python
  store = Store("TechHub Store")
  store.add_new_product("HP Laptop", 120000, "Electronics")
  store.add_new_product("Samsung Mobile", 70000, "Electronics")
  store.add_new_product("Lays Chips", 50, "Snacks")
  store.show_summary()
  ```

- **Example Output**:
  ```
  === TechHub Store Summary ===
  Total Items: 3
  Total Value: 190050 rps
  Products:
  - HP Laptop: 120000 rps (Electronics)
  - Samsung Mobile: 70000 rps (Electronics)
  - Lays Chips: 50 rps (Snacks)
  ```

---

## Complete Program Output

When you run `python a7.py`, the complete output is:

```
Product name is Lays and it belongs to the category Chips and its price is 10 rps
120
10
product name is HP OMEN it belongs to Laptop, its price is 1,20,000 and it has a warranty for 2 Years year/years
HP OMEN is from Laptop category, its price is 1,20,000, it has 16GB RAM, 1TB SSD storage, RTX 3060 GPU and Intel i7 CPU
Samsung Galaxy S21 is from Mobile category, its price is 70,000, it has 8GB RAM, 256GB storage and 64MP camera
Processing credit card payment of 500 rps
Processing UPI payment of 1000 rps
Product(Lays, 10, Chips)
Product(Pepsi, 50, Beverages)
Combined price: 60 rps

=== TechHub Store Summary ===
Total Items: 3
Total Value: 190050 rps
Products:
- HP Laptop: 120000 rps (Electronics)
- Samsung Mobile: 70000 rps (Electronics)
- Lays Chips: 50 rps (Snacks)
```

---

## OOP Concepts Summary

| Task | Concept | Key Points |
|------|---------|-----------|
| 1 | Classes & Objects | Blueprint creation, attributes, instance methods |
| 2 | Encapsulation | Private attributes using `__`, getters/setters |
| 3 | Inheritance | Child classes inherit from parent, `super()` keyword |
| 4 | Polymorphism | Method overriding, same interface, different behavior |
| 5 | Abstraction | Abstract base classes, abstract methods, interfaces |
| 6 | Magic Methods | `__str__()` for string representation, operator overloading |
| 7 | Integration | Composition, multiple classes working together |

---

## Troubleshooting

### Issue: "python: command not found"

**Solution**: Use `python3` instead
```bash
python3 a7.py
```

### Issue: "ModuleNotFoundError: No module named 'abc'"

**Solution**: `abc` is built-in. Ensure Python 3.6+ is installed
```bash
python --version
```

### Issue: "No output appears"

**Solution**: Verify all code is present in `a7.py` and run with:
```bash
python a7.py 2>&1
```

### Issue: Character encoding errors (Windows)

**Solution**: Change terminal encoding
```bash
chcp 65001
python a7.py
```

---

## File Structure

```
/home/edwin-robert-perera/Documents/genai/GenAI-A7(Task 1-7)-Edwin_Robert_Perera/
├── a7.py           # Main program file
└── README.md       # Documentation (this file)
```

---

## Key Features

✅ Pure Object-Oriented Programming (No imports except `abc`)
✅ No file handling or exception handling (as per requirements)
✅ Fully commented and documented
✅ Real-world practical example (Inventory System)
✅ Progressive difficulty from basic to complex concepts
✅ Reusable and extensible code structure

---

## How to Extend the Program

### Add a New Product Type (Task 4)

```python
class Tablet(Product):
    def __init__(self, name, price, category, screen_size, processor):
        super().__init__(name, category)
        self.price = price
        self.screen_size = screen_size
        self.processor = processor
    
    def get_info(self):
        print(f"{self.name}: {self.screen_size} screen, {self.processor} processor")
```

### Add a New Payment Method (Task 5)

```python
class WalletPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing wallet payment of {amount} rps")

wallet = WalletPayment()
wallet.process_payment(2000)
```

### Extend Store Functionality (Task 7)

```python
def remove_product(self, product_name):
    self.inventory.remove_product(product_name)

store.remove_product("Lays Chips")
store.show_summary()
```

---

## Notes

- Program redefines `Product` class multiple times (Tasks 1-4) for educational purposes
- Task 6 uses separate `Product6` class to demonstrate new concepts
- Task 7 uses `Product6` for the inventory system
- All concepts are independent and can be studied separately
- No external dependencies required

---

## Learning Outcomes

After completing this assignment, you will understand:

1. How to design and create classes
2. How to control data access with encapsulation
3. How to reuse code through inheritance
4. How to create flexible designs with polymorphism
5. How to define interfaces with abstraction
6. How to customize object behavior with magic methods
7. How to integrate multiple classes in real-world scenarios

---

## Author

**Edwin Robert Perera**

GenAI Assignment A7

---

## Date

September 6, 2026

---

*For questions or clarifications, refer to the inline comments in `a7.py`*