

#imports
import random
import os
import time
import copy



class Person:
    __all_people = { }
    def __init__(self, name, address, possessions= [] ) :
        self.name = name
        self.address = address
        self._possessions  =  possessions
        self.__all_people[(name, address)] = self

    def __str__(self):
        return f'{self.name} from {self.address} '
   
    def view_possessions(self):
        copy_of_possessions =  self._possessions
        return copy_of_possessions
   
    def get_person(self,name, address):
        return self.__all_people[(name, address)]
   
    def create_parcel(self,recipient_name, recipient_address, item): 
        recipient_name = recipient_name
        recipient_address = recipient_address
       
        if item in self._possessions:
            self._possessions.remove(item)
            parcel = Parcel(self.name, self.address, recipient_name, recipient_address, item)      
            return parcel
         
        else:
            return f'error {item} not in possessions'
   
    def receive_parcel(self, parcel):
        if isinstance(parcel, Parcel):
            item = parcel.open_parcel()
            x = list(self._possessions)
            x.append(item)
        return x


class Parcel():
   
    def __init__(self,sender_name, sender_address,recipentname,recipentaddress, item , tracking_id=None):  
        self._sender_name= sender_name
        self._sender_address = sender_address
        self._recipentname = recipentname
        self._recipentaddress = recipentaddress
        self._item = item
        self._tracking_id = tracking_id
       
    def __str__(self):
        return f'Parcel with id {self._tracking_id} for {self._recipentname} in {self._recipentaddress}, from {self._sender_name} in {self._sender_address}'
   
    def get_sender_name(self):
        return  f'{self._sender_name}'
   
    def get_sender_address(self):
        return  f'{self._sender_address}'
   
    def get_recipentname(self):
        return  f'{self._recipentname}'
   
    def get_recipentaddress(self):
        return  f'{self._recipentaddress}'
   
    def set_tracking_id(self):
        if self._tracking_id == None:
           
            self._tracking_id =  random.randint(0,4999)
            return  f'{self._tracking_id}'
        else:
            return  f'{self._tracking_id}'
   
    def open_parcel(self):
        final = self._item  
        self._item = None
        return final



class Truck:
    def __init__(self, canada_post, city, manifest):
        self.canada_post = canada_post
        self.city = city
        self.manifest = manifest


    def ship_parcel(self, parcel):
        tracking_id = parcel.set_tracking_id()
        a= self.canada_post.get_location(self.city)
        w = PostOffice(a,self.canada_post,self.manifest)
        w.receive_parcel(parcel)  


class Manifest:
    # num = -1
    def __init__(self, sender_names = [], sender_addresses = [],recipient_names = [],recipient_addresses = [],status = [] ,size = 0 ):
        self._size = 0
        self._sender_names = []
        self._sender_addresses = []
        self._recipient_names = []
        self._recipient_addresses = []
        self._status = {}
        self.tracking_id = None
       
    def __str__(self):
        return f"\nFROM:\n{''.join(self._sender_names)}\n{''.join(self._sender_addresses)}\nTO:\n{''.join(self._recipient_names)}\n{''.join(self._recipient_addresses)}"
   
    def new_parcel(self, parcel):
        sender_name = parcel.get_sender_name()
        sender_address = parcel.get_sender_address()
        recipient_name = parcel.get_recipentname()
        recipient_address = parcel.get_recipentaddress()
        
    
        
        self._sender_names.append(sender_name )
        self._sender_addresses.append( sender_address )
        self._recipient_names.append(recipient_name)
        self._recipient_addresses.append(recipient_address)
        self.tracking_id = parcel.set_tracking_id()
        self._status[self.tracking_id] = []
        self._status[self.tracking_id].append("Tracking ID Created")
        self._size +=  1
   


        return self.tracking_id
       
    def track_parcel(self,tracking_id):
        return self._status[tracking_id]
   
    def update_status(self, tracking_id, new_status):
        self._size +=  1
        self._status[tracking_id].append(new_status)
        return self._status[tracking_id]
       
   

       
