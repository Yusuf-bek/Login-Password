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

    def entrance(self):
        self.entrance_text()
        option = input(": ").strip()

        if option == '':
            option = ' '

        list_option = '1234'

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
                "Invalid input. Username only contains letters or maximum length should be 30 ").lower().strip()

        self.login = input("Enter your login: ").lower().strip()
        while len(self.login) < 6 or len(self.login) > 30 or self.is_login_exists(self.login):
            self.clear_everything()
            self.login = input("Invalid input. 6 <= login <= 30: ").lower().strip()

        self.password = input("Enter your password: ").lower().strip()
        while len(self.password) < 8 or len(self.password) > 30:
            self.clear_everything()
            self.password = input("Invalid password. It should be at least 8, maximum 30: ").lower().strip()

        self.age = input("Enter your age: ").strip()
        while not self.age.isnumeric() or int(self.age) > 200:
            self.age = input("Invalid age. Enter it again: ").strip()

        self.write_to_database(self.username, self.login, self.password, self.age)



    def log_in(self):
        print('log in')

    def log_out(self):
        print('log out')

    def delete_account(self):
        print('delete account')

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


logpass = Login_password()
logpass.entrance()
