import customtkinter as ctk
import verify_email
import modules.app as app

def verify_registration():
    if app.main_app.ENTRY_LOGIN._textvariable.get() and app.main_app.ENTRY_EMAIL._textvariable.get() and app.main_app.ENTRY_PASSWORD._textvariable.get() and app.main_app.ENTRY_REPEAT._textvariable.get():
        verification_email = verify_email.verify_email(app.main_app.ENTRY_EMAIL._textvariable.get())
        if verification_email == True:
            if app.main_app.ENTRY_PASSWORD._textvariable.get() == app.main_app.ENTRY_REPEAT._textvariable.get():
                username_data = app.main_app.CURSOR.execute("SELECT username FROM Users").fetchall()
                print(username_data)
                if not (app.main_app.ENTRY_LOGIN._textvariable.get()) in username_data:
                    email_data = app.main_app.CURSOR.execute("SELECT email FROM Users").fetchall()
                    print(email_data)
                    if not (app.main_app.ENTRY_EMAIL._textvariable.get()) in email_data:
                        app.main_app.CURSOR.execute("INSERT INTO Users (username, password, email) VALUES (?, ?, ?)", (app.main_app.ENTRY_LOGIN._textvariable.get(), app.main_app.ENTRY_PASSWORD._textvariable.get(), app.main_app.ENTRY_EMAIL._textvariable.get()))
                        app.main_app.DATABASE_CONNECTION.commit()
                        print("Тут має фрейм перемикатися")


def verify_authorization():
    if app.main_app.ENTRY_EMAIL_AUTH._textvariable.get() and app.main_app.ENTRY_PASSWORD_AUTH._textvariable.get():
        data = app.main_app.CURSOR.execute("SELECT password, email FROM Users").fetchall()
        if (app.main_app.ENTRY_PASSWORD_AUTH._textvariable.get(), app.main_app.ENTRY_EMAIL_AUTH._textvariable.get()) in data:
            print("Тут має фрейм перемикатися, але не")

def auth_tab():
    app.main_app.REGISTRATION_FRAME.place_forget()
    app.main_app.AUTHORIZATION_FRAME.place(x = 5, y = 5)

def register_tab():
    app.main_app.AUTHORIZATION_FRAME.place_forget()
    app.main_app.REGISTRATION_FRAME.place(x = 5, y = 5)