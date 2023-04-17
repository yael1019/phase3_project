from tetris import main_menu

class CLI:
    
    def __init__(self,username=None,password=None):
        self.welcome()
        self.user_authentication()
        #self.username = username
        #self.password = password

    def welcome(self):
        print("/////ARE YOU READY TO PLAY SOME TETRIS?!/////")

    # def user_authentication(self):
    #     print("Select Option")
    #     print("1. Log-In")
    #     print("2. Create Account")
    #     user_input = input(">>>")
    #     if user_input == "1":
    #         self.log_in()
    #     elif user_input =="2":
    #         self.create_account()
    #         pass
    #     else:
    #         print("Select valid option")
    #         self.user_authentication()

    # def log_in(self):
    #     print("Username")
    #     user_name = input(">>> ")
    #     print("Password")
    #     password = input(">>> ")
    #     pass

    # def create_account(self):
    #     print("Enter Username")
    #     user_name = input(">>> ")
    #     self.username = user_name
    #     print("Enter Password")
    #     password = input(">>>")
    #     self.password = password

    def start(self):
        self.show_menu()
        user_input = ""
        while user_input != "3":
            user_input = input(">>> ")
            if user_input =="1":
                pass
                main_menu()
            elif user_input =="2":
                pass
            elif user_input =="3":
                print("Goodbye thanks for playing!")
                pass
            else:
                print("Invalid input please try again")
                    
        
    def show_menu(self):
        print("Please choose an option:")
        print("1. Play Tetris")
        print("2. Scores")
        print("3. Exit")

cli = CLI()
