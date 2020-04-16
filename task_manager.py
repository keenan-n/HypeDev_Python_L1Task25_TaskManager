import datetime
from datetime import date  # import datetime module:

user_library = open('user.txt', 'r')  # open user.txt to view username's & password's:

u_name_list = ""  # username list.
p_word_list = ""  # password list.

# Loop through each line/user in user.txt:
for user in user_library:
    user = user.replace(' ', '')
    user = user.strip()
    user = user.split(',')

    # Add user index 0 to username:
    u_name_list += user[0]
    u_name_list += ','
    # Add user index 1 to password:
    p_word_list += user[1]
    p_word_list += ','

# Split to list: Remove last item ('')
u_name_list = u_name_list.split(',')
u_name_list = u_name_list[:-1]
# Split to list: Remove last item ('')
p_word_list = p_word_list.split(',')
p_word_list = p_word_list[:-1]

# Header/Title:
print(" ____________________________________")
print("|  WELCOME TO TASK MANAGER PROGRAM   |")
print(" ____________________________________")
print("")


# Function login:
def login():
    print("Login:")
    # Set Boolean false:
    validate = False
    # While False: Request username and password:
    while not validate:
        username = input("Username: ")  # Request username:
        password = input("Password: ")  # Request password:

        # if username and password are both in list and have the same index. Login user:
        if (username in u_name_list) and (password in p_word_list) \
                and u_name_list.index(username) == p_word_list.index(password):
            print("")
            print(f"Welcome, {username}.")
            # If user is admin:
            # Return user to admin menu:
            if username == 'admin':
                return admin(username)
            # If user is not admin:
            # Return user to user menu:
            else:
                return menu(username)

        # if username and password in are both in list but index doesn't match. Don't login user:
        elif (username in u_name_list) and (password in p_word_list) \
                and u_name_list.index(username) != p_word_list.index(password):
            # Keep Boolean as False to loop again:
            # Send error message:
            validate = False
            print(f"Username, {username} is correct.\n"
                  f"Password {len(password) * '*'} is incorrect.\n"
                  f"Please make sure you enter the correct password.")
            print("")

        # if username in list and password not in list. Don't login user:
        elif (username in u_name_list) and (password not in p_word_list):
            # Keep Boolean as False to loop again:
            # Send error message:
            validate = False
            print(f"Username, {username} is correct.\n"
                  f"Password {len(password) * '*'} is incorrect.\n"
                  f"Please make sure you enter the correct password.")
            print("")

        # if both username and password not in list. Don't login user:
        elif (username not in u_name_list) and (password not in p_word_list):
            # Keep Boolean as False to loop again:
            # Send error message:
            validate = False
            print(f"Username, {username} is incorrect.\n"
                  f"Password {len(password) * '*'} is incorrect.\n"
                  f"Please make sure you enter the correct password.")
            print("")


# Close user.txt file:
user_library.close()


# Function for admin:
def admin(username):
    # Admin menu options:
    print("Please select from the following options:")
    print("1 - Main Menu\n"
          "2 - Admin Menu")
    # Request admin choice:
    admin_choice = int(input(": "))
    # Depending on admin choice return admin to desired menu:
    if admin_choice == 1:
        # Return admin to user menu:
        return menu(username)

    else:
        print("")
        print("Admin Menu:")
        # Return admin to admin main menu:
        return admin_menu(username)


# Function for admin main menu:
# Request admin choice:
# Return it to admin exe with username and admin choice:
def admin_menu(username):
    print("")
    print("Please select from the following options:")
    print("1 - Register User\n"
          "2 - Add Task\n"
          "3 - View All Tasks\n"
          "4 - View My Tasks\n"
          "5 - Generate Reports\n"
          "6 - Display Statistics\n"
          "7 - Go Back\n"
          "8 - Exit")

    admin_choice_2 = int(input(": "))
    return admin_exe(username, admin_choice_2)


# Function for admin menu execution:
# Get username and admin choice:
# Return admin choice to menu exe or admin exe to perform function:
def admin_exe(username, admin_choice):
    if admin_choice == 1:
        return menu_exe(username, admin_choice)

    if admin_choice == 2:
        return menu_exe(username, admin_choice)

    if admin_choice == 3:
        return menu_exe(username, admin_choice)

    if admin_choice == 4:
        return menu_exe(username, admin_choice)

    if admin_choice == 5:
        # Return admin to generate reports function:
        return gen_reports(username)

    if admin_choice == 6:
        # Return admin to display statistics function:
        return display_stats(username)

    if admin_choice == 7:
        # Return admin back to admin menu function:
        return admin(username)

    else:
        # Return admin to exit code function:
        return exit_code(username)


