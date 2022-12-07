from customtkinter import *
from datetime import *

#Função para rodar
def rodar():
    agora = datetime.now()
    hora = agora.strftime("%H:%M:%S")
    relogio.configure(text = hora)
    relogio.after(1000,rodar)
    
#Tela    
root= CTk()
root.geometry("400x200")
root.resizable(False,False)
root.configure(background="#363434")
root.title("Relogio digital")
root.iconbitmap("img/clock.ico")

f1= CTkFrame(fg_color="#363434", width=400, height=200, border_color="#424040", border_width=5)
f1.pack()

#Data
agora = datetime.now()
hoje = date.today()

#Label cima
relogio = CTkLabel(root,text_font="DS-Digital 84 bold",text_color="#ed2226")
rodar()

#Label baixo
dia = CTkLabel(root,text= agora.strftime("%A"),text_font="DS-Digital 14 bold",text_color="#ed2226")
day = CTkLabel(root,text= hoje,text_font="DS-Digital 14 bold",width=200, text_color="#ed2226")

#Place
relogio.place(x=15,y=30)
dia.place(x=25,y=125)
day.place(x=150,y=125)

root.mainloop()