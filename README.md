Authors: Joshena Allen and Deborah Williams
Date Created: April 05, 2025
Course: ITT103
GitHub Public URL to Code:

Program Purpose
The program is a Python-based Point-of-Sale (POS) system designed for Best Buy Retail Store. It allows cashiers to manage customer transactions and inventory, while managers have additional privileges to manage stock levels, prices, and sales-related information.

The key features of this system are:
1. User Authentication - cashiers and managers can log in
2. Inventory Management - for managers - add and remove stock
3. Price and Sales Tax Adjustment - for managers
4. Discount Handling
5. Cart Management - for cashiers- adding and removing items from the cart
6. Checkout and receipt generation - for cashiers
7. Sales history - for managers- tracking and viewing the sales each cashier made

How to Run it:
1. Clone the repository containing the source code on the local machine
2. Install Python - Ensure to have Python 3.x installed
3. Run the code: 
   I. Open a terminal or command prompt
   II. navigate to where the Python file is located using the cd command
   III. Run the program by using this command: 
		python best_buy_pos_system.py

Login and Usage:
The program will prompt you to enter a username and password.

	Manager:
	Username: Admin
	Password: Admin2025

	Cashiers:
	Username: Cashier1 or Cashier2
	Password: Cashier12025 or Cashier22025

After logging in, the program will display the relevant menu

Required Modification:
Potential modifications can improve this version of the POS system:

Inventory Data Management 
A more secure user authentication system
Creation of a sales report

Assumptions and Limitations:
The program assumes that the user has basic knowledge of how to run Python scripts.
The POS system is designed for small retail stores.

Limitations:

The inventory is not connected to a real database, so it is limited to the sample included in the code. 

The program does not handle advanced features such as barcode scanning and external payment systems.
