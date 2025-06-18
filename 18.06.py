#codigos 18 de Junho de 2025 / tentar reproduzir em casa /  

  # Elementos do Formulário:
#– Entry: Nome do usuário - FEITO 
 #– Checkbutton: Interesses: Ex.: Programação, Design, Marketing - FEITO 
 #– Radiobutton: Gênero: ex :Masculino, Feminino, Outro - FEITO 
 #– Listbox: Linguagens favoritas: ex : Seleção múltipla (Python, Java, C++, JavaScript, etc.) - FEITO 
 #– Combobox: Nível de experiência: ex: Iniciante, Intermediário, Avançado - FEITO 

import tkinter as tk 
from tkinter import ttk 

janela = tk.Tk()
janela.geometry ("300x600")
janela.title("Formulário")

label_titulo = tk.Label (janela , text = "1. qaul o seu nome ?:")
label_titulo. pack()
campo_entrada = tk.Entry (janela , width = 30 )
campo_entrada.pack(pady=5)
label_titulo = tk.Label (janela , text = "2. Escolha seus interesses :")
label_titulo. pack()
var_Moda = tk.IntVar ()
check = tk.Checkbutton ( janela , text = " Moda " , variable=var_Moda)
check.pack()
var_Jornalismo= tk.IntVar ()
check = tk.Checkbutton ( janela , text = " Jornalismo " , variable=var_Jornalismo)
check.pack()
var_Marketing = tk.IntVar ()
check = tk.Checkbutton ( janela , text = " Marketing  " , variable=var_Marketing)
check.pack()


label_titulo = tk.Label (janela , text = "3. Qual o seu gênero ?  :")
label_titulo. pack()
opcao = tk.StringVar()
opcao.set("Gênero")
tk.Radiobutton(janela, text="Masculino",
variable=opcao, value="M").pack(anchor='w')
tk.Radiobutton(janela, text="Feminino",
variable=opcao, value="F").pack(anchor='w')
tk.Radiobutton(janela, text="Prefiro não informar",
variable=opcao, value="NI").pack(anchor='w')

label_titulo = tk.Label (janela , text = "4. Qual sua linguagem predileta ?:")
label_titulo. pack()
lista = tk.Listbox(janela)
lista.insert(1, "Python")
lista.insert(2, "Java")
lista.insert(3, "C++")
lista.insert(4, "Não gosto de programar!")
lista.pack()

label_titulo = tk.Label (janela , text = "5. Qual o seu nível de experiência ?:")
label_titulo. pack()
janela.title("Combobox com .get() e .bind()")
opcoes = ["Iniciante", "Intermediario", "Avançado", "não tenho ideia de nada"]
combobox = ttk.Combobox(janela, values=opcoes)
combobox.pack()
combobox.bind("<<ComboboxSelected>>",)

janela.mainloop ()