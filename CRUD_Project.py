from validation import money_v,email_v,date_v 
from file_handler import deleting,get_projects,save_project
from file_handler import find_project,generate_id,edit_project_from_the_file


#------CREATING NEW PROJECTS------------
def new_project():
    user_email=email_v("please enter you email address")
    title=input("Please enter the name of the campaign: ")
    details=input("Please enter the details of the campaign: ")
    target=money_v("Please enter the total target in USD: ")
    start_date=date_v("Please enter start date (YYYY-MM-DD): ")
    end_date=date_v("Please enter end date (YYYY-MM-DD): ")
    project_id = generate_id()
    new_project=f"{project_id}:{title}:{details}:{target}:{start_date}:{end_date}:{user_email} \n"
    
    try:
        fileobj =open("projects.txt", 'a')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.write(new_project)
        fileobj.close()
        return True
    

#------DELETITING BY ID AND EMAIL ADDRESS---------

def delete_project():
    email=email_v("First enter your email address: ")
    project_id = input("Please enter the id of the project you want to delete: ")
    found = find_project(project_id)
    rec=found[1].split(':')
    if found and email==rec[6].strip():
        removed=deleting(found[1])
        if removed:
            print(' Deleted Successfully ')
        else:
            print(" Something went wrong ")
    else:
        print(" Not Found,Please try again")

#--------EDITING WITH A MENU TO CHOOSE WHICH FIELD WILL BE EDITED-------

def edit_project():
    email=email_v("First enter your email address: ")
    project_id = input("Please enter the id of the project you want to update: ")
    found = find_project(project_id)
    rec=found[1].split(':')
    if found and email==rec[6].strip():
        edit = edit_project_from_the_file(found[1])
        if edit:
            print("Updated Successfully")
        else:
            print("Somthing went wrong")
    else:
        print(" Not Found,Please try again")
        
    #------LISTING ALL FIELDS WITHOUT THE EMAIL ADDRESS-------    
        
def list_all():
    pro = get_projects()
    for project in pro:
        fields = project.split(':')
        print(fields[0]," : ", fields[1]," : ", fields[2]," : ", fields[3]," : ", fields[4]," : ",fields[5])
        

