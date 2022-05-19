# Defining the class Shoe
class Shoe:
    
    # Assigning attributes in the constructor
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Defining the get_cost method
    # To return the cost of each shoe
    def get_cost(self):
        return self.cost
    
    # Defining the get_quantity method
    # To return the quantity of each shoe
    def get_quantity(self):
        return self.quantity
    
    # Defining a method to write to the text file
    def write_to_file(self):
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

    # Defining a string representation of the text file data
    def __str__(self):
        return f"""Country: {self.country}
Product Code: {self.code}
Shoe Name: {self.product}
Shoe Cost: {self.cost}
Quantity: {self.quantity}"""