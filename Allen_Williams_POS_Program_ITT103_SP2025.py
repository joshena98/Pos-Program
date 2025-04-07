import datetime

# User Information (For login)
users = {
    "Admin": {"role": "manager", "password": "Admin2025"}, # Admin credentials
    "Cashier1": {"role": "cashier", "password": "Cashier12025"}, # Cashier1 credentials
    "Cashier2": {"role": "cashier", "password": "Cashier22025"} # Cashier2 credentials
}

# Sales History of Cashiers
sales_history = {
    "Cashier1": [],
    "Cashier2": []
}

# Login Function: Handles user authentication (username/password validation)
def login():
    print("Login Required")
    username = input("Username: ").strip() # User enter username
    password = input("Password: ").strip() # User enter password
    if username in users and users[username]["password"] == password: # if credentials are correct
        print(f"Logged in as {username} ({users[username]['role']})") # user is logged in
        return users[username]["role"], username
    print("Invalid Credentials") # If credentials are incorrect
    return None, None



# Manager Features: Add stock for an item in the inventory
def add_stock(items):
    item = input("Item to restock: ").strip().title()  # Ask the manager for the item name
    if item in items:  # If item exists in inventory
        try:
            stock_quantity = int(input("Enter Quantity"))  # Ask for quantity to add
            items[item]['stock'] += stock_quantity  # Update stock level
            print(f"Updated: {item} now has {items[item]['stock']}")
        except ValueError:
            print("Invalid Amount")  # Error handling for invalid input
    else:
        print("Item not found.")  # If item doesn't exist in inventory


# Manager Features: Remove stock of an item from the inventory
def remove_stock(items):
    item = input("Enter the name of the item to be removed: ").strip().title()  # Ask the manager for the item name
    if item in items:  # If item exists in inventory
        try:
            stock_quantity = int(input("How much item to remove? "))  # Ask for quantity to remove
            if stock_quantity <= items[item]['stock']:  # Check if enough stock exists to remove
                items[item]['stock'] -= stock_quantity  # Update stock level
                print(f"The {item} now has {items[item]['stock']}")
            else:
                print("Insufficient amount in stock.")  # Error if not enough stock to remove
        except ValueError:
            print("Invalid quantity")  # Error handling for invalid input
    else:
        print("Item not found.")  # If item doesn't exist in inventory


# Manager Features: Change the price of an item
def price_change(items):
    item = input("Enter item name for price change: ").strip().title()  # Ask the manager for the item name
    if item in items:  # If item exists in inventory
        try:
            price = float(input("Enter new price: $"))  # Ask for new price
            items[item]['price'] = price  # Update the price of the item
            print(f"The price is updated for {item}: ${price:.2f}")
        except ValueError:
            print("Invalid Amount")  # Error handling for invalid price
    else:
        print("Item not found")  # If item doesn't exist in inventory


# Manager Features: Set a discount rate for the store
def discount_rate():
    global Discount_Rate
    try:
        rate = float(input("Enter new discount amount: "))  # Ask for new discount percentage
        Discount_Rate = rate  # Update the global discount rate
        print(f"Discount rate updated to {Discount_Rate * 100: .1f}%")  # Show the updated discount rate
    except ValueError:
        print("Invalid amount")  # Error handling for invalid input


# Manager Features: Set a sales tax rate for the store
def change_sales_tax():
    global Sales_Tax
    try:
        rate = float(input("Enter new sales rate: "))  # Ask for new sales tax rate
        Sales_Tax = rate  # Update the global sales tax rate
        print(f"Sales Tax updated to {Sales_Tax * 100: .1f}%")  # Show the updated tax rate
    except ValueError:
        print("Invalid Amount")  # Error handling for invalid input


