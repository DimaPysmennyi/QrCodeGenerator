import customtkinter as ctk
import sqlite3 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("TriangleMonkey")
        self.geometry("1080x720+0+0")
        self.resizable(False, False)
        self.DATABASE_CONNECTION = sqlite3.connect("database.db")
        self.CURSOR = self.DATABASE_CONNECTION.cursor()
        self.USERS = '''
            CREATE TABLE IF NOT EXISTS Users (id integer PRIMARY KEY, username TEXT, password TEXT, email TEXT)
        '''
        self.CURSOR.execute(self.USERS)
        self.REGISTRATION_FRAME = ctk.CTkFrame(master = self, width = 1070, height = 710, corner_radius = 20, border_width = 3, border_color = "#911CEE")
        # self.REGISTRATION_FRAME.place(x = 5, y = 5)

        self.REGISTRATION_LABEL = ctk.CTkLabel(master = self.REGISTRATION_FRAME, text = "Реєстрація", font = ctk.CTkFont(family = "Arial", size = 30))
        self.REGISTRATION_LABEL.place(x = 470, y = 10)

        self.ENTRY_LOGIN = ctk.CTkEntry(master = self.REGISTRATION_FRAME, width = 500, height = 100, textvariable = ctk.StringVar(), border_color = "#911CEE")
        self.ENTRY_EMAIL = ctk.CTkEntry(master = self.REGISTRATION_FRAME, width = 500, height = 100, textvariable = ctk.StringVar(), border_color = "#911CEE")
        self.ENTRY_PASSWORD = ctk.CTkEntry(master = self.REGISTRATION_FRAME, width = 500, height = 100, textvariable = ctk.StringVar(), border_color = "#911CEE")
        self.ENTRY_REPEAT = ctk.CTkEntry(master = self.REGISTRATION_FRAME, width = 500, height = 100, textvariable = ctk.StringVar(), border_color = "#911CEE")

        self.ENTRY_LOGIN.place(x = 300, y = 50)
        self.ENTRY_EMAIL.place(x = 300, y = 160)
        self.ENTRY_PASSWORD.place(x = 300, y = 270)
        self.ENTRY_REPEAT.place(x = 300, y = 380)

        self.AUTHORIZATION_FRAME = ctk.CTkFrame(master = self, width = 1070, height = 710, corner_radius = 20, border_width = 3, border_color = "#911CEE")
        
        self.ENTRY_EMAIL_AUTH = ctk.CTkEntry(master = self.AUTHORIZATION_FRAME, width = 500, height = 100, textvariable = ctk.StringVar(), border_color = "#911CEE")
        self.ENTRY_PASSWORD_AUTH = ctk.CTkEntry(master = self.AUTHORIZATION_FRAME, width = 500, height = 100, textvariable = ctk.StringVar(), border_color = "#911CEE")
        
        self.AUTHORIZAION_LABEL = ctk.CTkLabel(master = self.AUTHORIZATION_FRAME, text = "Авторизацiя", font = ctk.CTkFont(family = "Arial", size = 30))
        self.AUTHORIZAION_LABEL.place(x = 470, y = 10)

        self.ENTRY_EMAIL_AUTH.place(x = 300, y = 160)
        self.ENTRY_PASSWORD_AUTH.place(x = 300, y = 270)

        # self.AUTHORIZATION_FRAME.place(x = 5, y = 5)
        self.REGISTRATION_FRAME.place(x = 5, y = 5)

main_app = App()