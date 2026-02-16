
#intro statment
import time  
import database

print ()
print ("""Welcome to the Phone Book""")

print ()
time.sleep(1)

print ("Please enter your name")

user = input ()
user = user.capitalize()

print ("Hello," , user) 

time.sleep(0.8)

print ("Welcome to the Company's Contact list")

time.sleep(1.5)
print () 

#questions
print("Who would you like to contact? ")

time.sleep(1.5)
print ()

print (database.names)

time.sleep(0.5)

name = input(("Please select the letter: "))

time.sleep(1)
print ()

print ("What information would you prefer?")

time.sleep(1.5)

print (database.m1)

time.sleep(0.5)

ans = input(("Please select the letter: "))

time.sleep(1.8)


#name1
if name in database.name1 or name in database.choice_a and ans in database.choice_d or ans in database.choice_allinfo:
    print (database.name1_contact_info)

elif  name in  database.name1 or name in database.choice_a and ans in database.phone_number or ans in database.choice_a:
    print (database.name1_phone) 

elif  name in  database.name1  or name in database.choice_a and ans in database.address or ans in database.choice_b:
    print (database.name1_address)

elif  name in  database.name1  or name in database.choice_a and ans in database.email or ans in database.choice_c:
    print (database.name1_email)



#name2
elif  name in  database.name2 or name in database.choice_b or ans in database.choice_d or ans in  database.choice_allinfo:
    print (database.name2_contact_info)

elif  name in  database.name2 or name in database.choice_b   and ans in database.phone_number or ans in database.choice_a:
    print (database.name2_phone) 

elif  name in  database.name2 or name in database.choice_b and ans in database.address or ans in database.choice_b:
    print (database.name2_address)

elif  name in  database.name2  or name in database.choice_b  and ans in database.email or ans in database.choice_c:
    print (database.name2_email)


#name3 
elif  name in  database.name3 or name in database.choice_c or ans in  database.choice_d or ans in  database.choice_allinfo:
    print (database.name3_contact_info)

elif  name in  database.name3 or name in database.choice_c   and ans in database.phone_number or ans in database.choice_a:
    print (database.name3_phone) 

elif  name in  database.name2 or name in database.choice_c  and ans in database.address or ans in database.choice_b:
    print (database.name3_address)

elif  name in  database.name2  or name in database.choice_c  and ans in database.email or ans in database.choice_c:
    print (database.name3_email)


#name4 
elif  name in  database.name4 or name in database.choice_d  or ans in  database.choice_d or ans in  database.choice_allinfo:
    print (database.name4_contact_info)

elif  name in  database.name4 or name in database.choice_d   and ans in database.phone_number or ans in database.choice_a:
    print (database.name4_phone) 

elif  name in  database.name4 or name in database.choice_d  and ans in database.address or ans in database.choice_b:
    print (database.name4_address)

elif  name in  database.name4  or name in database.choice_d  and ans in database.email or ans in database.choice_c:
    print (database.name4_email)


#name5
elif  name in  database.name5 or name in database.choice_e or ans in  database.choice_d or ans in  database.choice_allinfo:
    print (database.name5_contact_info)

elif  name in  database.name5 or name in database.choice_e  and ans in database.phone_number or ans in database.choice_a:
    print (database.name5_phone) 

elif  name in  database.name5 or name in database.choice_e  and ans in database.address or ans in database.choice_b:
    print (database.name5_address)

elif  name in  database.name5 or name in database.choice_e and ans in database.email or ans in database.choice_c:
    print (database.name5_email)


else: 
    print()
    print ("""unfortunately, this person is not listed
Please contact us for more information""")

print()

#outro
print ("Thank you for using our service!")


