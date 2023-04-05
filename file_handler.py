import time 
from validation import date_v 
from validation import money_v,email_v
def listing():
    try:
        fileobj =open("projects.txt", 'r')
    except Exception as e:
        print(e)
        return False
    else:
        projects = fileobj.readlines()
        return projects

def save_project(project):
    try:
        fileobj =open("projects.txt", 'a')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.write(project)
        fileobj.close()
        return True

def get_projects():
    try:
        fileobj =open("projects.txt", 'r')
    except Exception as e:
        print(e)
        return False
    else:
        project = fileobj.readlines()
        return project


def deleting(project):
    projects=listing()
    projects.remove(project)  
    removed = save_to_file(projects)
    return removed


def find_project(title):
    pro = listing()
    for project in pro:
        print(project)
        project_title = project.strip('\n').split(":")
        if project_title[0]==str(title):
            return True , project
    else:
        return False
    
    
def save_to_file(pro_list):
    try:
        fileobj =open("projects.txt", 'w')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.writelines(pro_list)
        fileobj.close()
        return True
    
    

        
        
def generate_id():
    return round(time.time())



def edit_project_from_the_file(project):
    edit_project = project
    print(project)
    choice = input(
        " 1-Edit title \n 2-Edit details \n 3-Edit target \n 4-Edit start time \n 5-Edit end time \n 6-Exit \n ->")

    if choice == '1':
        new_value = input("Enter the new title: ")
        project_parts = edit_project.split(':')
        project_parts[1] = new_value
        edit_project = ':'.join(project_parts)
        print("The project's title has been updated to:", new_value)

    elif choice == '2':
        new_value = input("Enter the new details: ")
        project_parts = edit_project.split(':')
        project_parts[2] = new_value
        edit_project = ':'.join(project_parts)
        print("The project's details have been updated to:", new_value)

    elif choice == '3':
        new_value = money_v("Enter the new total pages: ")
        project_parts = edit_project.split(':')
        project_parts[3] = str(new_value)
        edit_project = ':'.join(project_parts)
        print("The project's target have been updated to:", new_value)

    elif choice == '4':
        new_value = date_v("Enter the new start time: ")
        project_parts = edit_project.split(':')
        project_parts[4] = new_value
        edit_project = ':'.join(project_parts)
        print("The project's start time has been updated to:", new_value)

    elif choice == '5':
        new_value = date_v("Enter the new end time: ")
        project_parts = edit_project.split(':')
        project_parts[5] = new_value
        edit_project = ':'.join(project_parts)
        print("The project's end time has been updated to:", new_value)

    elif choice == '6':
        print("--------------------")
        exit()

    else:
        print("Invalid choice")
        return

    projects = listing()
    projects.append(edit_project)
    edit_t = save_to_file(projects)
    deleting(project)
    return edit_t