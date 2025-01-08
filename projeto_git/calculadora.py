import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import itertools

# Função de cálculo
def calculadora(primeiro_numero, segundo_numero, operador):
    try:
        if operador == 1:
            return primeiro_numero + segundo_numero
        elif operador == 2:
            return primeiro_numero - segundo_numero
        elif operador == 3:
            return primeiro_numero * segundo_numero
        elif operador == 4:
            if segundo_numero != 0:
                return primeiro_numero / segundo_numero
            else:
                return "Erro: Divisão por zero"
        else:
            return "Erro: Operação inválida"
    except Exception as e:
        return f"Erro: {e}"

# Função para exibir o resultado
def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operacao = int(selected_operation.get())
        resultado = calculadora(num1, num2, operacao)
        label_result.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")


# Configuração principal da janela
root = tk.Tk()
root.title("Calculadora com Interface Personalizada")
root.geometry("600x400")

# Carregar uma única imagem de fundo (substitua pelo caminho da sua imagem)
image = ImageTk.PhotoImage(Image.open("pokemon1.png").resize((600, 400)))

# Inicializar o label de fundo com a imagem
bg_label = tk.Label(root, image=image)
bg_label.pack()

# Frame principal para os elementos da interface
frame = tk.Frame(root, bg="white", relief="raised", bd=5)
frame.pack(fill="both", expand=True)

# Entradas e rótulos
tk.Label(frame, text="Primeiro Número:", font=("Arial", 12)).pack(pady=5)
entry_num1 = tk.Entry(frame, font=("Arial", 12))
entry_num1.pack(pady=5)

tk.Label(frame, text="Segundo Número:", font=("Arial", 12)).pack(pady=5)
entry_num2 = tk.Entry(frame, font=("Arial", 12))
entry_num2.pack(pady=5)

tk.Label(frame, text="Operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão):", font=("Arial", 12)).pack(pady=5)
selected_operation = tk.Entry(frame, font=("Arial", 12))
selected_operation.pack(pady=5)

# Botão personalizado
btn_image = ImageTk.PhotoImage(Image.open("botao_calcular.jpg").resize((150, 50)))
btn_calcular = tk.Button(frame, image=btn_image, command=calcular, bd=0, bg="white")
btn_calcular.pack(pady=20)

# Label de resultado
label_result = tk.Label(frame, text="", font=("Arial", 14, "bold"), bg="white", fg="green")
label_result.pack(pady=5)

# Iniciar o loop principal do Tkinter
root.mainloop()