# Main Function: Start the POS system and manage different user actions
def best_buy_retail_store():
    role = None
    username = None
    while role is None:
        role, username = login()  # Get and display user role after login
        if role is None:
            continue  # Retry if login fails

    store_name = "Best Buy Retail Store"
    grocery_stock = create_product_list()
    customer_cart = {}  # Empty cart for the customer

    while True:
        print(f"\n--- {store_name} POS ---")
        if role == "cashier":  # Cashier's available options
            print(
                "1. See what we have\n2. Add to cart\n3. Remove from cart\n4. See cart\n5. Checkout\n6. Leave\n7. Logout")
        elif role == "manager":  # Manager's available options
            print(
                "1. See inventory\n2. Add stock\n3. Remove stock\n4. Change prices\n5. Set discount rate\n6. Set sales tax\n7. View last 5 sales of cashier\n8. Logout")

        user_choice = input("Select an option: ")

        if role == "cashier":  # If logged in as cashier
            if user_choice == '1':  # View available items in inventory
                show_available_items(grocery_stock)
            elif user_choice == '2':  # Add an item to the cart
                put_item_in_cart(customer_cart, grocery_stock)
            elif user_choice == '3':  # Remove an item from the cart
                take_item_out_of_cart(customer_cart, grocery_stock)
            elif user_choice == '4':  # View the current cart
                cart_display(customer_cart)
            elif user_choice == '5':  # Checkout and generate receipt
                subtotal = give_a_discount(cart_display(customer_cart))  # Apply discounts if applicable
                final_due, amount_received, change_given = handle_payment(subtotal)  # Handle payment
                print_receipt(store_name, customer_cart, subtotal, subtotal * Sales_Tax, final_due, amount_received,
                              change_given, username)  # Print receipt

                # Save sale to sales history with cashier name
                if username in sales_history:
                    sales_history[username].append({
                        'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'cashier': username,
                        'items': {item: details['quantity'] for item, details in customer_cart.items()},
                        'total': final_due
                    })

                customer_cart.clear()  # Clear the cart after checkout

            elif user_choice == '7':  # Logout
                print("Logged out")
                return best_buy_retail_store()  # Restart POS system
            elif user_choice == '6':  # Exit the system
                print("Goodbye!")
                break

        elif role == "manager":  # If logged in as manager
            if user_choice == '1':  # View available items in inventory
                show_available_items(grocery_stock)
            elif user_choice == '2':  # Add stock to inventory
                add_stock(grocery_stock)
            elif user_choice == '3':  # Remove stock from inventory
                remove_stock(grocery_stock)
            elif user_choice == '4':  # Change the price of an item
                price_change(grocery_stock)
            elif user_choice == '5':  # Set a discount rate
                discount_rate()
            elif user_choice == '6':  # Set sales tax rate
                change_sales_tax()
            elif user_choice == '7':  # View sales history of a cashier
                view_previous_sales()
            elif user_choice == '8':  # Logout
                print("Logging Out")
                return best_buy_retail_store()
# Variables for discount and sales tax
Sales_Tax = 0.10
Discount_Rate = 0.05


# Creation of Product list with their relevant prices
def create_product_list():
    return {
        "Bread": {"price": 750, "stock": 50},
        "Milk": {"price": 380, "stock": 30},
        "Eggs": {"price": 480, "stock": 100},
        "Apples": {"price": 140, "stock": 75},
        "Natural Juice": {"price": 560, "stock": 40},
        "Cereal": {"price": 790, "stock": 60},
        "Coffee": {"price": 800, "stock": 25},
        "Tea": {"price": 400, "stock": 80},
        "Sugar": {"price": 280, "stock": 90},
        "Pasta": {"price": 150, "stock": 120},
        "Tomatoes": {"price": 200, "stock": 70}
    }


# Display the available items in the store's inventory
def show_available_items(grocery_items):
    print("\n--- Grocery Items ---")
    for item_name, item_details in grocery_items.items():
        print(f"{item_name}: ${item_details['price']:.2f} (We have {item_details['stock']} left)")
    print("----------------------")


# Cashier adds an item to the customer's cart
def put_item_in_cart(shopping_cart, grocery_items):
    item_to_add = input("What item would you like to add? ").strip().title()
    if item_to_add in grocery_items:  # Check if the item is in stock
        while True:
            try:
                quantity = int(input(f"How many {item_to_add}s would you like? "))
                if quantity > 0:  # Check if quantity is greater than zero
                    if grocery_items[item_to_add]['stock'] >= quantity:  # Check if enough stock exists
                        shopping_cart[item_to_add] = shopping_cart.get(item_to_add, {'quantity': 0, 'price':
                            grocery_items[item_to_add]['price']})
                        shopping_cart[item_to_add]['quantity'] += quantity
                        grocery_items[item_to_add]['stock'] -= quantity  # Update stock level
                        print(f"Added {quantity} {item_to_add}(s) to your cart.")
                        break
                    else:
                        print(f"Sorry, we only have {grocery_items[item_to_add]['stock']} {item_to_add}(s) left.")
                else:
                    print("Please enter amount greater than zero.")
            except ValueError:
                print("Please enter a numeric value.")
    else:
        print(f"We don't have {item_to_add} in stock.")


