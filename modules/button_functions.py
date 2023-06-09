import customtkinter as ctk
import verify_email
import modules.app as app
import os
import qrcode
from qrcode.image.styledpil import StyledPilImage
from PIL import Image

counter = 0
reg = None

def verify_registration():
    global reg
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
                        # print("Тут має фрейм перемикатися")
                        app.main_app.APP_FRAME.place(x = 5, y = 5)
                        os.mkdir(f"users/{app.main_app.ENTRY_LOGIN._textvariable.get()}")
                        reg = True
                        # os.chdir(f"users/{app.main_app.ENTRY_LOGIN._textvariable.get()}")


def verify_authorization():
    global reg
    if app.main_app.ENTRY_USERNAME_AUTH._textvariable.get() and app.main_app.ENTRY_PASSWORD_AUTH._textvariable.get():
        data = app.main_app.CURSOR.execute("SELECT password, username FROM Users").fetchall()
        if (app.main_app.ENTRY_PASSWORD_AUTH._textvariable.get(), app.main_app.ENTRY_USERNAME_AUTH._textvariable.get()) in data:
            # print("Тут має фрейм перемикатися, але не")
            app.main_app.APP_FRAME.place(x = 5, y = 5)
            reg = False

def auth_tab():
    app.main_app.REGISTRATION_FRAME.place_forget()
    app.main_app.AUTHORIZATION_FRAME.place(x = 5, y = 5)
    

def register_tab():
    app.main_app.AUTHORIZATION_FRAME.place_forget()
    app.main_app.REGISTRATION_FRAME.place(x = 5, y = 5)


def make_qrcode():
    global counter 
    QRCode = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10
    )
    try:
        counter += 1
        QRCode.add_data(app.main_app.URL_ENTRY._textvariable.get())
        QRCode.make(True)
        file = QRCode.make_image(back_color = app.main_app.IMAGE_COLOR, fill_color = app.main_app.BG_COLOR)
        if reg == True:
            file.save(f"users/{app.main_app.ENTRY_LOGIN._textvariable.get()}/{counter}.png")
            app.main_app.IMAGE_LABEL = ctk.CTkLabel(
                master = app.main_app.QR_CODE_FRAME, 
                text = "", 
                image = ctk.CTkImage(light_image = Image.open(f"users/{app.main_app.ENTRY_LOGIN._textvariable.get()}/{counter}.png"), size = (280, 280))
            )
        if reg == False:
            file.save(f"users/{app.main_app.ENTRY_USERNAME_AUTH._textvariable.get()}/{counter}.png")
            app.main_app.IMAGE_LABEL = ctk.CTkLabel(
                master = app.main_app.QR_CODE_FRAME, 
                text = "", 
                image = ctk.CTkImage(light_image = Image.open(f"users/{app.main_app.ENTRY_USERNAME_AUTH._textvariable.get()}/{counter}.png"), size = (280, 280))
            )
        app.main_app.IMAGE_LABEL.place(x = 0, y = 0)

    except:
        print("Введи нормально, а потім кнопку натискай, бидле")

def bg_color():
    frame = ctk.CTkFrame(
        master = app.main_app.APP_FRAME, 
        width = 535, 
        height = 260,
        corner_radius = 20,
        border_width = 3,
        border_color = "#911CEE"
    )

    def change_bg_color():
        app.main_app.BG_COLOR = (int(bg_color_entry_r._textvariable.get()), int(bg_color_entry_g._textvariable.get()), int(bg_color_entry_b._textvariable.get()))
        frame.place_forget()

    bg_color_entry_r = ctk.CTkEntry(
        master = frame, 
        width = 50, 
        height = 50, 
        # corner_radius = 20, 
        # border_width = 3, 
        # border_color = "#911CEE", 
        textvariable = ctk.StringVar(),
    )
    bg_color_entry_g = ctk.CTkEntry(
        master = frame, 
        width = 50, 
        height = 50, 
        # corner_radius = 20, 
        # border_width = 3, 
        # border_color = "#911CEE", 
        textvariable = ctk.StringVar(),
    )
    bg_color_entry_b = ctk.CTkEntry(
        master = frame, 
        width = 50, 
        height = 50, 
        # corner_radius = 20, 
        # border_width = 3, 
        # border_color = "#911CEE", 
        textvariable = ctk.StringVar(),
    )
    
    confirm_button = ctk.CTkButton(
        master = frame, 
        width = 235, 
        height = 100, 
        corner_radius = 20, 
        border_width = 3, 
        border_color = "#911CEE",
        fg_color = "#343638",
        hover_color = "#29292a",
        text = "Підтвердити",
        command = change_bg_color
    )

    r_label = ctk.CTkLabel(master = frame, font = ("Arial", 20), text = "R:")
    g_label = ctk.CTkLabel(master = frame, font = ("Arial", 20), text = "G:")
    b_label = ctk.CTkLabel(master = frame, font = ("Arial", 20), text = "B:")

    bg_color_entry_r.place(x = 180, y = 50)
    bg_color_entry_g.place(x = 240, y = 50)
    bg_color_entry_b.place(x = 300, y = 50)
    confirm_button.place(x = 150, y = 120)
    r_label.place(x = 180, y = 20)
    g_label.place(x = 240, y = 20)
    b_label.place(x = 300, y = 20)

    frame.place(x = 267, y = 225)


