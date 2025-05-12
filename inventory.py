# Initialize with example in the inventory: products and their prices and quantities
inventory = {
    "sugar": {
        "price": 1000, 
        "quantity" : 5, 
    },
    "salt": {
        "price": 500, 
        "quantity" : 5, 
    }
}

def show_menu(): #Display the main inventory menu with available options.
    """
    Show the main inventory menu with available options. 
    This function prints a menu with numbered options for the user to choose. 
    """
    print("\033[1;35m") # Change the color of the text in the console to a "magenta" color
    print (("------- INVENTORY -------"))
    print("1. Add product")
    print("2. Consult product")
    print("3. Update price product")
    print("4. Delete product")
    print("5. Calculate total")
    print("6. Exit")
    print("-------------------------\n")# A line to separate the menu from other content

def valid_input_num(valid_num):
    """
    Prompt the user for a valid numeric input.
    This function continuously prompts the user until a valid integer is entered.
    
    :prompt: The message to display to the user.
    :return: The valid integer input from the user.
    """
    while True:
        valid = input(valid_num)
        if valid.isdigit():# Check if the input is a digit
            return int(valid) #Convert the input to an integer and return it
        else:
            print("\033[4;31m")# Change the color of the text to red
            print("enter a valid number")# Inform the user to enter a valid number

def find_product(name_product):
    """
    Check if a product exists in the inventory.
    This function checks if a given product name is a key in the inventory dictionary.
    
    :name_product: The name of the product to check.
    :return: True if the product exists, False if not exists.
    """
    if name_product in inventory:
        return True #return true 
    else:
        return False #return false

def add_product():
    """
    Add a new product to the inventory.
    This function prompts the user to enter the name, price, and quantity of a new product,
    and adds it to the inventory if it does not already exist.
    """
    name_product = input("add new product, what is the name?: ").lower().strip() #Get the product name in lower case and remove spaces at the beginning and end
    if  find_product(name_product): # Check if the product already exists
        print("\033[4;31m")
        print("\nthis product already exists")# Inform the user that the product already exists
    else:#if the product exists do:
        price = valid_input_num("price: ") # Get the price of the product and verify
        quantity = valid_input_num("quantity: ") # Get the quantity of the product
        print("\033[;32m")
        inventory[name_product] = {"quantity":quantity, "price":price} # Add the product to the inventory
        print(f"book {name_product} added successfully.") # Inform the user that the product was added successfully

def consult_product():
    """
    Consult the details of a product in the inventory.
    
    This function prompts the user to enter the name of a product and displays its details if it exists.
    """
    name = input("What product do you want to search?: ").lower().strip()  #Get the product name in lower case and remove spaces at the beginning and end
    if find_product(name):  # Check if the product exists
        print("\033[;32m") 
        print(f"The product is: {name}\nPrice: {inventory[name]['price']}\nQuantity: {inventory[name]['quantity']}")  # Display the product details
    else:
        print("\033[4;31m")  
        print("This product doesn't exist")  # Inform the user that the product does not exist

def update_price():
    """
    Update the price of an existing product in the inventory.
    
    This function prompts the user to enter the name of a product and a new price,
    and updates the price in the inventory if the product exists.
    """
    name_product = input("Enter the name of the product to change its price: ").lower().strip()  #Get the product name in lower case and remove spaces at the beginning and end
    if not find_product(name_product):  # Check if the product does not exist
        print("\033[4;31m")  
        print("This product doesn't exist")  # Inform the user that the product does not exist
    else:
        price = valid_input_num("New price: ")  # Get the new price of the product
        inventory[name_product]["price"] = price  # Update the price in the inventory
        print("\033[;32m") 
        print(f"New price updated successfully: {price}")  # Inform the user that the price was updated successfully
    
def del_product():
    """
    Delete a product from the inventory.
    This function prompts the user to enter the name of a product and deletes it from the inventory if it exists.
    """
    name_product = input("What is the product you want to delete?: ").lower().strip() #Get the product name in lower case and remove spaces at the beginning and end
    if not find_product(name_product):  # Check if the product does not exist
        print("\033[4;31m")  
        print("This product doesn't exist")  # Inform the user that the product does not exist
    else:
        del inventory[name_product]  # Delete the product from the inventory
        print("\033[;32m")  
        print("The product was deleted successfully")  # Inform the user that the product was deleted successfully


def sum_price():
    """
    Calculate and display the total value of all products in the inventory.
    
    This function iterates through the inventory, calculates the total value of all products,
    and displays the result.
    """
    total = 0 # Initialize the total value to 0
    print("sum of products") #Print a header for the sum of products
    for item in inventory.values(): # Iterate through each product in the inventory
        total = total + (item["price"] * item["quantity"]) # Calculate the total value of the product and add it to the total
    print("\033[;32m")
    print(f"the total of the products is: {total}") # Display the total value of the products

#finally!!!!
# Main loop to handle user interactions
while True:
    show_menu()  # Display the main menu
    print("\033[4;35m")  # Change the color of the text to magenta
    select = valid_input_num("Select an option: ")  # Prompt the user to select an option and verify
    match select:
        case 1:
            add_product()  # Add a new product to the inventory
        case 2:
            consult_product()  # Consult the details of a product
        case 3:
            update_price()  # Update the price of a product
        case 4:
            del_product()  # Delete a product from the inventory
        case 5:
            sum_price()  # Calculate and display the total value of the inventory
        case 6:
            print("\033[4;36m")  # Change the color of the text to cyan
            print("Leaving the program")  # Inform the user that the program is exiting
            break  # Exit the main loop
        case _:
            print("\033[4;31m")  # Change the color of the text to red
            print("Invalid option. Please try again.\n")  # Inform the user that the selected option is invalid