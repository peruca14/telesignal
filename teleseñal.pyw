from tkinter import *
from tkinter.ttk import Combobox
from telegrama import *

class panel:
    def __init__(self, vent):
        self.wind = vent
        self.wind.resizable(0,0)
        self.wind.title("Panel de señales")
        self.wind.iconbitmap("iconomont.ico")

    # enter to send
        self.wind.bind('<KeyPress-Return>', self.entercommand)

    # Window and config
        # title
        self.titulo = Label(self.wind, text= "Señales", font= "Courgette 30 bold").grid(row= 0,column=1)
        self.titulo2 = Label(self.wind, text= "MONTT  -", font= "Verdana 30 bold").grid(row= 0,column=0)
        # subtitle
        self.margen = LabelFrame(self.wind, text= "Crea la señal", font= "arial 16 bold")
        self.margen.grid(columnspan=2, row=2, padx=5, pady=5)

        # entries
        self.lado = Label(self.margen, text= "lado :", font= "arial 16", pady= 10, width= 17).grid(row= 0, column= 0)
        self.ladoentra = Combobox(self.margen, width= 8, font= "arial 14", values= ['LONG', 'SHORT'])
        self.ladoentra.grid(row= 0, column= 2, padx= 10)

        # cripto-pair
        self.par = Label(self.margen, text= "Par :", font= "arial 16", pady= 10, width= 17).grid(row= 1, column= 0)
        self.parentra = Entry(self.margen, width= 8, font= "arial 14")
        self.parentra.grid(row=1, column= 2, padx= 10)
        self.Parborrar = Button(self.margen, text="X", font= "arial 10 bold", bg= "#F73D3D", command= self.borrar0)
        self.Parborrar.grid(row=1, column= 3, padx= 10)

        # 1
        self.E_P = Label(self.margen, text= "Precio de entrada :", font= "arial 16", pady= 10, width= 17).grid(row= 2, column= 0)
        self.E_Pentra = Entry(self.margen, width= 8, font= "arial 14")
        self.E_Pentra.grid(row=2, column= 2, padx= 10)
        self.E_Pborrar = Button(self.margen, text="X", font= "arial 10 bold", bg= "#F73D3D", command= self.borrar1)
        self.E_Pborrar.grid(row=2, column= 3, padx= 10)

        # 2
        self.SL = Label(self.margen, text= "Toma de perdidas :", font= "arial 16", pady= 10, width= 17).grid(row= 3, column= 0)
        self.SLentra = Entry(self.margen, width= 8, font= "arial 14")
        self.SLentra.grid(row= 3, column= 2, padx= 10)
        self.SLborrar = Button(self.margen, text="X", font= "arial 10 bold", bg= "#F73D3D", command= self.borrar2)
        self.SLborrar.grid(row= 3, column= 3, padx= 10)

        # 3
        self.TP = Label(self.margen, text= "Toma de ganancias :", font= "arial 16", pady= 10, width= 17).grid(row= 4, column= 0)
        self.TPentra = Entry(self.margen, width= 8, font= "arial 14")
        self.TPentra.grid(row= 4, column= 2, padx= 10)
        self.TPborrar = Button(self.margen, text="X", font= "arial 10 bold", bg= "#F73D3D", command= self.borrar3)
        self.TPborrar.grid(row= 4, column= 3, padx= 10)


    # Enter button
        self.mandar = Button(self.wind, text= "Enviar señal", font= "verdana 30 bold",bg= "#53E21D" ,command= self.entercommand)
        self.mandar.grid(columnspan=10,row= 5, padx= 5, pady=5)


    # Errase functions
    def borrar0(self):
        self.parentra.delete(0, END)

    def borrar1(self):
        self.E_Pentra.delete(0, END)

    def borrar2(self):
        self.SLentra.delete(0, END)

    def borrar3(self):
        self.TPentra.delete(0, END)


    # Funcion de crear la plantilla
    def getposicion(self):
        # Declarar el str final
        if  self.ladoentra.get() == "" or self.parentra.get() == "" or self.E_Pentra.get() == "" or self.SLentra.get() == "" or self.TPentra.get() == "":
            None
        else:
            if self.ladoentra.get() == "LONG":
                pdeganancia = float(self.TPentra.get()) - float(self.E_Pentra.get())
                pdeganancia = (pdeganancia*100)/float(self.E_Pentra.get())
                pdeganancia = abs(round(pdeganancia, 2))

                pdeperdida = float(self.E_Pentra.get()) - float(self.SLentra.get())
                pdeperdida = (pdeperdida*100)/float(self.E_Pentra.get())
                pdeperdida = abs(round(pdeperdida, 2))

            else:
                pdeganancia = float(self.E_Pentra.get()) - float(self.TPentra.get())
                pdeganancia = (pdeganancia*100)/float(self.E_Pentra.get())
                pdeganancia = abs(round(pdeganancia, 2))

                pdeperdida = float(self.SLentra.get()) - float(self.E_Pentra.get())
                pdeperdida = (pdeperdida*100)/float(self.E_Pentra.get())
                pdeperdida = abs(round(pdeperdida, 2))


            rb = round((pdeganancia / pdeperdida), 2)

            self.posicion = \
                "Side:  " + self.ladoentra.get() + \
                "\nPair:  " + self.parentra.get().upper() + \
                "\nEP:  " + self.E_Pentra.get() + \
                "\nSL:  " + self.SLentra.get() + \
                "\nSL %:  " + repr(pdeperdida) + \
                "\nTP:  " + self.TPentra.get() + \
                "\nTP %:  " + repr(pdeganancia) + \
                "\nRisk:  1 / " + repr(rb)


            #print(self.posicion)
            self.enviar_S()

    # Send to API
    def enviar_S(self):
        telegrama_api(self.posicion)


    def entercommand(self, event = 0):
        self.getposicion()
        self.borrar0()
        self.borrar1()
        self.borrar2()
        self.borrar3()


if __name__ == '__main__':
    vent = Tk()
    panel(vent)
    vent.mainloop()
