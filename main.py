from listofdata import get_line
from totalsalaries import get_salaries
from getage import get_age
from emails_check import emailscheck
from deleterow import delete_row
from edite import edit_values

# the welcome massage
print('welcome here :) ')
# open the file to append
ff = open("/home/gamal/Downloads/python projects/lab_1_python/data.txt" , 'a')

# the start
user_input =  input("Enter '1' to login or any other character to exit ")
if user_input == '1':
    #Enter the name
    print(' please enter your email' )
    user_email = input('Enter your email : ')
    print(' please enter your password' )
    user_password = input('Enter your password : ')
    thedataline = get_line(user_email,user_password)
    
    
    print('Hello '+ thedataline[1])
                # gettin credentials
    if thedataline[8] == 'admin':
        print('you can add admin or employee and remove or edit employee')
        admin_cred = input(" '1' to add admin or employee '2' to remove or '3' edit employee")
        if admin_cred == '1':
            add_id = input('enter your data id : ')
            add_name = input('enter your data name: ')
            add_salary = input('enter your data salary: ')
            add_age = input('enter your data age: ')
            add_position = input('enter your data position: ')
            add_technology = input('enter your data technology: ')
            add_email = input('enter your data email: ')
            while True:
                add_email = input('enter your data email: ')
                if emailscheck(add_email) == 0:
                    print("it is duplicated")
                else:
                    break
            add_password = input('enter your data password : ')
            add_management_type = input('enter your data management_type: ')
            ff.write(add_id+','+add_name+','+add_salary+','+add_age+','+add_position+','+add_technology+','+add_email+','+add_password+','+add_management_type+'\n')
        if admin_cred == '2': 
            enter_name = input('Enter the name : ') 
            delete_row(enter_name)
        if admin_cred == '3':
            userx = input("the email: ")
            oldvalue = input(' enter oldvalue: ')
            newvalue = input(' enter newvalue: ')
            edit_values(userx,oldvalue ,newvalue)
            print("Check your data to see the changes")
              
    else:
        print('you have employee credentials')
        employee_input = input("enter '1' to calculate your salary '2' to allsalaries '3' get age with themail  ")
        # get the employee salary
        if employee_input == '1':
            print(thedataline[2])
        # get the total ssalaries
        if employee_input == '2':
            print(get_salaries())
         # get other employee's age
        if employee_input == '3':
            employee_name = input('Enter the name : ')
            print(get_age(employee_name))

else:
    print('Goodby sir')