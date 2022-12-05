from tkinter import *
from tkinter import ttk

# importando dependencias para o matplotlib

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib as plt
from matplotlib.figure import Figure

# Definindo Cores

co0 = "#f0f3f5"  # Cinza
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#6dd695"  # + profit
fundo = "#3F729B"

# Criando janela tkinter

janela = Tk()
janela.title('GEPEF APP')
janela.geometry('1190x500')
janela.resizable(width=FALSE, height=FALSE)


# Frame de cima para aplicar o nome da minha aplicação

Frame_top = Frame(janela, width=1360, height=45,
                  pady=0, padx=0, bg=co1, relief='flat')

Frame_top.grid(row=0, column=0)

# dividindo a janela principal em duas partes

Frame_quadro = Frame(janela, width=1360, height=700,
                     pady=15, padx=7, relief='flat')

Frame_quadro.grid(row=1, column=0, pady=6, sticky=NW)

# Configurando Frame Top

app_nome = Label(Frame_top, text='GEPEF ANALYTICS', width=20, height=2,
                 pady=1, padx=0, bg=co1, fg=co4, relief='flat', anchor=N, font=('Ivy 14 bold'))
app_nome.place(x=0, y=5)

# FRAME QUADROS (GRÁFICOS)

Frame_Total = Frame(Frame_quadro, width=200, height=90, bg=co1, relief='flat')
Frame_Total.place(x=0, y=0)

# TRAÇO AZUL QUE FICA NA PARTE SUPERIOR DE CADA LABEL
app_traco = Label(Frame_Total, text='', width=1, height=10,
                  pady=0, padx=0, bg=co2, fg=co4, relief='flat', anchor=NW, font=('Ivy 1 bold'))
app_traco.place(x=0, y=0)

# LABEL PARA O TITULO

app_nome = Label(Frame_Total, text='Total de Demandas', height=1,
                 pady=0, padx=0, bg=co1, fg=co4, relief='flat', anchor=CENTER, font=('Ivy 10 bold'))
app_nome.place(x=20, y=5)


janela.mainloop()
