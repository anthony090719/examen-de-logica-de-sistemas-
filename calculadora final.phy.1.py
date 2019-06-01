from tkinter import *

def Sumar():
    varres.set( "suma = " + str( float(vartxt1.get()) + float(vartxt2.get())))
def Restar():
    varres.set( "resta = " + str( float(vartxt1.get()) - float(vartxt2.get())))
def Multiplicar():
    varres.set( "multiplicacion = " + str( int(vartxt1.get()) * float(vartxt2.get())))
def Dividir():
    varres.set( "division = " + str( float(vartxt1.get()) / float(vartxt2.get())))
def Limpiar():
    varres.set("")
    vartxt1.set("")
    vartxt2.set("")

ventana = Frame(height=180,width=250)
ventana.pack(padx=5,pady=5)

vartxt1 = StringVar()
txt1 = Entry(ventana,textvariable=vartxt1).place(x=0,y=0) 
vartxt2 = StringVar()
txt2 = Entry(ventana,textvariable=vartxt2).place(x=130,y=0) 
varres = StringVar()
txtres = Entry(ventana,textvariable=varres,width=100).place(x=0,y=145)

bsum = Button(ventana,command=Sumar,text="sumar",padx=42,pady=5).place(x=0,y=25)
bres = Button(ventana,command=Restar,text="restar",padx=42,pady=5).place(x=130,y=25)
bmul = Button(ventana,command=Multiplicar,text="multiplicar",padx=30,pady=5).place(x=0,y=65)
bdiv = Button(ventana,command=Dividir,text="dividir",padx=42,pady=5).place(x=130,y=65)
blim = Button(ventana,command=Limpiar,text="limpiar",padx=110,pady=5).place(x=0,y=105)

ventana.mainloop()