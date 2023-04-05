from CRUD_Project import delete_project,edit_project,new_project,list_all

def projectmenu():
    while True:
        print ("PROJECTS MENU ")
        choice = input(" 1-List all projects \n 2-New project \n 3-Delete project \n 4-Edit a project \n 5-Logout \n -> ")
        if choice=='1':
            list_all()
            print('-------------------------------------')
        elif choice=='2':
            new_project()
            print('-------------------------------------')
        elif choice=='3':
            delete_project()
            print('-------------------------------------')
        elif choice=='4':
            edit_project()
            print('-------------------------------------')
        elif choice=='5':
            print('-------------------------------------')
            print('BYE, HOPE TO SEE YOU AGAIN SOON \U0001F44B')	
            exit()
            
        

