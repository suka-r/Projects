#imports
import os
import time 

#function 1 - base
def products (something,products_base ):
    counter = 1
    product = input("Product {}: " .format(counter))
    product = product.lower()
    global list_of_products
    list_of_products = []
    products_inventory = {}
    products_base.write("Products"+"\n")
    while product:
        counter += 1
        products_base.write( product +"\n" )
        list_of_products.append(product)
        something[product] = 0
        product = input("Product {}: " .format(counter))
        product.lower()

    products_base.close()
    products_inventory = something.copy()
    return(products_inventory)


#function 2 - stock file 
def stock(something, products_stock): 
    stock_inventory = {}
    key = list(something.keys()) 
    products_stock.write("Product" +"\t" + "Stock" +"\n" )
    for item in key:
        stock_for_each_item = input("{}: " .format(item))
        products_stock.write(item +"\t" )
        products_stock.write(stock_for_each_item +"\n" )
        something[item] = stock_for_each_item 
    products_stock.close()
    stock_inventory = something.copy()
    return(stock_inventory)


#function 3
#function 3
def shopping(xy ,purhcase_order ): 
    something = {}
    counter = 0
    global products
    products = list(xy.keys())
    numbers = list(xy.values())
    users_product = "something"
    purhcase_order.write("Purhcased Product" +"\t" + "Quantity" +"\n")
    
    while users_product:  
        counter += 1
        users_product = input("product {}: " .format(counter))
        users_product = users_product.lower()

        if users_product in products:
            current_stock = int(xy[users_product])  
            
            if current_stock == 0:
                print(" NO stock")
                print()

            else:
                users_no = int(input("Quantity: " .format(users_product)))
                purhcase_order.write(users_product +"\t" +"\t" +"\t" +"\t" )
                
                if users_no > current_stock:
                    print(f"""Sorry product is limited\nYou're provided an extend of {current_stock}""")
                    something["Purchased " + users_product] = current_stock
                    something["Stock "+ users_product] = 0
                    xy[users_product] = 0  
                    purhcase_order.write(str(current_stock) + "\n")
                    
                elif users_no <= current_stock:
                    q = current_stock - users_no
                    something["Purchased " + users_product] = users_no
                    something["In Stock "+ users_product] = q
                    xy[users_product] = q  
                    purhcase_order.write(str(users_no) + "\n")
                print()
                
        elif users_product not in products and users_product != "":
            print("Sorry product not provided")
            
    purhcase_order.close()
    inventory = something.copy()
    return xy  

#main
def main():
 
    inventory = {}

    os.system('cls' if os.name =='nt' else 'clear')

#intro
    print("""
-------------------------------
Welcome to Bamazon's inventory
-------------------------------
""")
#company login
    print("LOGIN")
    n = input("Name: ")
    n = n.capitalize()
    id = input("Employee ID #: ")  
    
    i = input("")
    os.system('cls' if os.name =='nt' else 'clear')
    print("")
    print("""Hello, {}. \nPress enter start step #1: Suppling""" .format(n))

    i = input("")
    os.system('cls' if os.name =='nt' else 'clear')

#function 1
    products_base = open( "products_base.txt", "w" )#open file and closes in function
    a = products (inventory,  products_base) 
    print("""You have added the following products {} \n
Press enter to conform""".format(list_of_products))

    i = input("")
    os.system('cls' if os.name =='nt' else 'clear')
    time.sleep(1)

#function 2
    print("""
Step #2: Stocking""")
    print()
    print("Enter the quantity of each item")
    products_stock = open( "products_stock.txt", "w" ) #open file and closes in function
    b = stock(inventory , products_stock) 
    print()
    print()
    time.sleep(0.5)
    print("""You have successfully updated inventory\nCurrent invntory {} """.format(b))

    i = input("")
    os.system('cls' if os.name =='nt' else 'clear')
    time.sleep(2)

# online shopping - keeping aksing to order but no receipt
    z = True
    while z: 
        print("""
-------------------------------
Welcome to Bamazon Online store
-------------------------------
""")
        z = input("Would you like to start your order \nEnter 'yes' if so\n")  
        os.system('cls' if os.name =='nt' else 'clear')
        if z == "yes":
            purhcase_order = open( "purhcase_order.txt", "w" )
            c = shopping(inventory, purhcase_order)
            print( """You have purhcased the following products {}""".format(products))
            inventory = c
            i = input("")
            os.system('cls' if os.name =='nt' else 'clear')
            time.sleep(2)

        else: break

#start   
if __name__ == "__main__":
    main()