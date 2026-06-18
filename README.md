# 🔐 Sistema de Login - CustomTkinter

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/CustomTkinter-Modern_UI-green?style=for-the-badge">

## 📖 Descrição

Projeto simples de um sistema de login desenvolvido em Python.

Inicialmente o projeto foi criado utilizando o Tkinter padrão, mas posteriormente foi refeito utilizando o CustomTkinter para obter uma interface mais moderna e agradável.

## ✨ Funcionalidades

✔ Login de usuário

✔ Campo de senha oculto

✔ Verificação de credenciais

✔ Mensagens de sucesso e erro

✔ Tratamento de exceções

✔ Janela com tamanho fixo

## 🛠 Tecnologias

- Python
- CustomTkinter

## 🔑 Credenciais

| Usuário | Senha |
|----------|----------|
| admin | 123 |

## 📂 Estrutura

```text
Sistema de Login/
│
├── app.py
└── README.md
```

## 🚀 Como executar

### Instalar a biblioteca

```bash
pip install customtkinter
```

### Executar o programa

```bash
python app.py
```

## 📚 O que aprendi

Durante a criação deste projeto aprendi:

- Criar interfaces gráficas
- Trabalhar com botões
- Utilizar campos de entrada
- Fazer validações
- Tratar erros com try/except
- Migrar projetos de Tkinter para CustomTkinter

## 🔄 Antes e Depois

### Tkinter
Interface padrão do Python.

### CustomTkinter
Interface mais moderna com melhor aparência visual.

## 💻 Código Principal

```python
def login():
    try:
        nome = 'admin'
        senha2 = 123

        login1 = usuario.get()
        login2 = float(senha.get())

        if login1 == nome and login2 == senha2:
            texto1.configure(text='Logado com sucesso')
        else:
            texto1.configure(text='Usuario ou senha inválidos!')
    except ValueError:
        texto1.configure(text='Digite apenas números na senha')
```

## 👨‍💻 Autor

Feito por Rafael enquanto aprende Python e desenvolvimento de interfaces gráficas.

⭐ Se gostou do projeto, deixe uma estrela no repositório.
