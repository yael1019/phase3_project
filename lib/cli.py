from tetris import main_menu
from lib import CONN, CURSOR
# import ipdb
from ascii import welcome_purple, welcome_blue
# from ascii_magic import AsciiArt
import random

# my_art = AsciiArt.from_image('tetris7.png')
welcome = random.choice([welcome_purple, welcome_blue])
# print(welcome)

class CLI:

    
    def __init__(self,username=None,password=None, id = None):
        self.welcome()
        self.user_authentication()
        self.username = username
        self.password = password
        self.id = id
    
    def __repr__(self):
        return f'<CLI id={self.id} username={self.username} password={self.password}>'

    @classmethod
    def create(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT
            )
        """
        CURSOR.execute(sql)

    def create_user(self):
        sql = """
            INSERT INTO users (username, password)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, [self.username, self.password])
        CONN.commit()
        self.id = CURSOR.execute('SELECT * FROM users ORDER BY id DESC').fetchone()[0]


    def welcome(self):
        # print("/////ARE YOU READY TO PLAY SOME TETRIS?!/////")
        print(welcome)
        # my_art.to_terminal()

    def user_authentication(self):
        print("Select Option")
        print("1. Log-In")
        print("2. Create Account")
        user_input = input(">>>")
        if user_input == "1":
            self.log_in()
        elif user_input =="2":
            self.create_account()
        else:
            print("Select valid option")
            self.user_authentication()

    def log_in(self):
        print("Username")
        user_name = input(">>> ")
        print("Password")
        password = input(">>> ")
        sql = """
            SELECT * FROM users
        """
        all = CURSOR.execute(sql).fetchall()
        for i in all:
            if i[1] == user_name and i[2] == password:
                self.username = user_name
                self.password = password
                sql = """
                    SELECT id FROM users WHERE username = (?)
                """
                self.id = CURSOR.execute(sql,(user_name,)).fetchone()[0]
                return self.start()
        print('Invalid username or password')
        self.log_in()


    def create_account(self):
        print("Enter Username")
        user_name = input(">>> ")
        self.username = user_name
        print("Enter Password")
        password = input(">>>")
        self.password = password
        self.create_user()
        self.start()

    def start(self):
        self.show_menu()
        user_input = ""
        while user_input != "3":
            user_input = input(">>> ")
            if user_input =="1":
                main_menu(self.username, self.id)
            elif user_input =="2":
                self.show_scores()
            elif user_input =="3":
                print("Goodbye thanks for playing!")
                pass
            else:
                print("Invalid input please try again")
    
    def show_scores(self):
        sql = """
            SELECT highscore FROM highscores WHERE user_id = (?)
        """
        scores = CURSOR.execute(sql,(self.id,)).fetchall()
        print("/////YOUR SCORES/////")
        for i in scores:
            print(i[0])
        pass
                    
        
    def show_menu(self):
        print("Please choose an option:")
        print("1. Play Tetris")
        print("2. Scores")
        print("3. Exit")

CLI.create()
cli = CLI()