class CanadaPost:
    def __init__(self, cities, manifest):
        self.__post_offices = {}
        self.__manifest = manifest


        for city in cities:
            post_office = PostOffice(self, city, manifest)
            self.__post_offices[city] = post_office


    def __str__(self):
        city_list = ', '.join(self.__post_offices.keys())
        return f"CanadaPost is pleased to have stations available in the following cities:\n{city_list}"


    def track_parcel(self, tracking_id):
        return self.__manifest.track_parcel(tracking_id)


    def get_location(self, city):
        return self.__post_offices.get(city)




class PostOffice:
    def __init__(self, city, canada_post, manifest ):
        self.__city = city
        self.__canada_post = canada_post
        self.__manifest = manifest
        self.__truck = Truck(self.__canada_post, self.__city,self.__manifest )
       
    def __str__(self):
        return f"CanadaPost office located in {self.__city}"
   
    def ship_parcel(self, parcel):  
        tracking_id = self.__manifest.new_parcel(parcel)
        parcel.set_tracking_id()
        v = self.__canada_post.get_location(self.__city)
        # truck = self.__truck(v)
        self.__truck.ship_parcel(parcel)
        self.__manifest.update_status(tracking_id, "In Transit")      
        return tracking_id


    def receive_parcel(self, parcel):
        tracking_id = parcel.set_tracking_id()
        self.__manifest.update_status(tracking_id, "Awaiting Pickup")  
        self.pickup(parcel)
        self.__manifest.update_status(tracking_id, "Delivered")
       


    def pickup(self, parcel):
        recipient = parcel.get_recipentname()
        address  = parcel.get_recipentaddress()
        person = Person(recipient,address)
        person.receive_parcel(parcel)                    
        self.__manifest.update_status(parcel.set_tracking_id(), "Delivered and recieved")
       
       



