from tabulate import tabulate

class Shoe():
    """ This class will create a Shoe object with 5 attributes about the shoes
        in stock """

    
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)


    # Define function to display all objects from inventory file in a table format   
    def read_data(self):
        try:
            with open('inventory.txt', 'r') as invent_file:
                info = []
                for line in invent_file:
                    line.split("\n")
                    info.append(line.split(","))
            print(tabulate(info))
        except FileNotFoundError:
            print("The inventory file cannot be found.")


    # Define function to search for specific shoe code
    def search(shoe):   
        if shoe.code == code_search:
            print("Search Results:\n")
            print(f"~ {shoe.country} - {shoe.code} - {shoe.product} - {shoe.cost} - {shoe.quantity}")


    # Define function to sort objects by lowest quantity, add 20 units to restock quantity
    def restock(shoe):
        shoe_list.sort(key=lambda x: x.quantity)
        shoe_list[0].quantity += 20
        print(f"Item with least stock, {shoe_list[0].product}: restocked by 20 units.\nNew item amount:")
        print(f"{shoe_list[0].country} - {shoe_list[0].code} - {shoe_list[0].product} - {shoe_list[0].cost} - {shoe_list[0].quantity}")


    # Define function to sort objects by highest quantity and mark for sale
    def mark_for_sale(shoe):
        shoe_list.sort(key=lambda x: x.quantity, reverse = True)
        print(f"Item with highest stock, {shoe_list[0].product}: marked for sale.\n")
        print(f"FOR SALE**{shoe_list[0].country} - {shoe_list[0].code} - {shoe_list[0].product} - {shoe_list[0].cost} - {shoe_list[0].quantity}")


# Define subclass to add 6th column 'value per item'
class Value(Shoe):
    """ This is a subclass that will use the same attributes as a Shoe object
        with the addition of a 6th attribute for the value of shoes in stock
    """

    
    def __init__(self, country, code, product, cost, quantity, value):
        super().__init__(country, code, product, cost, quantity)


# ************************************MAIN LOGIC************************************

# Welcome user and request menu option
print("Welcome to the inventory Application\n")
choice = input("Would you like to:\n1) Calculate value per item\n2) Search for a Shoe by code\n\
3) Restock a Shoe\n4) Mark a shoe for sale\n5) View all stock\n")

# Read information frrom text file and append to 'info' list
# If text file does not exist, ask user to create/find one
try:
    with open('inventory.txt', 'r') as invent_file:
        info = []
        for line in invent_file:
            line.split("\n")
            info.append(line.split(","))

except FileNotFoundError:
    print("The inventory file cannot be found.")
    
# Create 5 objects from information in 'info' list                         
try:
    shoe_list = [Shoe(info[1][0],info[1][1],info[1][2],info[1][3],info[1][4]),
                 Shoe(info[2][0],info[2][1],info[2][2],info[2][3],info[2][4]),
                 Shoe(info[3][0],info[3][1],info[3][2],info[3][3],info[3][4]),
                 Shoe(info[4][0],info[4][1],info[4][2],info[4][3],info[4][4]),
                 Shoe(info[5][0],info[5][1],info[5][2],info[5][3],info[5][4])]

# If user chooses 1, calculate value per item and write to 'inventory.txt' file
    if choice == "1":
        for shoe in shoe_list:
            shoe.value = int(shoe.cost) * int(shoe.quantity)

        with open('inventory.txt', 'w') as write_value_column:
            write_value_column.write("Country,Code,Product,Cost,Quantity,ValuePerItem")
            for shoe in shoe_list:
                write_value_column.write(f"\n{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity},{shoe.value}")
        print("Value per item calculated and written to file 'inventory.txt'")
 
# if user choices 2, request code from user to search with and call search function
    elif choice == "2":
        code_search = input("\nPlease enter a shoe code to search: ")

        for shoe in list(shoe_list):
            shoe.search()
        
# If user chooses 3, call restock function
    elif choice == "3":
        shoe_list[0].restock()

# If user chooses 4, call mark_for_sale function
    elif choice == "4":
        shoe_list[0].mark_for_sale()

# If user chooses 5, call read_data function
    if choice == "5":
        shoe_list[0].read_data()   

except:
    print("Please create/find the inventory.txt file to continue.")
