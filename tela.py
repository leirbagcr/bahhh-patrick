import tkinter as tk
from tkinter import messagebox

def verificar_login():
    email = entry_email.get()
    senha = entry_senha.get()
    
    if email and senha:
        # Simulação de login bem-sucedido
        messagebox.showinfo("Sucesso", "✅ Login realizado com sucesso!\nBem-vindo ao Gmail!")
        # Aqui você poderia fechar a janela ou abrir outra tela
        # root.destroy()  # descomente se quiser fechar após login
    else:
        messagebox.showerror("Erro", "Por favor, preencha email e senha.")

# ====================== CRIAÇÃO DA JANELA ======================
root = tk.Tk()
root.title("Gmail - Entrar")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#f8f9fa")

# Logo do Gmail (texto simulando)
tk.Label(root, text="Arthur", font=("Arial", 60, "bold"), fg="#4285F4", bg="#f8f9fa").pack(pady=(40, 10))
tk.Label(root, text="Gmail", font=("Arial", 22, "bold"), fg="#202124", bg="#f8f9fa").pack(pady=(0, 30))

# Campo de Email
tk.Label(root, text="Email ou telefone", font=("Arial", 11), fg="#5f6368", bg="#f8f9fa", anchor="w").pack(pady=(0, 5), padx=50, fill="x")
entry_email = tk.Entry(root, font=("Arial", 14), width=30, relief="solid", bd=1)
entry_email.pack(pady=(0, 20), padx=50, ipady=8)

# Campo de Senha
tk.Label(root, text="Senha", font=("Arial", 11), fg="#5f6368", bg="#f8f9fa", anchor="w").pack(pady=(0, 5), padx=50, fill="x")
entry_senha = tk.Entry(root, font=("Arial", 14), width=30, relief="solid", bd=1, show="●")
entry_senha.pack(pady=(0, 20), padx=50, ipady=8)

# Botão de Verificação / Entrar
btn_login = tk.Button(root, text="Entrar", font=("Arial", 14, "bold"), 
                      bg="#1a73e8", fg="white", activebackground="#185abc",
                      activeforeground="white", relief="flat", height=2, width=20,
                      command=verificar_login)
btn_login.pack(pady=20)

# Link "Esqueceu a senha?"
tk.Label(root, text="Esqueceu a senha?", fg="#1a73e8", bg="#f8f9fa", cursor="hand2").pack(pady=10)

# Rodapé
tk.Label(root, text="Não é sua conta? ", fg="#5f6368", bg="#f8f9fa").pack(side="bottom", pady=30)
tk.Label(root, text="Usar outra conta", fg="#1a73e8", bg="#f8f9fa", cursor="hand2").pack(side="bottom", pady=(0, 30))

root.mainloop()