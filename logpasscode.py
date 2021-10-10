import os

class Login_password:

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
        print('register')

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


logpass = Login_password()
logpass.entrance()