# Function for menu:
def menu(username):
    print("")
    print("Please select from the following options:")
    print("1 - Register User\n"
          "2 - Add Task\n"
          "3 - View All Tasks\n"
          "4 - View My Tasks\n"
          "5 - Exit"
          )
    menu_choice = int(input(": "))
    # Send username and user choice to menu exe:
    return menu_exe(username, menu_choice)


# open user.txt:
user_library = open('user.txt', 'a')


# Function for menu execution:
# Get username and user choice:
# Take user choice and send user to desired function:
def menu_exe(username, menu_choice):
    if menu_choice == 1:
        print("")
        print("Register User:")
        print("")
        # Return user to register user function (admin can only do this):
        return reg_user(username)

    if menu_choice == 2:
        print("")
        print("Add Task:")
        print("")
        # Return admin to add task function:
        return add_task(username)

    if menu_choice == 3:
        print("")
        print("View All Tasks:")
        print("")
        # Return user to view task function:
        return view_tasks(username)

    if menu_choice == 4:
        print("")
        print("View My Tasks:")
        print("")
        # Return user to my task function:
        return my_tasks(username)

    if menu_choice == 5:
        print("")
        print(f"Logging Out...")
        print("")
        # Return user to exit code function:
        return exit_code(username)


# Function for registering a new user:
def reg_user(username):
    # Only admin can do this:
    if username == 'admin':
        # Request new user details:
        new_username = input("Enter Username: ")
        # While new username is in username list, request new_username again:
        while new_username in u_name_list:
            print("")
            print(f"The username, {new_username} is already taken .\n"
                  f"Please try another username.")
            new_username = input("Enter Username: ")

        new_password = input("Create Password: ")
        new_password_confirm = input("Confirm Password: ")
        # While new password is not equal to password confirm, request again:
        while new_password != new_password_confirm:
            print("Password's Don't Match.\n"
                  "Please try again:")
            new_password_confirm = input("Confirm Password: ")
        # If new password matches password confirm:
        # Append username and password:
        if new_password == new_password_confirm:
            u_name_list.append(new_username)
            p_word_list.append(new_password)
            # Write username and password to user.txt:
            user_library.write(f"\n{new_username}, {new_password}")
        # Return admin to admin menu:
        return admin_menu(username)

    else:
        # If user not admin:
        print("You Don't Have Access To This Feature.")
        # Return user to user menu:
        return menu(username)


# Function to add new task:
# Request task details from user:
def add_task(username):
    for_user = input("User assigned to: ")
    task_title = input("Task Title: ")
    task_desc = input("Task Description: ")
    task_assigned_date = date.today()
    task_due_year = int(input("Task Due Year: "))
    task_due_month = input("Task Due Month: ").capitalize()
    task_due_day = int(input("Task Due Day: "))
    due_date = f"{task_due_day} {task_due_month[0:3]} {task_due_year}"
    task_complete = 'No'

    # Request user to confirm if task details are correct:
    print("1 - Confirm\n"
          "2 - Edit")
    confirm = int(input("Confirm: "))
    # If users confirms: Write task details to tasks.txt:
    if confirm == 1:
        tasks_library_write = open('tasks.txt', 'a', encoding='utf-8-sig')
        tasks_library_write.write(f"\n{for_user}, {task_title}, {task_desc}, "
                                  f"{task_assigned_date.strftime('%d %b %Y')}, {due_date}, {task_complete}")  # format:
        tasks_library_write.close()
    # If user cancels: Return back to add task:
    else:
        print(add_task(username))

    # If user is admin return back to admin menu:
    if username == 'admin':
        return admin_menu(username)
    else:
        return menu(username)


# Function to view all tasks:
def view_tasks(username):
    tasks_library = open('tasks.txt', 'r')
    task_number = 0
    # Loop through each task/line in tasks.txt:
    for task in tasks_library:
        task = task.strip()
        task = task.split(', ')
        i = 0
        # For item in task list:
        for item in task:
            if i == 0:
                task_number += 1
                print(f"Task Number:        {task_number}")
                print(f"Assigned to:        {item}")
                i += 1
            elif i == 1:
                print(f"Task Title:         {item}")
                i += 1
            elif i == 2:
                print(f"Task Description:   {item}")
                i += 1
            elif i == 3:
                print(f"Time Assigned:      {item}")
                i += 1
            elif i == 4:
                print(f"Task Due Date:      {item}")
                i += 1
            elif i == 5:
                print(f"Task Complete:      {item}")
                print("________________________________")

    tasks_library.close()
    # Return user to user main menu:
    return menu(username)


