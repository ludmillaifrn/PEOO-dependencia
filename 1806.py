#codigos 18 de Junho de 2025 / tentar reproduzir em casa /  

  # Elementos do Formulário:
#– Entry: Nome do usuário
 #– Checkbutton: Interesses:
#‣ Ex.: Programação, Design, Marketing
 #– Radiobutton: Gênero:
#‣ Masculino, Feminino, Outro
 #– Listbox: Linguagens favoritas:
#‣ Seleção múltipla (Python, Java, C++, JavaScript, etc.)
 #– Combobox: Nível de experiência:
#‣ Iniciante, Intermediário, Avançado 

import tkinter as tk 
from tkinter import ttk 

janela = tk.Tk()
janela.title("Formulário")

var = tk.IntVar ()
check = tk.Checkbutton ( janela , text = " Moda " , variable=var)
check.pack()
check = tk.Checkbutton ( janela , text = " Jornalismo " , variable=var)
check.pack()
check = tk.Checkbutton ( janela , text = " Marketing  " , variable=var)
check.pack()

janela.mainloop ()