ID= input("Your ID : ").strip()
Name= input("Your Name :").upper().strip()
dob= input("Your date of birth in this way : DD-MM-YYY :").strip()
Address= input("Your Address :").lower().strip() 
ID= '0' + ID
dob= dob.replace("-" , "/")
print("Your Information:")
print(f"Your Profile-ID : {ID} , Name : {Name} , Dob : {dob} , Address: {Address} ")










