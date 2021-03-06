import os
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    database='user__data',
    user='Abdulaziz',
    password='123123123',
)
mycursor = mydb.cursor()


class Login_password:

    def __init__(self):
        self.username = None
        self.login = None
        self.password = None
        self.age = None
        self.is_loggedin = False


    def entrance(self):
        self.entrance_text()
        option = input(": ").strip()

        if option == '':
            option = ' '

        list_option = ['1', '2', '3', '4']

        while option not in list_option:
            self.clear_everything()
            self.entrance_text()
            option = input("Invalid input. Choose only 1/2/3/4: ").strip()

            if option == '':
                option = ' '

        if option == '1':
            self.register()
        elif option == '2':
            self.log_in()
        elif option == '3':
            self.log_out()
        elif option == '4':
            self.delete_account()



    def register(self):
        self.clear_everything()
        self.registration_text()

        self.username = input("Enter your username: ").lower().strip()
        while not self.username.isalpha() or len(self.username) > 30:
            self.clear_everything()
            self.registration_text()
            self.username = input(
                "Invalid input. Username only contains letters or maximum length should be 30: ").lower().strip()

        self.login = input("Enter your login: ").lower().strip()
        while len(self.login) < 6 or len(self.login) > 30 or self.is_login_exists(self.login):
            self.clear_everything()
            self.login = input("Invalid login. 6 <= login <= 30: ").lower().strip()

        self.password = input("Enter your password: ").lower().strip()
        while len(self.password) < 8 or len(self.password) > 30:
            self.clear_everything()
            self.password = input("Invalid password. It should be at least 8, maximum 30: ").lower().strip()

        self.age = input("Enter your age: ").strip()
        while not self.age.isnumeric() or int(self.age) > 200:
            self.age = input("Invalid age. Enter it again: ").strip()

        self.write_to_database(self.username, self.login, self.password, self.age)
        self.is_loggedin = True
        print("\n")
        print("<<< You are in system >>>")
        self.wish_to_logout()



    def log_in(self):
        self.clear_everything()
        print("<<< Log in >>>")

        self.login = input("Enter your login: ").lower().strip()
        while len(self.login) < 6 or len(self.login) > 30:
            self.clear_everything()
            self.login = input("Invalid login. 6 <= login <= 30: ").lower().strip()


        self.password = input("Enter your password: ").lower().strip()
        while len(self.password) < 8 or len(self.password) > 30:
            self.clear_everything()
            self.password = input("Invalid password. It should be at least 8, maximum 30: ").lower().strip()

        if self.is_user_exists(self.login, self.password):
            print("<<< Welcome to system >>>")
        else:
            print("<<< You have entered wrong login or password >>>")


            yes_no = input("<<< Do you want to register or login? [r/l]>>>  ").lower().strip()

            while yes_no not in ['r', 'l']:
                self.clear_everything()
                print("Invalid input. Enter only r or l")
                yes_no = input("<<< Do you want to register or login? [r/l]>>>  ").lower().strip()

            if yes_no == 'r':
                self.register()
            elif yes_no == 'l':
                self.log_in()

        self.is_loggedin = True
        self.clear_everything()
        print("<<< You are in system >>>")
        self.wish_to_logout()



    def log_out(self):

        if not self.is_loggedin:
            self.clear_everything()
            print("<<< First you have to login or register >>>")
            self.entrance()
        else:
            self.clear_everything()
            print("<<< You logged out >>>")



    def delete_account(self):
        self.clear_everything()
        print("<<< Delete account >>>")

        self.login = input("Enter your login: ").lower().strip()
        while len(self.login) < 6 or len(self.login) > 30:
            self.clear_everything()
            self.login = input("Invalid login. 6 <= login <= 30: ").lower().strip()

        self.password = input("Enter your password: ").lower().strip()
        while len(self.password) < 8 or len(self.password) > 30:
            self.clear_everything()
            self.password = input("Invalid password. It should be at least 8, maximum 30: ").lower().strip()

        self.delete_user(self.login, self.password)




    def entrance_text(self):
        print("""
        <<< Welcome >>>

        1) Register
        2) Log in
        3) Log out
        4) Delete account

        """)

    @staticmethod
    def clear_everything():
        os.system('clear')

    @staticmethod
    def registration_text():
        print("<<< Registration page >>>")



    def is_login_exists(self,input_login):
        mycursor.execute(f"select * from users  where login='{input_login}'")
        data_users = mycursor.fetchall()

        return data_users

    def write_to_database(self, username, login, password, age):
        mycursor.execute(f"insert into users (username, login, password, age) values ('{username}', '{login}', '{password}', '{age}')")
        mydb.commit()

    def is_user_exists(self, login, password):
        mycursor.execute(f"select password from users where login='{login}'")
        data_users = mycursor.fetchall()

        if not data_users:
            return False

        if password == data_users[0][0]:
            return True
        return False

    def wish_to_logout(self):
        logout_option = input("<<< Do you wish to log out? [y/n] >>> ").lower().strip()

        while logout_option not in ['y', 'n']:
            self.clear_everything()
            print("<<< Invalid input. You can only write y or n >>>")
            logout_option = input("<<< Do you wish to log out? [y/n] >>> ").lower().strip()

        if logout_option == 'y':
            self.log_out()
        elif logout_option == 'n':
            self.clear_everything()
            print("<<< You are in system >>>")

    def delete_user(self, login, password):
        if self.is_user_exists(login, password):
            option = input("<<< Do you wish to delete your account [y/n] >>> ").lower().strip()

            while option not in ['y', 'n']:
                print("<<< Invalid input. Choose only y or n >>>")
                option = input("<<< Do you wish to delete your account [y/n] >>> ").lower().strip()

            if option == 'y':
                mycursor.execute(f"delete from users where login='{login}'")

                mydb.commit()
                print('<<< Your account is deleted >>>')
            else:
                self.entrance()

        else:
            self.clear_everything()
            print("<<< Login or password is invalid >>>")

            option2 = input("Do you want to delete your account or go back to main menu [d/m]: ").lower().strip()

            while option2 not in ['d', 'm']:
                print("<<< You entered invalid option. Choose only d or m >>>")
                option2 = input("Do you want to delete your account or go back to main menu [d/m]: ").lower().strip()

            if option2 == 'd':
                self.delete_account()
            elif option2 == 'm':
                self.entrance()



logpass = Login_password()
logpass.entrance()