def main():
    print(input(""))
    os.system('cls' if os.name =='nt' else 'clear')
    print()

    #Variables
    names = ["Jane" , "Jake", "Ethan" , "Freya", "Dylan" , "Emily"]
    cities  = ["Edmonton AB", "Toronto ON", "Calgary AB", "Vancouver BC"  ]
    possessions = ["Taxidermied Duck", "Lava Lamp" , "Shirt" ,  "Mug" , "Wig", "Notebook" , "Clock" ,"Magnifying glass" , "Desk" , "Rug" , "Picture Frame", "Camera"]
    people = {
       
        names[0] : [ names[0] ,cities[0], possessions[0] , possessions[2] , possessions[8]],
        names[1] : [ names[1] ,cities[1], possessions[1] , possessions[2] ,possessions[6]],
        names[2] : [ names[2] ,cities[2], possessions[2] , possessions[2], possessions[7]],
        names[3] : [ names[3] ,cities[3], possessions[3]  ,possessions[2] , possessions[9]],
        names[4] : [ names[4] ,cities[0], possessions[4] , possessions[2], possessions[10] ],
        names[5] : [ names[5] ,cities[3], possessions[5] , possessions[2], possessions[11]],
    }
    sender_name = None
    recipient_name = None
    result = False
    all_manifests = [] 
    new_list= None

    #while loop
    while result == False:
        menus_chioce = None
        menu2_choice = None

        print()
        print()

        #MENU 1  
        print("\nMenu 1:")
        print("1) Sign in")
        print("2) Print Manifest")
        print("3) Exit")
        print()
        menus_chioce = input("Please enter the corresponding number: ")
        os.system('cls' if os.name =='nt' else 'clear')
       
       
        if int(menus_chioce) == 1:
            print("Please select the corresponding number from the following \n")
        #setting up a sender
            num = 0
            for i in list(people.keys()):
                num = num+1
                print(f'{num}) {i} - {people[i][1]}')   
         
            person= int(input("\nwho's signing in?: "))
            person  = person - 1
           
            #sender
            sender_name = people.get(names[person])[0]
            sender_location = people.get(names[person])[1]
            sender__possessions = sorted(people.get(names[person])[2:])
            os.system('cls' if os.name =='nt' else 'clear')

            #MENU 2
            print("\nMenu 2:")
            print("1) View Your Possessions")
            print("2) Send Parcel")
            print("3) Back")
            menu2_choice= int(input("\nPlease enter the corresponding number: "))

            os.system('cls' if os.name =='nt' else 'clear')

            if menu2_choice == 1:
                print("\n-Your Inventory-\n")
                #the sender view their possessions
                x = sorted(people.get(names[person])[2:])
                print('\n'.join(x))
                print(input(""))
                os.system('cls' if os.name =='nt' else 'clear')
                continue


            elif menu2_choice == 2:   #SEND PARCEL
            #Setting up the item
                w=0
                print("\nFrom Your Inventory\n")
                for x in sender__possessions:
                    w+=1
                    print (f'{w}) {x} ')
               
                item_1 = int(input("Please enter the corresponding number of the item you would like to send: "))
                item_1  = sender__possessions[item_1 -1]
                
                os.system('cls' if os.name =='nt' else 'clear')
                
            #settin up the recipent
                #copy of names without the sender to print when choosing a recipent
                copy_of_dict = copy.deepcopy(people)  
                add_back_in = people[sender_name]


                del copy_of_dict [sender_name]
                num = 0
                print("\nPlease enter the corresponding number of the recipent\n")
                for i in list(copy_of_dict.keys()):
                    num =num+1
                    print(f'{num}) {i} - {copy_of_dict[i][1]}')
                person2 = int(input("\nWho's the recipent?: "))
               
                if person2 > person:
                    person2  = person2
                elif person2 < person or person2 == person:
                    person2  = person2 +1
       

                people[sender_name] = add_back_in


                #recipient
                recipient_name = copy_of_dict.get(names[person2])[0]     
                recipient_location = copy_of_dict.get(names[person2])[1]
               
                os.system('cls' if os.name =='nt' else 'clear')
               
               
                print("Initiating Parcel Shipment...")
                time.sleep(1.5)

                #Classes
                person = Person(sender_name, sender_location, sender__possessions)
                parcel = person.create_parcel(recipient_name, recipient_location, item_1)
                manifest = Manifest(parcel)
                canadapost = CanadaPost(cities,manifest)
                location = canadapost.get_location(sender_location)  
                postoffice = PostOffice(location,canadapost,manifest)
                tracking_id = postoffice.ship_parcel(parcel)
               
           
                print("Parcel Shipment Confirmation")
                # print(manifest)
                print(f'{manifest} \nTracking ID: UA-{tracking_id} ')
               
                print(input("\nPress enter to confirm "))
                os.system('cls' if os.name =='nt' else 'clear')

                all_manifests.append(manifest)     #to be able to print hitory of manifest
                continue
           
           
            elif menu2_choice == 3:
                os.system('cls' if os.name =='nt' else 'clear')
                continue




        elif int(menus_chioce) == 2: #manifest menu
           
            if sender_name == None or recipient_name == None:
                print("No Parcels delivered")
            else:
                print("Manifest History")
                num=0
                for i in all_manifests:
                    num=+1
                    print(f"\nParcel {num} \n {i} \nParcels Status: Delivered")
                    postoffice.receive_parcel(parcel)
                   
   
          
             #updating sender's and recipent's items
            people[recipient_name] += [item_1]
            people[sender_name].remove(item_1)
            print(f'Your Inventory has been updated to {people[sender_name][2:]} ')
            print(input(""))
            os.system('cls' if os.name =='nt' else 'clear')
            continue


        elif int(menus_chioce) == 3:
            print("Thank you for using Parcel Delivery System \n\nExiting System....")
            time.sleep(1)
            os.system('cls' if os.name =='nt' else 'clear')
            break


        else:
            print("Error")
   
        result = True
   



os.system('cls' if os.name =='nt' else 'clear')
Welcome_message = "\n----------------------------------\nWelcome to Parcel Delivery System \nPress enter to continue\n----------------------------------\n"    #welcome message is out of function so that it doesnt reprint when looping
print(Welcome_message)
if __name__ == "__main__":
    main()

