from tkinter import *
from tkinter import Tk, ttk

#cores

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#483D8B"  # DarkSlateBlue
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#4169E1"   # azul
co7 = "#4682B4"   # SteelBlue
co8 = "#C0C0C0"   # Silver
co9 = "#708090"   # SlateGray

cores = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

#criando janela
janela = Tk()
janela.title()
janela.geometry('900x630')
janela.configure(background=co7)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")
janela.mainloop()
