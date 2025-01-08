import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import itertools

# Função de cálculo
def calculadora(num1, num2, operacao):
    try:
        if operacao == 1:
            return num1 + num2
        elif operacao == 2:
            return num1 - num2
        elif operacao == 3:
            return num1 * num2
        elif operacao == 4:
            if num2 != 0:
                return num1 / num2
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

# Alternar imagens de fundo
def animar_fundo():
    current_image = next(background_images)
    bg_label.config(image=current_image)
    root.after(100, animar_fundo)

# Configuração principal da janela
root = tk.Tk()
root.title("Calculadora com Interface Personalizada")
root.geometry("600x400")

# Carregar imagens de fundo (substitua pelos caminhos das suas imagens)
images = [ImageTk.PhotoImage(Image.open(f"pokemon{i}.png").resize((600, 400))) for i in range(1, 4)]
background_images = itertools.cycle(images)

# Adicionar fundo animado
bg_label = tk.Label(root)
bg_label.place(relwidth=1, relheight=1)
animar_fundo()

# Frame principal para os elementos da interface
frame = tk.Frame(root, bg="white", relief="raised", bd=5)
frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=300)

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
btn_image = ImageTk.PhotoImage(Image.open("botao_calcular.png").resize((150, 50)))
btn_calcular = tk.Button(frame, image=btn_image, command=calcular, bd=0, bg="white")
btn_calcular.pack(pady=20)

# Label de resultado
label_result = tk.Label(frame, text="", font=("Arial", 14, "bold"), bg="white", fg="green")
label_result.pack(pady=5)

# Iniciar a aplicação
root.mainloop()
