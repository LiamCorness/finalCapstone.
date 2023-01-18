
#========The beginning of the class==========
class Shoe:
    # Initilalize shoe object and parameters
    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Method to get shoe cost
    def get_cost(self):

        return (f"The cost of {self.product} is R{self.cost}")

    # Method to get shoe quantity
    def get_quantity(self):

        return (f"The quantity {self.product} is {self.quantity}")

    # Return a string representation of the object
    def __str__(self):

        return (f"""
country : {self.country}
code : {self.code}
product : {self.product}
cost : {self.cost}
quantity : {self.quantity}

""")

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
# Function to read data about shoes from the text file
# It skips the first line and ceats a shoe object with every other line and adds to shoe list
# raises error if file not found
    try:
        with open ("inventory.txt", "r") as f:

            first_line = True

            for line in f:

                if first_line:
                    first_line = False
                    continue
                
                line = line.strip().split(",")

                shoe = Shoe(line[0], line[1], line[2], int(line[3]), int(line[4]))

                shoe_list.append(shoe)

    except FileNotFoundError:

        print ("inventory.txt not found")


def capture_shoes():
# Funtion to capture data about shoes 
# Takes input to create a new shoe object and adds it to the shoe list
# Handles empty inputs and negative values
    print ("\nEnter Data about Shoe\n")

    country = input("Enter data for Country : ")
    while not country:
        print ("Country cannot be empty")
        country = input("Enter data for country")

    code = input("Enter code : ")
    while not code:
        print ("Code cannot be empty")
        code = input("Enter code")

    product = input("Enter product name : ")
    while not product:
        print ("product cannot be empty")
        product = input("Enter product name")
    
    while True:
        try:
            cost = int(input("Enter cost : "))
            if cost < 0 :
                print ("Cost cannot be negative")
                break
            else:
                break
        except ValueError:
            print ("Invalid input")

    while True:
        try:
            quantity = int(input("Enter quantity : "))
            if quantity < 0 :
                print ("Quantity cannot be negative")
                break
            else:
                break
        except ValueError:
            print ("Invalid input")

    shoe_to_capture = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe_to_capture)

    print ("Shoe added to inventory")

def view_all():

    # function to view all shoes in the list
    for shoe in shoe_list:

        print (shoe.__str__())

def re_stock():

# Function to find the soes with lowest quantity and ive option to add more

# Creates an empty list to store quantity values, find min quantity the iterates through the shoe list to see if a shoe object has that quantity
#
    quantity_list = []

    for shoe in shoe_list:

        quantity_list.append(shoe.quantity)

    min_quant = min(quantity_list)

    print(min_quant)

    for shoe in shoe_list:

        if shoe.quantity == min_quant:

            lowest_quant = shoe

            print (lowest_quant)

            ask = input (f"\n{shoe.product} (Code : {shoe.code}) has the lowest stock. Do you want to add more yes/no : ").lower()
            
            if ask == "yes":
            # add more shoes
                while True:
                    try:
                        to_add = int(input("Enter how many shoes you want to add : "))
                        break
                    except ValueError:
                        print ("Please enter a number")

                shoe.quantity += to_add

                print(f"{to_add} {shoe.product}'s have been added")

                # update text file
                with open ("inventory.txt", "w") as f:
                    f.write(f"Country,Code,Product,Cost,Quantity\n")

                    for shoe in shoe_list:

                        f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

def seach_shoe():
    # Function to search for shoe by code
    # If code is not found raise error
    while True:
        search_code = input("Enter the code of the shoe you are searching for : ")
        if not search_code:
            print("code cannot be empty")
            continue
        break

    shoe_found = False
    for line in shoe_list:
        if line.code == search_code:
            print (line)
            shoe_found = True
            break
    if not shoe_found:
        print (f"Shoe with code {search_code} not found")

def value_per_item():
    # Function to show value of each shoe

    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity

        print (f"{shoe.product}({shoe.code}) value is : R{value}\n")

def highest_qty():
    # Function to show the shoe with the highest quantity as for sale.
    highest_q_list = []

    for shoe in shoe_list:

        highest_q_list.append(shoe.quantity)

    highest_quant = max(highest_q_list)

    for shoe in shoe_list:

        if shoe.quantity == highest_quant:

            print (f"{shoe.product} is for sale\nCost : r{shoe.cost}\nQuantity : {shoe.quantity}")


#==========Main Menu=============
    
read_shoes_data ()

while True:
    
    menu = input("""
    Select one of the options below :

    capture data

    view all

    re stock

    search

    value per item

    highest quantity

    : """).lower()

    if menu =="capture data":

        capture_shoes()

    elif menu == "view all":

        view_all()

    elif menu == "re stock":

       print(re_stock())

    elif menu == "search":

        seach_shoe()

    elif menu == "value per item":

        value_per_item()
    
    else:

        if menu == "highest quantity":

            highest_qty()