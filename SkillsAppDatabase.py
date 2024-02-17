# Import SQLite Module
import sqlite3

# Create a variable to store the file named.db
fileName = "app"

"""Create Database and connect then Setting up the cursor"""
db = sqlite3.connect(fileName + ".db")
cr = db.cursor()

def close_database_connection():
    """You must Save (Commit) Changes then close database connection"""
    db.commit()
    db.close()
    print("Connection to database is closed.")

# Users id
users_id = [1001, 1002, 1003, 1004, 1005]

# Define the methods
def show_skills():
    cr.execute(f"select * from skills where user_id = '{users_id[0]}'")
    result = cr.fetchall()
   
    print(f"You've {len(result)} skills.")   
    for row in result:
        print(f"{row[0]} skill with", end=" ")
        print(f"{row[1]}% progress.")

    close_database_connection()

def add_skill():
    sk = input("Write a new skill name: ").strip().capitalize()
    progress = input("Write the skill progress: ").strip()

    
    cr.execute(
        f"insert into skills(name, progress, user_id) values('{sk}', '{progress}', '{users_id[1]}')")
    close_database_connection()

def delete_skill():
    sk = input("Write a skill name to delete: ").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id = '{users_id[0]}' ")
    close_database_connection()

def update_skill_progress():
    sk = input("Write a skill name to update: ").strip().capitalize()
    progress = input("Write the skill progress to update: ").strip()

    cr.execute(f"update skills set progress = '{progress}' where name = '{sk}' and user_id = {users_id[0]}")
    close_database_connection()

# Command List
commands_List = {
    "s": show_skills,
    "a": add_skill,
    "d": delete_skill,
    "u": update_skill_progress,
    "q": exit
}

# Input Message
input_message = """
What do you want to do?
"s": Show all skills
"a": Add new skill
"d": Delete a skill
"u": Update a skill progress
"q": Quit
"""

while True:
    user_input = input(input_message).strip().lower()
    
    if user_input in commands_List:
        commands_List[user_input]()
        if user_input == "q":
            print("Exiting the application...")
            close_database_connection()
            break
    else:
        print("Please enter a valid command!")
