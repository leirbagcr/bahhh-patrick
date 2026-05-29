import tkinter as tk
from tkinter import ttk, messagebox
import json

def formatar_cpf(event=None):
    """Formata o CPF automaticamente enquanto digita"""
    entry = cpf_entry
    value = entry.get().replace(".", "").replace("-", "").replace(" ", "")
    
    if len(value) > 11:
        value = value[:11]
    
    if len(value) >= 9:
        formatted = f"{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:11]}"
    elif len(value) >= 6:
        formatted = f"{value[:3]}.{value[3:6]}.{value[6:]}"
    elif len(value) >= 3:
        formatted = f"{value[:3]}.{value[3:]}"
    else:
        formatted = value
    
    entry.delete(0, tk.END)
    entry.insert(0, formatted)

def enviar():
    titular = titular_entry.get().strip()
    agencia = agencia_entry.get().strip()
    cpf = cpf_entry.get().strip()
    
    if not titular or not agencia or not cpf:
        messagebox.showwarning("Campos obrigatórios", "Por favor, preencha todos os campos!")
        return
    
    
    resposta_label.config(
        text=f"✅ Consulta realizada com sucesso!\n\n"
             f"Titular: {titular}\n"
             f"Agência: {agencia}\n"
             f"CPF: {cpf}",
        foreground="green"
    )
        
def cadastrar():
    conta = conta(titular_entry.get(),agencia_entry.get(),cpf_entry.get())
    with open("clientes.json", "r") as clientes_arq:
        clientes = json.load(clientes_arq)
    clientes.append({
        "titular": conta.titular,
        "agencia": conta.agencia,
        "numero": conta.numero,
        "cpf": conta.cpf,
        "saldo": conta.saldo,
        "senha": conta.semha,
        "chavepix": conta.chavepix
    })
    print (clientes)
    with open("clientes.json", "w") as clienetes_ecrita:
        json.dump(clientes, clienetes_ecrita, indent=4)
    resposta_label.configure(text=f"Conta: {conta.numero} titulo: {conta.titular} cadastrado com sucesso", fg="green")


root = tk.Tk()
root.title("Painel do Gerente")
root.geometry("500x450")
root.resizable(False, False)
root.configure(bg="#f0f2f5")


titulo = tk.Label(root, text="Painel do Gerente", font=("Arial", 18, "bold"), bg="#f0f2f5", fg="#1e3a8a")
titulo.pack(pady=20)


frame = tk.Frame(root, bg="#f0f2f5", padx=40, pady=20)
frame.pack(fill="both", expand=True)


tk.Label(frame, text="Titular:", font=("Arial", 11), bg="#f0f2f5", anchor="w").pack(fill="x")
titular_entry = tk.Entry(frame, font=("Arial", 11), width=40, relief="solid", borderwidth=1)
titular_entry.pack(pady=(0, 15), ipady=6)

tk.Label(frame, text="Agência:", font=("Arial", 11), bg="#f0f2f5", anchor="w").pack(fill="x")
agencia_entry = tk.Entry(frame, font=("Arial", 11), width=40, relief="solid", borderwidth=1)
agencia_entry.pack(pady=(0, 15), ipady=6)

tk.Label(frame, text="CPF:", font=("Arial", 11), bg="#f0f2f5", anchor="w").pack(fill="x")
cpf_entry = tk.Entry(frame, font=("Arial", 11), width=40, relief="solid", borderwidth=1)
cpf_entry.pack(pady=(0, 15), ipady=6)
cpf_entry.bind("<KeyRelease>", formatar_cpf)


btn_enviar = tk.Button(frame, text="ENVIAR", font=("Arial", 12, "bold"), 
                       bg="#2563eb", fg="white", height=2, width=20,
                       command=enviar, relief="flat", cursor="hand2")
btn_enviar.pack(pady=20)


resposta_label = tk.Label(frame, text="", font=("Arial", 10), bg="#f0f2f5", 
                         justify="center", wraplength=400)
resposta_label.pack(pady=10)

root.mainloop()