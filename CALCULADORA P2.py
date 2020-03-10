from tkinter import *
from math import *
ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("400x450")
ventana.configure(background="gray10")
color_boton=("white")


def btnClik(num):
    global operador
    operador=operador+str(num)
    input_text.set(operador) 
    
def clear():
    global operador
    operador=("")
    input_text.set("0")

def operacion():
    global operador
    try:
        opera=str(eval(operador))
    except:
        clear()
        opera=("ERROR")
    input_text.set(opera)


ancho_boton=11
alto_boton=3
input_text=StringVar()
operador=""
clear()
Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(0)).place(x=17,y=180)
Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(1)).place(x=107,y=180)
Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(2)).place(x=197,y=180)
Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(3)).place(x=287,y=180)
Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(4)).place(x=17,y=240)
Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(5)).place(x=107,y=240)
Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(6)).place(x=197,y=240)
Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(7)).place(x=287,y=240)
Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(8)).place(x=17,y=300)
Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:btnClik(9)).place(x=107,y=300)
Button(ventana,text="+",bg="gray",width=ancho_boton,height=alto_boton,command=lambda:btnClik("+")).place(x=17,y=360)
Button(ventana,text="-",bg="gray",width=ancho_boton,height=alto_boton,command=lambda:btnClik("-")).place(x=107,y=360)
Button(ventana,text="*",bg="gray",width=ancho_boton,height=alto_boton,command=lambda:btnClik("*")).place(x=197,y=360)
Button(ventana,text="/",bg="gray",width=ancho_boton,height=alto_boton,command=lambda:btnClik("/")).place(x=287,y=360)
Button(ventana,text="C",bg="orange",width=ancho_boton,height=alto_boton,command=clear).place(x=287,y=300)
Button(ventana,text="=",bg="orange",width=ancho_boton,height=alto_boton,command=operacion).place(x=197,y=300)

Salida=Entry(ventana,font=('arial',20,'bold'),width=22,textvariable=input_text,bd=20,insertwidth=4,bg="powder blue",justify="right").place(x=10,y=60)

ventana.mainloop()
