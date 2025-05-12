# Inventory Management System 📈

## Description 📄
This is an inventory management system that allows users to perform the following operations:
- Add a new product to the inventory.
- Consult the details of a product.
- Update the price of a product.
- Delete a product from the inventory.
- Calculate the total value of the inventory.
- Exit the program.

## Requirements 🔧
- Python 3.x

## Execution Instructions 🛠

## ▶️ Step 1: Clone the Repository
Clone the GitHub repository (if you have uploaded it) or copy the code into a local file.

```bash
git clone https://github.com/menelikph/Inventory_Management_System.git
cd Inventory_Management_System
```

## ▶️ Step 2: Run the Program
Run the program using Python.

python inventory.py

## ▶️ Step 3: Navigate the Menu
Once the program is executed, the main menu will be displayed with the following options:

### ➕ Add a product:
- Enter the product name, price, and quantity.
- If the product already exists, an error message will be displayed.

### 🔍 Consult a product:
- Enter the product name.
- The details of the product will be displayed if it exists.

### 💵 Update the price of a product:
- Enter the product name.
- Enter the new price.
- If the product exists, the price will be updated.

### ➖ Delete a product:
- Enter the product name.
- If the product exists, it will be deleted from the inventory.

### 🖩 Calculate the total value of the inventory:
- The total value of all products in the inventory will be calculated and displayed.

### 🚶🏼‍♂️ Exit the program:
- Terminate the program.
- Examples of Input and Output Data

# Examples 🤔
### Example 1: Add a Product ➕
✅ Input:

      1. Add product
      Add new product, what is the name?: sugar
      This product already exists
      
❎ Input (new product):

      1. Add product
      Add new product, what is the name?: flour
      Price: 800
      Quantity: 10
      Product flour added successfully.
      
### Example 2: Consult a Product 🔍
✅ Input:

      2. Consult product
      What product do you want to search?: sugar
      The product is: sugar
      Price: 1000
      Quantity: 5
      
❎ Input (non-existent product):

      2. Consult product
      What product do you want to search?: rice
      This product doesn't exist
      
### Example 3: Update the Price of a Product 💵
✅ Input:

      3. Update price product
      Enter the name of the product to change its price: sugar
      New price: 1200
      New price updated successfully: 1200
      
❎ Input (non-existent product):

      3. Update price product
      Enter the name of the product to change its price: rice
      This product doesn't exist
      
### Example 4: Delete a Product ➖
✅ Input:

      4. Delete product
      What is the product you want to delete?: salt
      The product was deleted successfully

❎ Input (non-existent product):

      4. Delete product
      What is the product you want to delete?: tea
      This product doesn't exist
      
### Example 5: Calculate the Total Value of the Inventory 🖩
✅ Input:

      5. Calculate total
      Sum of products
      The total value of the products is: 16000
      
### Example 6: Exit the Program 🚶🏼‍♂️
✅ Input:

      6. Exit
      Leaving the program
      
# that's it! 🤸‍♀️
