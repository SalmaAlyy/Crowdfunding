
from create import createUser
from login import signin


  
def mainmenu():
    while True:
        print ("WELCOME TO OUR CROWDFUNDING PLATFORM \U0001F600")
        choice = input(" 1-Login \n 2-Signup \n 3-Exit \n -> ")
        if choice=='1':
            signin()
        elif choice=='2':
            createUser()
            
            print ("THANK YOU FOR JOINING US \U00002764")
            print ("-----------------------")
        elif choice=='3':
            print('BYE \U0001F44B')
            exit()
        else:
            print("Invalid choice")
            return
        
            

mainmenu()
