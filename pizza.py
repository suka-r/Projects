

#imports
from datetime import datetime, timedelta
import os



#function
def pizza():
    
    #variables
    pize_size = None
    topping = None
    address_and_info = None
 
    welcome = """
Welcome to Eastglen Pizza Classroom delivery!
Would you like to start your order?
Press 'enter' to continue"""
 
 
    sizes = ["Small", "Medium", "Large"]
    topping_list = ["Onions", "Extra Cheese", "Peppers" , "Chicken",  "Mushroom", "Black olives" , "Pepperoni"]
    choices = ["A", "B", "C" , "D", "E" , "F" , "G" ]
    choices1 = ["a", "b", "c" , "d", "e" , "f" , "g" ]
    new_topping = []
    name = None
    address = None
    id = None
    counter1 = 0
    pizza_size_cost = 0
    topping_cost = 0
    
 
    os.system('cls' if os.name =='nt' else 'clear')
    print(welcome)
    q = input("")
    os.system('cls' if os.name =='nt' else 'clear')
    
    #start/input
    print(
        """
Hello student!
Please enter the following information to start your order""")
   
#info
    name = str(input("Name: "))
    name = name.capitalize()
    id = input("Student ID: # ")
    address= str(input("Classroom to deliver order to: "))
    print()
 
    address_and_info = [name, id, address]
    print(address_and_info)
   
    
 
    os.system('cls' if os.name =='nt' else 'clear')
 
#pizza size
    print("""
-----------------------------
        Pizza size
-----------------------------
  """)
    print()
    print("All pizzas include traditional sauce")
    print()
    print(""""
We offer the following size
A.Small   (10 inches) \t  $10.00
B.Medium  (12 inches) \t  $12.00
C.Large   (15 inches) \t  $15.00
 
Please press A for small and B for medium and C for large""")
 
    pizza_size = input("")
    
 
    if pizza_size == choices1[0]:
        pizza_size = sizes[0]
        pizza_size_cost = 10.00
    elif pizza_size == choices1[1]:
        pizza_size = sizes[1]
        pizza_size_cost = 12.00
    elif pizza_size == choices1[2]:
        pizza_size = sizes[2]
        pizza_size_cost = 15.00
 
 
    os.system('cls' if os.name =='nt' else 'clear')
 

#pizza toppings
    print("""
-----------------------------
        Pizza Toppings
-----------------------------
""")
    print()
    print("""We offer a variety of toppings
Please select the letter of your chosen topping and enter 'done' when finished""")
    print()
    print(topping)
 
    counter = 0
    for item in topping_list: #print list of toppings
        print("{}.{} \t $3.00" .format(choices[0+counter], item))
        counter += 1
   
    
    while topping != "done":
        topping =  input("Please select a letter: ")
        counter1 +=1
 
        if topping == choices1[0]:
            topping = topping_list [0]
            new_topping.append(topping)
 
        elif topping == choices1[1]:
            topping = topping_list [1]
            new_topping.append(topping)
 
        elif topping == choices1[2]:
            topping = topping_list [2]
            new_topping.append(topping)
 
        elif topping == choices1[3]:
            topping = topping_list [3]
            new_topping.append(topping)

        elif topping == choices1[4]:
            topping = topping_list [4]
            new_topping.append(topping)
        elif topping == choices1[5]:
            topping = topping_list [5]
            new_topping.append(topping)
        elif topping == choices1[6]:
            topping = topping_list [6]
            new_topping.append(topping)

    

    counter1= counter1 - 1
    topping_cost = counter1 * 3 #cost
    print(new_topping)
 
    print()
    print()
    #time
    time = input("Please enter the current time: ")
 
    return ( pizza_size, pizza_size_cost, new_topping, topping_cost, address_and_info)
 


#main
def main():
    """MAIN/output"""

    now = datetime.now() #current time
    result = now + timedelta(minutes=15) #adds 15 min because it's in school delivery and make
    time = f'{result:%B %d %Y %H:%M:%S}' 

    
    x = pizza ()
    os.system('cls' if os.name =='nt' else 'clear')
    print("""

Eastglen Pizza Classroom delivery
Order No. 35
------------------------------------------------------------------------
Order for Student {}, #{} delivered to room {} at Eastglen high school
{}
-----------------------------------------------------------------------
One {} pizza with traditional sauce        \t ${}
Extra Toppings                             \t ${}
    {} 

TOTAL                                      \t ${}
------------------------------------------------------------------------
Estimated delivery time {}
Thank You For Visiting Eastglen Pizza Classroom delivery!

""".format(x[4][0] , x[4][1], x[4][2] , now, x[0] , x[1] , x[3], x[2], x[1] + x[3] , time ))


if __name__ == "__main__":
    main()