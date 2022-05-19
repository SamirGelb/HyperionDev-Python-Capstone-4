# Importing the Shoe class from the class file
from L1T29_class import Shoe

# Defining the read_shoes_data function
def read_shoes_data():

    # Using a try and except block
    # I open the inventory.txt file
    try:
        f = open("inventory.txt", "r")
        f.readline()
        for line in f:
            # I strip each line and
            # make the attributes from the Shoe class
            # align with each item in the list
            country, code, product, cost, quantity = line.strip().split(",")
            # I then append the attributes to the shoe list
            shoe_list.append(Shoe(country, code, product, int(cost), int(quantity)))

    # If the file does not exist, the user is shown an error message 
    except FileNotFoundError:
        print("File not found: inventory.txt")

# Defining a function to update the text file
def update_file():

    # Creating an object for the first line in the file
    data = f"Country,Code,Product,Cost,Quantity"

    # Looping over each shoe in the list
    for shoe in shoe_list:

        # Updating the object to include the info about each shoe
        # and calling the write_to_file method from the class
        data += "\n" + shoe.write_to_file()

        # Writing the data to the text file
        with open("inventory.txt", "r+") as f:
            f.write(data)

# Defining the function capture_shoes
# to allow the user to add a shoe to the shoe list
def capture_shoes():
    
    # I ask the user to input the shoe details
    country = input("Please enter your country: ")
    code = input("Please enter your product code: ")
    product = input("Please enter your product name: ")
    cost = input("Please enter the cost of the product: ")
    quantity = input("Please enter how much stock of the shoe you have: ")

    # I then append the details into the list
    shoe_list.append(Shoe(country, code, product, int(cost), int(quantity)))

# Defining a function to view all
# The shoes in the list
def view_all():
    # I loop over each item in the list
    for shoe in shoe_list:
        # I then print all the information about the shoe
        print(shoe)

# Defining the re_stock function
def re_stock():
    # Defining an empty index to find the shoe
    index = 0

    # Calling the get_quantity() function from the shoe class to 
    # extract the shoe quantity from the list
    min_quantity = shoe_list[index].get_quantity()

    # Looping over each shoe to find the lowest quantity
    for i, shoe in enumerate(shoe_list):
        if shoe.get_quantity() < min_quantity:

            # Finding the shoe with the lowest quantity
            min_quantity = shoe.get_quantity() 
            index = i
    
    # Displaying the information about the shoe to the user
    print(f"""The shoe with the lowest quantity is: 
{shoe_list[index]}""")
    print("")

    # I present the user with the option to update the quantity of the shoe
    menu2 = input("Would you like to update this quantity Y/N? ")
    if menu2 == "Y":
        # If the user chooses to update the quantity of the shoe,
        # They are presented with an input to change the quantity
        shoe_list[index].quantity = int(input("Please enter the new quantity: "))
        # I then call the update_file function
        # and print a message for the user
        update_file()
        print("Shoe quantity updated\n")

    # If the user chooses not to update the quantity
    # I print an appropriate message
    if menu2 == "N":
        print("Shoe quantity not updated.\n") 

# Defining the search_shoe function
def search_shoe(code):

    # I loop through the list
    for shoe in shoe_list:
        # if the code entered by the user matches the shoe code then
        # the function returns the searched for shoe
        if shoe.code == code:
            return shoe

    # If the shoe does not exist the user is told as much
    return f"Product code {code} not found\n"

# Defining a function to calculate the value of each shoe
def value_per_item():
    # I loop over each shoe
    for shoe in shoe_list:
        # Extracting the cost and quantity for each shoe from the shoe class
        value = shoe.cost * shoe.quantity
        # Printing the value for each shoe
        print(f"""{shoe}
Value: {value}
""")

def highest_qty():
    # Defining an empty index to find the shoe
    index = 0

    # Calling the get_quantity() function from the shoe class to 
    # extract the shoe quantity from the list
    max_quantity = shoe_list[index].get_quantity()

    # Looping over each shoe to find the highest quantity
    for i, shoe in enumerate(shoe_list):
        if shoe.get_quantity() > max_quantity:

            # Finding the shoe with the highest quantity
            max_quantity = shoe.get_quantity() 
            index = i
    
    # Displaying the information about the shoe to the user
    # and marking it for sale
    print(f"""{shoe_list[index]}\n
This shoe is marked for sale!""")

# Defining an empty shoe list
shoe_list = []

# Calling the read_shoes_data() function
read_shoes_data()

while True:
    # Presenting the user with a menu
    menu = input("""What would you like to do?
add - add shoes
view all - view all shoes
restock - find the item with the lowest quantity in order to restock it
search - search shoes by product code
sale - find the item with the highest quantity
value - calculate the value of each item
: """).casefold()
# I use the casefold() function to mitigate 
# for random capitals in the user input

    if menu == "add":
        # If the user chooses to add a shoe
        # The capture_shoes() function is called
        capture_shoes()

    elif menu == "search":
        # If the user chooses to search for a shoe
        # They are asked for the shoe's product code
        code = input("Please enter the product code for the shoe you wish to find: ")
        
        # Then printing the shoe
        print(f"{search_shoe(code)}\n")

    elif menu == "view all":
        # If the user chooses to view all shoes
        # The view_all() function is called
        view_all()

    elif menu == "restock":
        # If the user chooses to find the shoe with the lowest quantity
        # The re_stock() function is called
        re_stock()

    elif menu == "sale":
        # If the user chooses to find the item with the highest quantity
        # The highest_qty() function is called
        highest_qty()

    elif menu == "value":
        # If the user chooses to find the value of each shoe
        # The value_per_item() function is called
        value_per_item()
    
    # If the user types anything else
    # An exit message is printed
    else:
        print("Must be an Adidas fan.\n")