# Function to view logged in users tasks:
def my_tasks(username):
    task_library_my = open('tasks.txt', 'r')
    has_task = False
    x = 0
    # Loop through task/line in tasks.txt:
    for task in task_library_my:
        task = task.strip()
        task = task.split(', ')
        x += 1
        # Loop through index in task
        for i in task:
            if i in username:
                print(f"Task Number:        {x}")
                print(f"Assigned to:        {task[0]}")
                print(f"Task Title:         {task[1]}")
                print(f"Task Description:   {task[2]}")
                print(f"Time Assigned:      {task[3]}")
                print(f"Task Due Date:      {task[4]}")
                print(f"Task Complete:      {task[5]}")
                print("________________________________")
                has_task = True

    if not has_task:
        # Let the user know they have no tasks:
        print(f"{username}, you have no tasks.")
    # Request if user wants to edit the task:
    print("")
    print("Please select from the following options:")
    print("1 - Edit Task\n"
          "2 - Go Back")
    edit_choice = int(input(": "))

    if edit_choice == 1:
        # If user wants to edit task return to edit task:
        task_library_my.close()
        return edit_task(username)
    else:
        task_library_my.close()
        # Return to user main menu:
        return menu(username)


# Function to edit task:
# Check if task number is not complete:
def edit_task(username):
    print("")
    print("Edit Task:")
    print("")
    task_edit_number = int(input("Edit Task Number:\n"
                                 ": "))

    task_to_edit = open('tasks.txt', 'r')

    task_to_edit_read = task_to_edit.readlines()
    check_task = (task_to_edit_read[task_edit_number - 1])  # Edit Task/Line No.
    check_task = check_task.strip()
    check_task = check_task.split(', ')

    # Check if task is complete or incomplete:
    # If not complete request what they would like to edit on the task:
    if check_task[5] == "No":
        print("")
        print("Please select from the following options:")
        print("1 - Mark Task Complete\n"
              "2 - Edit The Task\n"
              "3 - Cancel")

        edit_task_choice = int(input(": "))
        # If want to mark complete:
        if edit_task_choice == 1:
            # Return user to edit task complete:
            return edit_task_complete(username, task_edit_number)
        # If you want to change task details.
        elif edit_task_choice == 2:
            # Return user to edit the task:
            return edit_the_task(username, task_edit_number)
        # If user chooses to cancel:
        elif edit_task_choice == 3:
            # Return user to user menu:
            return menu(username)
    # Else print that the task is complete and return user to user menu:
    else:
        print("This task is already complete and cannot be edited.")
        return menu(username)


# Function to edit task complete:
# Mark task complete:
def edit_task_complete(username, task_edit_number):
    print("")
    print("Mark Task Complete:")
    task_to_edit = open('tasks.txt', 'r+')
    # Get task number:
    task_to_edit_read = task_to_edit.readlines()
    mark_complete = (task_to_edit_read[task_edit_number - 1])
    mark_complete = mark_complete.strip()
    mark_complete = mark_complete.split(', ')
    # Delete index 5:
    if mark_complete[5] == 'No':
        mark_complete.__delitem__(5)
        # Append "Yes" to list:
        task_complete = "Yes"
        mark_complete.append(task_complete)
        # New sentence:
        completed_task = f"{mark_complete[0]}, {mark_complete[1]}, {mark_complete[2]}, {mark_complete[3]}, " \
                         f"{mark_complete[4]}, {mark_complete[5]}\n"
        task_to_edit.close()
        # Request confirm change:
        confirm_change = int(input("1 - Confirm\n"
                                   "2 - Cancel\n"
                                   ": "))
        # If user confirms:
        # Write new sentence to task.txt:
        if confirm_change == 1:
            task_to_edit = open('tasks.txt', 'w')
            task_to_edit_read[task_edit_number - 1] = completed_task
            task_to_edit.writelines(task_to_edit_read)
            task_to_edit.close()
        # Else return user to edit task complete:
        else:
            return edit_task_complete(username, task_edit_number)
        print("")

        print("Task Change Complete.")
        # Return user to user menu:
        return menu(username)


