import customtkinter as ctk
from tkinter import *

janela = ctk.CTk()


class Aplication:
    # classe inicial que chama todas funcoes que precisam ser inicializadas junto com o programa.
    def __init__(self):
        self.janela = janela
        self.tema()
        self.tela()
        self.telaLogin()
        janela.mainloop()

    def button_function(self):
        print("button pressed")

    def tema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

    def tela(self):
        janela.geometry("700x400")
        janela.title("LOGIN")
        janela.iconbitmap("icon.ico")
        janela.resizable(False, False)
        # adiciona transparencia a tela
        janela.attributes("-alpha", 0.9)

    def telaLogin(self):
        # Imagem tela
        img = PhotoImage(file="logo.png").subsample(
            4
        )  # redimensiona a imagem pela metade
        label_img = ctk.CTkLabel(master=janela, text=None, image=img).pack(
            side="left", padx=(20, 10)
        )  # adiciona 10 pixels de espaçamento à direita da imagem

        # Texto tela
        title_label = ctk.CTkLabel(
            master=janela,
            text="Entre na sua conta  \n e tenha acesso à plataforma",
            font=("Roboto", 20),
            text_color="orange",
        ).place(x=15, y=10)

        # frame
        login_frame = ctk.CTkFrame(master=janela, width=350, height=396)
        login_frame.pack(side=RIGHT)

        # wi0dget dentro da tela LOGIN
        label = ctk.CTkLabel(
            master=login_frame,
            text="LOGIN",
            font=("Roboto", 20),
        )
        label.place(x=25, y=5)

        username_entry = ctk.CTkEntry(
            master=login_frame,
            placeholder_text="Digite seu usuário",
            width=300,
            font=("Roboto", 15),
        ).place(x=25, y=105)

        username_label = ctk.CTkLabel(
            master=login_frame,
            text="*campo obrigátorio",
            font=("Roboto", 8),
            text_color="green",
        ).place(x=25, y=135)

        password_entry = ctk.CTkEntry(
            master=login_frame,
            placeholder_text="Digite sua senha",
            width=300,
            font=("Roboto", 15),
            show="*",
        ).place(x=25, y=175)
        password_label = ctk.CTkLabel(
            master=login_frame,
            text="*campo obrigátorio",
            font=("Roboto", 8),
            text_color="green",
        ).place(x=25, y=205)

        checkbox = ctk.CTkCheckBox(
            master=login_frame, text="Lembrar de mim", font=("Roboto", 10)
        ).place(x=25, y=245)

        loginButton = ctk.CTkButton(
            master=login_frame,
            text="Entrar",
            command=self.button_function,
            font=("Roboto", 15),
            width=300,
            fg_color="orange",
        ).place(x=25, y=285)

        cadastrar_span = ctk.CTkLabel(
            master=login_frame,
            text="Se não tem conta, \n cadastre-se!",
            font=("Roboto", 15),
        ).place(x=25, y=325)
        cadastrarButton = ctk.CTkButton(
            master=login_frame,
            text="Cadastre-se",
            width=150,
            command=self.button_function,
            font=("Roboto", 15),
            fg_color="green",
            hover_color="#00B0F0",
        ).place(x=175, y=325)


Aplication()
