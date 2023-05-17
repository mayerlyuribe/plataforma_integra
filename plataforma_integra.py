# se importa tkintery sus funciones
import tkinter
from tkinter import*
from tkinter import messagebox
from tkinter import ttk

#---------------------------
# funciones
#---------------------------

#toplevel notas

def ir_toplevel_notas():
    global toplevel_notas
    toplevel_notas = Toplevel()
    toplevel_notas.title =("Notas")
    toplevel_notas.geometry("300x300")
    toplevel_notas.resizable(False,False)
    toplevel_notas.config(bg="coral1")

    #frame título

    frame_titulo = Frame(toplevel_notas, width=300, height=300)
    frame_titulo.config(bg="white", width=280, height=280)
    frame_titulo.place(x=10, y=10)

#toplevel salud

def ir_toplevel_salud():
    pass

#se crea la ventana principal ttk
principal= Tk()

#título de la ventana
principal.title=("PLATAFORMA INTEGRA")

#anchor de la ventana
principal.geometry("500x500")

#color de la ventana
principal.config(bg="black")

#variables globales

global notas
global salud



#--------------------------------
# barra menu
#--------------------------------
barra_menu = Menu()
principal.config(menu=barra_menu)

menu_convertir = Menu(tearoff=0)
menu_convertir.add_command(label="Convertir")
menu_convertir.add_separator()
menu_convertir.add_command(label="Borrar")

menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir")

barra_menu.add_cascade(label="Convertir", menu=menu_convertir)
barra_menu.add_cascade(label="Salir", menu=menu_salir)


#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(principal)
frame_entrada.config(bg="coral1", width=480, height=180)
frame_entrada.place(x=10, y=10)

# frame del nombre
nombre= Label(principal, text="Nombre:")
nombre.config(bg = "coral1",fg="black", font=("Helvetica", 20))
nombre.place(x=10,y=20)

#frame botones(2)

frame_botones = Frame(principal)
frame_botones.config(bg="coral1", width=480, height=120)
frame_botones.place(x=10, y=200)


notas=PhotoImage(file="img/notas.png")
salud=PhotoImage(file="img/salud.png")

# boton notas

boton_notas= Button(frame_botones, image=notas,command=ir_toplevel_notas)
boton_notas.place(x=100, y=10, width=100, height=100)
boton_notas.config(bg="coral1")

#boton salud

boton_salud= Button(frame_botones, image=salud, command=ir_toplevel_salud)
boton_salud.place(x=280, y=10, width=100, height=98)
boton_salud.config(bg="coral1")

# frame resultados

frame_resultados = Frame(principal)
frame_resultados.config(bg="coral1", width=480, height=160)
frame_resultados.place(x=10, y=330)

# area de texto para los resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier", 12))
t_resultados.place(x=10,y=10,width=460,height=140)

# caja de texto para nombre
nombre_c = Entry(principal,)
nombre_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=10)
nombre_c.focus_set()
nombre_c.place(x=115,y=20)

# texto de la fecha de nacimiento

nacimiento= Label(principal, text="Fecha de nacimiento:")
nacimiento.config(bg = "coral1",fg="black", font=("Helvetica", 20))
nacimiento.place(x=10,y=55)

# caja de texto para fecha de nacimiento
nombre_c = Entry(principal,)
nombre_c.config(bg="white", fg="blue", font=("Times New Roman", 18), width=10)
nombre_c.focus_set()
nombre_c.place(x=268,y=55)


# escudo
logo= PhotoImage(file="img/escudo_colegio.png")
logo= Label(frame_entrada, image=logo, bg="white")
logo.place(x=70,y=300)


principal.mainloop()