# Function to edit task details:
def edit_the_task(username, task_edit_number):
    print("")
    print("Edit The Task:")
    print("")

    task_to_edit = open('tasks.txt', 'r+')
    # Get task number:
    task_to_edit_read = task_to_edit.readlines()
    make_change = (task_to_edit_read[task_edit_number - 1])
    make_change = make_change.strip()
    make_change = make_change.split(', ')
    # Request what user would like to change:
    change_to_what = int(input("1 - User Assigned:\n"
                               "2 - Due Date:\n"
                               ": "))
    # If user chooses to edit Username assigned:
    # Delete index 0:
    if change_to_what == 1:
        make_change.__delitem__(0)
        # Request new username:
        new_due_date = input("Enter New Assigned Username:\n"
                             ": ")
        # Insert new username:
        make_change.insert(0, new_due_date)
        # Create new sentence:
        completed_task = f"{make_change[0]}, {make_change[1]}, {make_change[2]}, {make_change[3]}, " \
                         f"{make_change[4]}, {make_change[5]}\n"
        task_to_edit.close()
        # Request if user wants to confirm change:
        confirm_change = int(input("1 - Confirm\n"
                                   "2 - Cancel\n"
                                   ": "))
        # If confirm:
        # Write to task.txt:
        if confirm_change == 1:
            task_to_edit = open('tasks.txt', 'w')
            task_to_edit_read[task_edit_number - 1] = completed_task
            task_to_edit.writelines(task_to_edit_read)
            task_to_edit.close()
            print("")
            print(f"Task change is complete.\n"
                  f"Task is now assigned to: {new_due_date}.")
            # Return user to user menu:
            return menu(username)
        # Else if user cancels:
        else:
            # Return user to edit the task:
            return edit_the_task(username, task_edit_number)
    # If user wants to change due date:
    # Delete index 4:
    elif change_to_what == 2:
        make_change.__delitem__(4)
        # Request user change:
        new_due_year = int(input("Enter Due Date Year: "))
        new_due_month = input("Enter Due Date Month: ").capitalize()
        new_due_day = int(input("Enter Due Date Day: "))
        # Create new date:
        new_due_date = f"{new_due_day} {new_due_month[0:3]} {new_due_year}"
        # Insert new date:
        make_change.insert(4, new_due_date)
        # Create new sentence:
        completed_task = f"{make_change[0]}, {make_change[1]}, {make_change[2]}, {make_change[3]}, " \
                         f"{make_change[4]}, {make_change[5]}\n"
        task_to_edit.close()
        # Request if user wants to confirm change:
        confirm_change = int(input("1 - Confirm\n"
                                   "2 - Cancel\n"
                                   ": "))
        # If user confirms:
        # Write edited task to tasks.txt
        if confirm_change == 1:
            task_to_edit = open('tasks.txt', 'w')
            task_to_edit_read[task_edit_number - 1] = completed_task
            task_to_edit.writelines(task_to_edit_read)
            task_to_edit.close()
            print("")
            print(f"Task change is complete.\n"
                  f"Task is new due date: {new_due_date}.")
            # Return user to user menu:
            return menu(username)


