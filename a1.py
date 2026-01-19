'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions. 

- You MUST complete the functions defined below, except the ones that are already defined. 
'''


def show_menu():
	'''
	Description: Prints the menu as shown in the PDF
	
	Parameters: No paramters
	
	Returns: No return value
	'''
	print("="*50)
	print((" "*20)+"MY BAZAAR"+(" "*20))
	print("="*50)
	print("Hello! Welcome to my grocery store!")
	print("Following are the products available in the shop:")
	print()
	print("-"*50)
	print("CODE | DESCRIPTION | CATEGORY    | COST (RS)")
	print("-"*50)
	print(" 0   | Tshirt      | Apparels    | 500 ")
	print(" 1   | Trousers    | Apparels    | 600 ")
	print(" 2   | Scarf       | Apparels    | 250 ")
	print(" 3   | Smartphone  | Electronics | 20,000 ")
	print(" 4   | iPad        | Electronics | 30,000 ")
	print(" 5   | Laptop      | Electronics | 50,000 ")
	print(" 6   | Eggs        | Eatables    | 5 ")
	print(" 7   | Chocolate   | Eatables    | 10 ")
	print(" 8   | Juice       | Eatables    | 100 ")
	print(" 9   | Milk        | Eatables    | 45 ")
	print("-"*50)
	print()

def get_regular_input():
	'''
	Description: Takes space separated item codes (only integers allowed). 
	Include appropriate print statements to match the output with the 
	screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i. 
	'''
	print('-'*50)
	print("ENTER ITEMS YOU WISH TO BUY ")
	order = list(map(int, input("Enter the item codes (space separated): ").split()))
	quantities = []
	valids = []
	for code in order:
		if code in range(10):
			valids.append(code)
		else:
			print(str(code)+" is an invalid item code.")
						
	for i in range(10):
		count = 0
		for v in valids:
			if i == v:
				count += 1
		quantities.append(count)
	print()
	return quantities

def get_bulk_input():
	'''
	Description: Takes inputs (only integers allowed) from a bulk buyer. 
	For details, refer PDF. Include appropriate print statements to match 
	the output with the screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	'''
	print("-"*50)
	print("ENTER ITEM AND QUANTITIES")
	print("-"*50)

	quantities = [0,0,0,0,0,0,0,0,0,0]
	while True:
		code_quantity = list(map(int, input("Enter code and quantity (leave blank to stop): ").split()))
		if len(code_quantity) == 0:
			print("Your order has been finalized.")
			print()
			break 

		code = int(code_quantity[0])
		quantity = int(code_quantity[1])
		if code in range(10) and quantity > 0:
			if code == 0:
				if quantity == 1:
					print("You added 1 Tshirt.")
				else:
					print("You added "+str(quantity)+" Tshirts.")
			elif code == 1:
				if quantity == 1:
					print("You added 1 Trouser.")
				else:
					print("You added "+str(quantity)+" Trousers.")
			elif code == 2:
				if quantity == 1:
					print("You added 1 Scarf.")
				else:
					print("You added "+str(quantity)+" Scarves.")
			elif code == 3:
				if quantity == 1:
					print("You added 1 Smartphone.")
				else:
					print("You added "+str(quantity)+" Smartphones.")
			elif code == 4:
				if quantity == 1:
					print("You added 1 iPad.")
				else:
					print("You added "+str(quantity)+" iPads.")
			elif code == 5:
				if quantity == 1:
					print("You added 1 Laptop.")
				else:
					print("You added "+str(quantity)+" Laptops.")
			elif code == 6:
				if quantity == 1:
					print("You added 1 Egg.")
				else:
					print("You added "+str(quantity)+" Eggs.")
			elif code == 7:
				if quantity == 1:
					print("You added 1 Chocolate.")
				else:
					print("You added "+str(quantity)+" Chocolates.")
			elif code == 8:
				if quantity == 1:
					print("You added 1 Juice box.")
				else:
					print("You added "+str(quantity)+" Juice boxes.")
			elif code == 9:
				if quantity == 1:
					print("You added 1 milk box.")
				else:
					print("You added "+str(quantity)+" milk boxes.")
			cur_quantity = quantities[code]
			quantities[code] = cur_quantity + quantity
		elif code in range(10) and quantity <= 0:
			print("Invalid quantity. Try again.")
		elif code not in range(10) and quantity > 0:
			print("Invalid code. Try again.")
		else:
			print("Invalid code and quantity. Try again.")
		print()
	return quantities		

def print_order_details(quantities):
	'''
	Description: Prints the details of the order in a manner similar to the
	sample given in PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: No return value
	'''
	print("-"*50)
	print("ORDER DETAILS")
	print("-"*50)
	count = 0
	for i in range(10):
		q = quantities[i]
		if  q == 0:
			item_costs.append(0)
		else:
			count += 1 
			if i == 0:
				amount = q * 500
				print("["+str(count)+"] Tshirt x "+str(q)+" = Rs 500 * "+str(q)+" = Rs "+str(amount))
				item_costs.append(amount)
			elif i == 1:
				amount = q * 600
				print("["+str(count)+"] Trouser x "+str(q)+" = Rs 600 * "+str(q)+" = Rs "+str(amount))
				item_costs.append(amount)
			elif i == 2:
				amount = q * 250
				print("["+str(count)+"] Scarf x "+str(q)+" = Rs 250 * "+str(q)+" = Rs "+str(amount))
				item_costs.append(amount)
			elif i == 3:
				amount = q * 20000
				print("["+str(count)+"] Smartphone x "+str(q)+" = Rs 20000 * "+str(q)+" = Rs "+str(amount))
				item_costs.append(amount)
			elif i == 4:
				amount = q * 30000
				print("["+str(count)+"] iPad x "+str(q)+" = Rs 30000 * "+str(q)+" = Rs "+str(amount))
				item_costs.append(amount)
			elif i == 5:
				amount = q * 50000
				print("["+str(count)+"] Laptop x "+str(q)+" = Rs 50000 * "+str(q)+" = Rs "+str(amount))
				item_costs.append(amount)
			elif i == 6:
				amount = q * 5
				print("["+str(count)+"] Eggs x "+str(q)+" = Rs 5 * "+str(q)+" = Rs "+str(amount))
				item_costs.append(amount)
			elif i == 7:
				amount = q * 10
				print("["+str(count)+"] Chocolate x "+str(q)+" = Rs 10 * "+str(q)+" = Rs "+str(amount))
				item_costs.append(amount)
			elif i == 8:
				amount = q * 100
				print("["+str(count)+"] Juice x "+str(q)+" = Rs 100 * "+str(q)+" = Rs "+str(amount))
				item_costs.append(amount)
			elif i == 9:
				amount = q * 45
				print("["+str(count)+"] Milk x "+str(q)+" = Rs 45 * "+str(q)+" = Rs "+str(amount))
				item_costs.append(amount)
	print("TOTAL COST = "+str(sum(item_costs)))
	print()
		
def calculate_category_wise_cost(quantities):
	'''
	Description: Calculates the category wise cost using the quantities
	provided. Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: A 3-tuple of integers in the following format: 
	(apparels_cost, electronics_cost, eatables_cost)
	'''
	print("-"*50)
	print("CATEGORY-WISE COST")
	print("-"*50)
	apparels_cost = sum(quantities[0:3])
	electronics_cost = sum(quantities[3:6])
	eatables_cost = sum(quantities[6:])
	if apparels_cost > 0:
		print("Apparels = Rs "+str(apparels_cost))
	if electronics_cost > 0:
		print("Electronics = Rs "+str(electronics_cost))
	if eatables_cost > 0:
		print("Eatables = Rs "+str(eatables_cost))
	#print()
	#print("TOTAL COST = "+str(apparels_cost+electronics_cost+eatables_cost))
	print()
	return (apparels_cost, electronics_cost, eatables_cost)

def get_discount(cost, discount_rate):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
	'''
	return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
	'''
	Description: Calculates the discounted category-wise price, if applicable. 
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'
	
	Returns: A 3-tuple of integers in the following format: 
	(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost). 
	'''
	print('-'*50)
	print("DISCOUNTS")
	print('-'*50)
	
	if apparels_cost >= 2000:
		apparels_discount = int(get_discount(apparels_cost,0.1))
		apparels_cost_new = apparels_cost - apparels_discount
		print("[APPARELS] Rs "+str(apparels_cost)+" - Rs "+str(apparels_discount)+" = Rs "+str(apparels_cost_new))
	else:
		apparels_discount = 0
		apparels_cost_new = apparels_cost

	if electronics_cost >= 25000:
		electronics_discount = int(get_discount(electronics_cost,0.1))
		electronics_cost_new = electronics_cost - electronics_discount
		print("[ELECTRONICS] Rs "+str(electronics_cost)+" - Rs "+str(apparels_discount)+" = Rs "+str(electronics_cost_new))
	else:
		electronics_discount = 0
		electronics_cost_new = electronics_cost

	if eatables_cost >= 500:
		eatables_discount = int(get_discount(eatables_cost,0.1))
		eatables_cost_new = eatables_cost - electronics_discount
		print("[EATABLES] Rs "+str(eatables_cost)+" - Rs "+str(eatables_discount)+" = Rs "+str(eatables_cost_new))
	else:
		eatables_discount = 0
		eatables_cost_new = eatables_cost

	print()
	print("TOTAL DISCOUNT = Rs "+str(electronics_discount+eatables_discount+apparels_discount))
	print("TOTAL COST = Rs "+str(apparels_cost_new+electronics_cost_new+eatables_cost_new))
	print()
	return (apparels_cost_new, electronics_cost_new, eatables_cost_new)