# Cashier removes an item from the cart
def take_item_out_of_cart(shopping_cart, grocery_items):
    item_to_remove = input("What item would you like to remove? ").strip().title()
    if item_to_remove in shopping_cart:
        while True:
            try:
                quantity_to_remove = int(input(f"How many {item_to_remove}s would you like to remove? "))
                if quantity_to_remove > 0:  # Check if quantity is greater than zero
                    if quantity_to_remove >= shopping_cart[item_to_remove]['quantity']:
                        grocery_items[item_to_remove]['stock'] += shopping_cart[item_to_remove][
                            'quantity']  # Return all stock to inventory
                        del shopping_cart[item_to_remove]  # Remove item from cart
                        print(f"{item_to_remove} was removed from your cart.")
                        break
                    else:
                        shopping_cart[item_to_remove]['quantity'] -= quantity_to_remove  # Update cart quantity
                        grocery_items[item_to_remove]['stock'] += quantity_to_remove  # Update inventory stock
                        print(f"Removed {quantity_to_remove} {item_to_remove}(s) from your cart.")
                        break
                else:
                    print("Please enter a number greater than zero.")
            except ValueError:
                print("Please enter a numeric value.")
    else:
        print(f"That item isn't in your cart.")


# Display the current cart to the customer
def cart_display(shopping_cart):
    if not shopping_cart:  # Check if cart is empty
        print("Your cart is empty.")
        return 0

    print("\n--- Your Shopping Cart ---")
    total_cost = 0
    for item_name, item_details in shopping_cart.items():
        item_total = item_details['quantity'] * item_details['price']
        print(f"{item_name}: {item_details['quantity']} x ${item_details['price']:.2f} = ${item_total:.2f}")
        total_cost += item_total  # Calculate total cost of items in cart
    print(f"---------------------------\nSubtotal: ${total_cost:.2f}")
    return total_cost  # Return total cost


# Apply discount if the subtotal is greater than $5000
def give_a_discount(subtotal_amount):
    discount_cutoff = 5000
    if subtotal_amount > discount_cutoff:  # If total is above the amount qualified for a discount
        discount_amount = subtotal_amount * Discount_Rate  # Calculate discount
        subtotal_amount -= discount_amount  # Apply discount to subtotal
        print(f"Discount (5% off over ${discount_cutoff:.2f}): -${discount_amount:.2f}")
        print(f"New Subtotal: ${subtotal_amount:.2f}")
    return subtotal_amount


# Handle payment process, including calculating tax and handling customer payment
def handle_payment(total_amount):
    tax_amount = total_amount * Sales_Tax  # Calculate sales tax
    final_total = total_amount + tax_amount  # Total after adding tax
    print(f"\nSales Tax ({Sales_Tax * 100}%): ${tax_amount:.2f}")
    print(f"Total: ${final_total:.2f}")

    while True:
        try:
            money_from_customer = float(input("How much money did the customer give you? $"))
            if money_from_customer >= final_total:  # Ensure customer gives enough money
                change_for_customer = money_from_customer - final_total  # Calculate change
                print(f"Change: ${change_for_customer:.2f}")
                return final_total, money_from_customer, change_for_customer  # Return transaction details
            else:
                print("Amount is insufficient.")  # Error if money given is insufficient
        except ValueError:
            print("Please enter a numeric value.")  # Error handling for invalid input


# Print the receipt after a transaction
def print_receipt(store_name, shopping_cart, subtotal_amount, tax_amount, total_paid, amount_given, amount_given_back, username):
    current_date = datetime.datetime.now()  # Get current date and time
    print("\n--- Receipt ---")
    print(f"{store_name.upper()}") # Display store name
    print(f"Cashier: {username}") # Display the Cashier name
    print(f"Date: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")  # Print date and time
    print("-" * 30)
    print("Items:")
    for item_name, item_details in shopping_cart.items():
        print(
            f"{item_name} ({item_details['quantity']} x ${item_details['price']:.2f}): ${item_details['quantity'] * item_details['price']:.2f}")
    print("-" * 30)
    print(f"Subtotal: ${subtotal_amount:.2f}")
    print(f"Sales Tax: ${tax_amount:.2f}")
    print(f"Total: ${total_paid:.2f}")
    print(f"Paid: ${amount_given:.2f}")
    print(f"Change: ${amount_given_back:.2f}")
    print("-" * 30)
    print("Thanks for shopping with us!")

# View the last 5 sales made by a cashier
def view_previous_sales():
    cashier = input("Enter the cashier username to view sales: ").strip()
    if cashier in sales_history:  # If sales history for the cashier exists
        print(f"\n---Last Sales for {cashier}---")
        if not sales_history[cashier]:
            print("No sales recorded")  # If no sales recorded for the cashier
        else:
            last_sales = sales_history[cashier][-5:]  # Get the last 5 sales
            for i, sale in enumerate(last_sales, 1):
                print(f"\n Sale {i} - Date: {sale['date']}")
                for item, stock_quantity in sale['items'].items():
                    print(f"{item}: {stock_quantity}")
                print(f"Total: ${sale['total']:.2f}")
    else:
        print("Cashier not found.")  # If no history exists for the cashier

if __name__ == "__main__":
    best_buy_retail_store()