# Function to generate reports:
# Generate reports and write to txt files:
def gen_reports(username):
    # Task Overview:
    task_overview = open('task_overview.txt', 'w')

    # Number of tasks:
    task_count = open('tasks.txt', 'r')
    task_total = task_count.readlines()
    task_total = len(task_total)
    task_count.close()
    task_overview.write(f"Total Number of Tasks:                                 {task_total}\n")
    task_count.close()

    # Number of Completed / Incomplete Tasks:
    task_complete = open('tasks.txt', 'r')
    num_completed = 0
    num_incomplete = 0

    for task in task_complete:
        task = task.strip()
        task = task.split(', ')
        for item in task:
            # If task is complete:
            # Add 1 to completed task:
            if "Yes" in item:
                num_completed += 1
            # Add 1 to incomplete task:
            if "No" in item:
                num_incomplete += 1
    # Number of Completed Task:
    task_overview.write(f"Total Number of Completed Tasks:                       {num_completed}\n")

    # Number of Incomplete Tasks:
    task_overview.write(f"Total Number of Uncompleted Tasks:                     {num_incomplete}\n")
    task_complete.close()

    # Number of Tasks that are not complete and pass due Date:
    num_task_overdue = 0
    task_overdue = open('tasks.txt', 'r')
    for task in task_overdue:
        task = task.strip()
        task = task.split(', ')
        # Change format of date:
        date_today = date.today()
        date_due = datetime.datetime.strptime(task[4], '%d %b %Y')
        date_due = date_due.date()
        if date_due < date_today:
            if task[5] == "No":
                num_task_overdue += 1
    task_overview.write(f"Total Number of Uncompleted & Overdue Tasks:           {num_task_overdue}\n")

    incomplete_percent = (num_incomplete / task_total) * 100
    task_overview.write(f"Percentage of Tasks that are incomplete:               {incomplete_percent:.2f}%\n")

    overdue_percent = (num_task_overdue / task_total) * 100
    task_overview.write(f"Percentage of Tasks that are overdue:                  {overdue_percent:.2f}%\n")

    task_overview.close()

    # User Overview:................................................................................................
    user_overview = open('user_overview.txt', 'w')
    # Total number of users:
    user_overview.write(f"Total Number of Users:                                  {len(u_name_list)}\n")
    # Total number of tasks:
    task_count = open('tasks.txt', 'r')
    task_total = task_count.readlines()
    task_total = len(task_total)
    user_overview.write(f"Total Number of Tasks:                                  {task_total}\n"
                        f"\n"
                        f"\n")
    task_count.close()
    # For each user:
    for user_name in u_name_list:

        # Total number of tasks assigned to user:
        task_user = open('tasks.txt', 'r')
        total_task_user = 0
        for task in task_user:
            task = task.strip()
            task = task.split(', ')

            if user_name == task[0]:
                total_task_user += 1
        user_overview.write(f"Username:                                               {user_name}\n")
        user_overview.write(f"Total Number of Tasks Assigned to You:                  {total_task_user}\n")
        task_user.close()

        # Percentage of tasks assigned to user:
        task_user = open('tasks.txt', 'r')

        my_total_task = 0
        task_total = 0
        my_completed = 0
        my_incomplete = 0
        my_over_incomplete = 0

        for task in task_user:
            task = task.strip()
            task = task.split(', ')
            task_total += 1
            if user_name == task[0]:
                my_total_task += 1
                # If task is complete:
                if task[5] == "Yes":
                    # Add 1 to completed tasks:
                    my_completed += 1
                # If task is incomplete:
                if task[5] == "No":
                    # Add 1 to completed tasks:
                    my_incomplete += 1
                    # Change date format:
                    date_due = datetime.datetime.strptime(task[4], '%d %b %Y')
                    date_due = date_due.date()
                    date_today = date.today()
                    if date_due < date_today:
                        my_over_incomplete += 1

        percent_my_task = (my_total_task / task_total * 100)
        user_overview.write(f"Percentage of total tasks assigned to you:              {percent_my_task:.2f} %\n")

        percent_my_completed = (my_completed / task_total * 100)
        user_overview.write(f"Percentage of total completed tasks assigned to you:    {percent_my_completed:.2f} %\n")

        percent_my_incomplete = (my_incomplete / task_total * 100)
        user_overview.write(f"Percentage of total incomplete tasks assigned to you:   {percent_my_incomplete:.2f} %\n")

        percent_incomplete_overdue = (my_over_incomplete / task_total * 100)
        user_overview.write(f"Percentage of total incomplete tasks assigned to you:   "
                            f"{percent_incomplete_overdue:.2f} %\n"
                            f"\n")
        task_user.close()
    user_overview.close()
    display_stats(username)
    # Return admin to admin menu:
    return admin_menu(username)


# Function to display tasks:
def display_stats(username):
    # Try to display tasks:
    try:
        print("Display Statistics")

        task_overview_read = open('task_overview.txt', 'r')

        user_overview_read = open('user_overview.txt', 'r')

        print("__________________")
        print("Last Generated Report:")
        print("Task Overview:")
        print("")

        for report in task_overview_read:
            report = report.strip()
            print("__________________________________________________________________")
            print(report)
        print("__________________________________________________________________")

        print("")

        print("__________________")
        print("Last Generated Report:")
        print("User Overview:")
        print("")

        for report in user_overview_read:
            report = report.strip()
            print("__________________________________________________________________")
            print(report)
        print("__________________________________________________________________")
        task_overview_read.close()
        user_overview_read.close()
        # If Displayed:
        # Return admin to admin menu:
        return admin(username)

    # If overview files don't exist:
    # Catch error and display error message:
    except FileNotFoundError:
        print("")
        print("No Reports have been generated.\n"
              "Generating New Report...")
        # Return admin to generate reports:
        return gen_reports(username)


# Function to exit program:
def exit_code(username):
    # Request user input to confirm or cancel:
    print("1 - Confirm\n"
          "2 - Cancel")
    exit_confirm = int(input(": "))
    # If user choice is 1:
    if exit_confirm == 1:
        print(f"Goodbye {username}.")
        return exit(0)
    # Else user choice is 2:
    else:
        print(f"Welcome Back, {username}")
        # Return to user main menu:
        return menu(username)


# start print login function:
print(login())
