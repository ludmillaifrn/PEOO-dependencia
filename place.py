import tkinter as tk 

janela = tk.Tk()
janela.geometry("300x200")

botao = tk.Button(janela, text="clique aqui")
botao.place(x=100, y=80, width=100, height=30)

janela.mainloop()