def image_color():
    frame = ctk.CTkFrame(
        master = app.main_app.APP_FRAME, 
        width = 535, 
        height = 260,
        corner_radius = 20,
        border_width = 3,
        border_color = "#911CEE"
    )

    def change_image_color():
        app.main_app.IMAGE_COLOR = (int(image_color_entry_r._textvariable.get()), int(image_color_entry_g._textvariable.get()), int(image_color_entry_b._textvariable.get()))
        frame.place_forget()

    image_color_entry_r = ctk.CTkEntry(
        master = frame, 
        width = 50, 
        height = 50, 
        # corner_radius = 20, 
        # border_width = 3, 
        # border_color = "#911CEE", 
        textvariable = ctk.StringVar(),
    )
    image_color_entry_g = ctk.CTkEntry(
        master = frame, 
        width = 50, 
        height = 50, 
        # corner_radius = 20, 
        # border_width = 3, 
        # border_color = "#911CEE", 
        textvariable = ctk.StringVar(),
    )
    image_color_entry_b = ctk.CTkEntry(
        master = frame, 
        width = 50, 
        height = 50, 
        # corner_radius = 20, 
        # border_width = 3, 
        # border_color = "#911CEE", 
        textvariable = ctk.StringVar(),
    )
    confirm_button = ctk.CTkButton(
        master = frame, 
        width = 235, 
        height = 100, 
        corner_radius = 20, 
        border_width = 3, 
        border_color = "#911CEE",
        fg_color = "#343638",
        hover_color = "#29292a",
        text = "Підтвердити",
        command = change_image_color,
    )

    r_label = ctk.CTkLabel(master = frame, font = ("Arial", 20), text = "R:")
    g_label = ctk.CTkLabel(master = frame, font = ("Arial", 20), text = "G:")
    b_label = ctk.CTkLabel(master = frame, font = ("Arial", 20), text = "B:")

    image_color_entry_r.place(x = 180, y = 50)
    image_color_entry_g.place(x = 240, y = 50)
    image_color_entry_b.place(x = 300, y = 50)
    confirm_button.place(x = 150, y = 120)
    r_label.place(x = 180, y = 20)
    g_label.place(x = 240, y = 20)
    b_label.place(x = 300, y = 20)

    frame.place(x = 267, y = 225)

# def version():
#     frame = ctk.CTkFrame(
#         master = app.main_app.APP_FRAME, 
#         width = 535, 
#         height = 260,
#         corner_radius = 20,
#         border_width = 3,
#         border_color = "#911CEE"
#     )

#     def change_image_color():
#         app.main_app.IMAGE_COLOR = (int(image_color_entry_r._textvariable.get()), int(image_color_entry_g._textvariable.get()), int(image_color_entry_b._textvariable.get()))
#         frame.place_forget()

#     image_color_entry_r = ctk.CTkEntry(
#         master = frame, 
#         width = 50, 
#         height = 50, 
#         # corner_radius = 20, 
#         # border_width = 3, 
#         # border_color = "#911CEE", 
#         textvariable = ctk.StringVar(),
#     )
#     image_color_entry_g = ctk.CTkEntry(
#         master = frame, 
#         width = 50, 
#         height = 50, 
#         # corner_radius = 20, 
#         # border_width = 3, 
#         # border_color = "#911CEE", 
#         textvariable = ctk.StringVar(),
#     )
#     image_color_entry_b = ctk.CTkEntry(
#         master = frame, 
#         width = 50, 
#         height = 50, 
#         # corner_radius = 20, 
#         # border_width = 3, 
#         # border_color = "#911CEE", 
#         textvariable = ctk.StringVar(),
#     )
#     confirm_button = ctk.CTkButton(
#         master = frame, 
#         width = 235, 
#         height = 100, 
#         corner_radius = 20, 
#         border_width = 3, 
#         border_color = "#911CEE",
#         fg_color = "#343638",
#         hover_color = "#29292a",
#         text = "Підтвердити",
#         command = change_image_color,
#     )

#     image_color_entry_r.place(x = 180, y = 50)
#     confirm_button.place(x = 150, y = 120)

#     frame.place(x = 267, y = 225)