def get_tax(cost, tax):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
	'''
	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
	'''
	Description: Calculates the total cost including taxes.
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables' 
	
	Returns: A 2-tuple of integers in the following format: 
	(total_cost_including_tax, total_tax)
	'''
	print("-"*50)
	print("TAX")
	print("-"*50)
	eatables_tax = int(get_tax(eatables_cost,0.05))
	apparels_tax = int(get_tax(apparels_cost,0.1))
	electronics_tax = int(get_tax(electronics_cost,0.15))
	if apparels_cost > 0:
		print("[APARREL] Rs "+str(apparels_cost)+" * 0.10 = Rs "+str(apparels_tax))
	if electronics_cost > 0:
		print("[ELECTRONICS] Rs "+str(electronics_cost)+" * 0.15 = Rs "+str(electronics_tax))
	if eatables_cost > 0:
		print("[EATABLES] Rs "+str(eatables_cost)+" * 0.05 = Rs "+str(eatables_tax))

	total_tax = apparels_tax+electronics_tax+eatables_tax
	total_cost = apparels_cost+apparels_tax+electronics_cost+electronics_tax+eatables_cost+eatables_tax
	print()
	print("TOTAL TAX = Rs "+str(total_tax))
	print("TOTAL COST = Rs "+str(total_cost))
	print()
	return (total_cost, total_tax) 

def apply_coupon_code(total_cost):
	'''
	Description: Takes the coupon code from the user as input (case-sensitive). 
	For details, refer the PDF. Include appropriate print statements to match 
	the output with the screenshot provided in the PDF.
	
	Parameters: The total cost (integer) on which the coupon is to be applied.
	
	Returns: A 2-tuple of integers:
	(total_cost_after_coupon_discount, total_coupon_discount)
	'''
	print("-"*50)
	print("COUPON CODE")
	print("-"*50)
	total_coupon_discount = 0
	total_cost_after_coupon_discount = 0
	code = " "
	coupons = ["HELLE25","CHILL50",""]

	while True:
		code = input("Enter the coupon code(else leave blank): ").strip()
		if code in coupons:
			break
		print("Invalid coupon code. Try Again.")
		print()
	
	if code == "HELLE25":
		if total_cost >= 25000:
			total_coupon_discount = min(int(0.25*total_cost), 5000)
			total_cost_after_coupon_discount = total_cost - total_coupon_discount
			print("[HELLE25] min(10000, Rs "+str(total_cost)+" * 0.25) = Rs "+str(total_coupon_discount))
		else:
			total_cost_after_coupon_discount = total_cost
			print("No coupon code applied.")

	elif code == "CHILL50":
		if total_cost >= 50000:
			print(total_cost)
			total_coupon_discount = min(int(0.5*total_cost), 10000)
			total_cost_after_coupon_discount = total_cost - total_coupon_discount
			print("[CHILL50] min(10000, Rs "+str(total_cost)+" * 0.50) = Rs "+str(total_coupon_discount))
		else:
			total_cost_after_coupon_discount = total_cost
			print("No coupon code applied.")
		
	elif code == "":
		print("No coupon code applied.")
		total_cost_after_coupon_discount = total_cost
	print()

	print("TOTAL COUPON DISCOUNT = Rs "+str(total_coupon_discount))
	print("TOTAL COST = Rs "+str(total_cost_after_coupon_discount))
	return (total_cost_after_coupon_discount, total_coupon_discount)

def main():
	'''
	Description: This is the main function. All production level codes usually
	have this function. This function will call the functions you have written
	above to design the logic. You will see how splitting your code into specialised
	functions makes the code easier to read, write and debug. Include appropriate 
	print statements to match the output with the screenshots provided in the PDF.
	
	Parameters: No parameters
	
	Returns: No return value
	'''
	show_menu()
	choice = ""
	while True: 
		choice = input("Would you like to buy in bulk? (y or Y / n or N): ").strip()
		if choice in ['y','Y',"n","N"]:
			break
		else: 
			print("Wrong input")
	print()
	if choice == "n" or choice == "N":
		quantities = get_regular_input()
	elif choice == "y" or "Y":
		quantities = get_bulk_input()

	print_order_details(quantities)
	cost_tuple = calculate_category_wise_cost(item_costs)
	dicounted_cost_tuple = calculate_discounted_prices(cost_tuple[0],cost_tuple[1],cost_tuple[2])
	tax_tuple = calculate_tax(dicounted_cost_tuple[0],dicounted_cost_tuple[1],dicounted_cost_tuple[2])
	after_coupon_cost = apply_coupon_code(tax_tuple[0])
	
	print()
	print("Thank you for visiting!")

if __name__ == '__main__':
	item_costs = []
	main()
	
