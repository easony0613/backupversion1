'''
Purpose of program: make a takeaway order system for customers
Written by: Eason Yang
Date: 02/05/23
Version one: Taking one order, choose one item, displaying the order details and money
Version two: Validating customer name, phone number, order amount and typing numbers to order instead of writing
the name of the item.
Version three: allowing customer to add an order, delete an order, view their order, or confirm and finish their order
'''
def print_menu():
        '''prints out the menu in a pretty way'''
        print()
        print(f"******** Menu ********")
        print()
        for i in menu:
                print(f"{i:<25} ${menu[i]:.2f}")


def num_there(s):
    '''checks if there are numbers in a string'''
    '''URL: https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number'''
    return any(i.isdigit() for i in s)

def selecting_choice(order):
       '''making the customer select from numbers'''
       order = input("Enter item numbers to order: ")
       while order not in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
              order = input("Choose from the following options: ")

       if order == "1":
              order = "1. chicken fried rice"
       elif order == "2":
              order = "2. beef fried rice"
       elif order == "3":
              order = "3. egg fried rice"
       elif order == "4":
              order = "4. roast pork fried rice"
       elif order == "5":
              order = "5. combination fried rice"
       elif order == "6":
              order = "6. chicken noodle"
       elif order == "7":
              order = "7. beef noodle"
       elif order == "8":
              order == "8. honey chicken noodle"
       elif order == "9":
              order = "9. singapore fried noodle"
       elif order == "10":
              order = "10. egg foo yong"
       elif order == "11":
              order = "11. chicken egg foo yong"
       else:
              order = "12. beef egg foo yong"

       return order

def printing_details():
       print()
       for info in credentials:
        print(info, credentials[info])
       
       


# making a dictionary displaying the menu with items and their prices
menu = {"1. chicken fried rice" : 17,
        "2. beef fried rice" : 17.5,
        "3. egg fried rice" : 14.5,
        "4. roast por fried rice" : 18,
        "5. combination fried rice" : 18,
        "6. chicken noodle" : 17,
        "7. beef noodle" : 17.5,
        "8. honey chicken noodle" : 17.5,
        "9. singapore fried noodle": 18,
        "10. egg foo yong" : 15.5,
        "11. chicken egg foo yong" : 18.5,
        "12. beef egg foo yong" : 18.5,
}

# a phone number must have no less than or more than 10 numbers
MINIMUM_AND_MAXIMUM_NUMBER = 10
list_of_function = ["Order more items", "Delete an order", "View your order", "Finish your order"]

# asking for the customers details
name = input("Enter your full name: ")

while num_there(name) != False:
        print("Sorry no numbers, please enter your name")
        print()
        name = input("Enter your full name: ")

phone_number = input("Enter your phone number: ")

# isdigit() checks if the input are all numbers and return a boolean value.
# even if the customer enters a number, it has to be no less than or more than 10
while phone_number.isdigit() != True or len(phone_number) != MINIMUM_AND_MAXIMUM_NUMBER:
       print("Invalid phone number")
       print()
       phone_number = input("Enter your phone number: ")


# printing the menu
print_menu()

# asking the customer what they would like to order
order = ""
order = selecting_choice(order)

# program will keep on asking if order not in menu. when order is in menu, then amount of that order will be asked. 

while True:
       try:
              amount = int(input("How many would you like to order(maximum of 5): "))
              if amount < 1 or amount > 5:
                     print("Please enter correctly")
                     print()
              else: 
                     break
                     

       except ValueError:
              print()
              print("Error please enter correctly")


# this will calculate the total price of the order placed times by how much the customer wanted. 
total = (menu[order] * amount)
print(f"The total price is ${total:.2f}.")

# farewell message
'''link URL is https://www.youtube.com/watch?v=-7xg8pGcP6w'''
# storing customer infos in a dictionary
credentials = {"name:": name, "phone:" : phone_number, "item:" : order, "amount:" : amount, "price" : total}

print()
for i, items in enumerate(list_of_function, 1):
       print(i, items)

choice = input("Enter the numbers for your choice: ")
new_order = ""
new_amount = ""

if choice == "1":
       print_menu()
       selecting_choice(new_order)
       new_amount = int(input("How many would you like to order(maximum of 5): "))

       credentials[new_order] = new_amount

printing_details()

       

       



# farewell message