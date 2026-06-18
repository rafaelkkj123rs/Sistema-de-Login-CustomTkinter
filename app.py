import customtkinter as ctk

def login():
    try:
        nome = 'admin'
        senha2 = 123

        login1 = usuario.get()
        login2 = float(senha.get())

        if login1 == nome and login2 == senha2:
            texto1.configure(text='Logado com sucesso')
        else:
            texto1.configure(text='Usuario ou senha Validos!')
    except ValueError:
        texto1.configure(text='Digite sua senha tem que se números')

tela = ctk.CTk()
tela.title('Sistema de Login')
tela.geometry('398x135')
tela.resizable(False,False)

usuario = ctk.CTkEntry(tela)
usuario.pack()

senha = ctk.CTkEntry(tela, show='#')
senha.pack(pady=5)

texto_usuario = ctk.CTkLabel(tela, text='Usuario')
texto_usuario.place(x=70, y=1)

texto_senha = ctk.CTkLabel(tela, text='Senha')
texto_senha.place(x=80, y=32)

botao = ctk.CTkButton(tela, text='logar', command=login)
botao.pack(pady=10)

texto1 = ctk.CTkLabel(tela, text='Digite seu login')
texto1.pack()
tela.mainloop()