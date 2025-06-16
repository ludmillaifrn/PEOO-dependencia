# aula de POO 
import tkinter as tk 

janela = tk.Tk()

tk.Label (janela, text = "Usuario:").grid (row=0, column=0)
tk.Entry(janela).grid(row=0, column=1)

tk.Label (janela, text = "Senha:").grid(row=1, column=0)
tk.Entry(janela, show ="*").grid(row=1, column=1)

tk.Button (janela , text = "Entrar") .grid (row=2, column=0, columnspan=2)

janela.mainloop()
