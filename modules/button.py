import customtkinter as ctk
import modules.app as appa
import modules.button_functions as btn_func

verify_registration_btn = ctk.CTkButton(
    master = appa.main_app.REGISTRATION_FRAME, 
    text = "Підтвердити",
    width = 250, 
    height = 100, 
    corner_radius = 20, 
    border_width = 3, 
    border_color = "#911CEE",
    command = btn_func.verify_registration
)

verify_authorization_btn = ctk.CTkButton(
    master = appa.main_app.AUTHORIZATION_FRAME, 
    text = "Підтвердити",
    width = 250, 
    height = 100, 
    corner_radius = 20, 
    border_width = 3, 
    border_color = "#911CEE",
    command = btn_func.verify_authorization
)

auth_btn = ctk.CTkButton(
    master = appa.main_app.REGISTRATION_FRAME, 
    text = "Авторизуватися",
    width = 250, 
    height = 100, 
    corner_radius = 20, 
    border_width = 3, 
    border_color = "#911CEE",
    command = btn_func.auth_tab
)

reg_btn = ctk.CTkButton(
    master = appa.main_app.AUTHORIZATION_FRAME, 
    text = "Зареєструватися",
    width = 250, 
    height = 100, 
    corner_radius = 20, 
    border_width = 3, 
    border_color = "#911CEE",
    command = btn_func.register_tab
)

verify_registration_btn.place(x = 425, y = 490)
verify_authorization_btn.place(x = 425, y = 490)
auth_btn.place(x = 425, y = 600)
reg_btn.place(x = 425, y = 600)