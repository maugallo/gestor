# GESTOR DE RESTAURANTE - MAIN:
"""
Código encargado de realizar el gestor completo. Tanto de su parte
front como de su parte back. Se implementan las librerías Tkinter,
datetime y random.
"""
from tkinter import (
    Tk,
    StringVar,
    FLAT,
    TOP,
    RIGHT,
    LEFT,
    BOTTOM,
    W,
    DISABLED,
    NORMAL,
    END,
)
from tkinter import filedialog, messagebox
import tkinter as tk
from random import randint
import datetime

# Clases:
class PanelSuperior(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=3, relief=FLAT, bg="#F1F1F1")
        self.pack(side=TOP)
        # Label:
        self.label = tk.Label(
            self,
            text="MAMA MIA'S",
            font=("Rome", 49, "bold"),
            fg="#ffffff",
            bg="#006900",
            width=26,
        )
        self.label.pack(padx=15)


class PanelIzquierdo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=20, relief=FLAT, bg="#F1F1F1")
        self.pack(side=LEFT)


class PanelCostos(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=0, relief=FLAT, bg="#980000", padx=30, pady=20)
        self.pack(side=BOTTOM)

        # Costo Comida:
        self.costocom = tk.Label(
            self,
            text="COSTO COMIDA",
            font=("Rome", 12, "bold"),
            bg="#980000",
            fg="#FEFFFF",
        )
        self.costocom.grid(row=0, column=0, sticky=W, padx=30)
        self.varcom = StringVar()
        self.entrycom = tk.Entry(
            self,
            font=("Rome", 12, "bold"),
            bd=1,
            width=10,
            state="readonly",
            textvariable=self.varcom,
        )
        self.entrycom.grid(row=0, column=1, ipadx=20)

        # Costo Bebida:
        self.costobeb = tk.Label(
            self,
            text="COSTO BEBIDA",
            font=("Rome", 12, "bold"),
            bg="#980000",
            fg="#FEFFFF",
        )
        self.costobeb.grid(row=1, column=0, sticky=W, padx=30)
        self.varbeb = StringVar()
        self.entrybeb = tk.Entry(
            self,
            font=("Rome", 12, "bold"),
            bd=1,
            width=10,
            state="readonly",
            textvariable=self.varbeb,
        )
        self.entrybeb.grid(row=1, column=1, ipadx=20)

        # Costo Postre:
        self.costopos = tk.Label(
            self,
            text="COSTO POSTRE",
            font=("Rome", 12, "bold"),
            bg="#980000",
            fg="#FEFFFF",
        )
        self.costopos.grid(row=2, column=0, sticky=W, padx=30)
        self.varpos = StringVar()
        self.entrypos = tk.Entry(
            self,
            font=("Rome", 12, "bold"),
            bd=1,
            width=10,
            state="readonly",
            textvariable=self.varpos,
        )
        self.entrypos.grid(row=2, column=1, ipadx=20)

        # Subtotal:
        self.subtotal = tk.Label(
            self,
            text="SUBTOTAL",
            font=("Rome", 12, "bold"),
            bg="#980000",
            fg="#FEFFFF",
        )
        self.subtotal.grid(row=0, column=2, sticky=W, padx=30)
        self.varsubtotal = StringVar()
        self.entrysubtotal = tk.Entry(
            self,
            font=("Rome", 12, "bold"),
            bd=1,
            width=10,
            state="readonly",
            textvariable=self.varsubtotal,
        )
        self.entrysubtotal.grid(row=0, column=3, ipadx=20)

        # Impuestos:
        self.impuesto = tk.Label(
            self,
            text="IMPUESTOS",
            font=("Rome", 12, "bold"),
            bg="#980000",
            fg="#FEFFFF",
        )
        self.impuesto.grid(row=1, column=2, sticky=W, padx=30)
        self.varimpuesto = StringVar()
        self.entryimpuesto = tk.Entry(
            self,
            font=("Rome", 12, "bold"),
            bd=1,
            width=10,
            state="readonly",
            textvariable=self.varimpuesto,
        )
        self.entryimpuesto.grid(row=1, column=3, ipadx=20)

        # Total:
        self.total = tk.Label(
            self,
            text="TOTAL",
            font=("Rome", 12, "bold"),
            bg="#980000",
            fg="#FEFFFF",
        )
        self.total.grid(row=2, column=2, sticky=W, padx=30)
        self.vartotal = StringVar()
        self.entrytotal = tk.Entry(
            self,
            font=("Rome", 12, "bold"),
            bd=1,
            width=10,
            state="readonly",
            textvariable=self.vartotal,
        )
        self.entrytotal.grid(row=2, column=3, ipadx=20)


class PanelComidas(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self.config(
            text="          PIZZAS",
            font=("Rome", 15, "bold"),
            bd=0,
            fg="#FEFFFF",
            bg="#006900",
            relief=FLAT,
        )
        self.pack(side=LEFT, ipadx=5)

        self.lista = [
            "Muzarella",
            "Margarita",
            "Napoliana",
            "Cuatro Quesos",
            "Pepperoni",
            "Hawaiana",
            "Marinara",
            "Champiñones",
        ]
        self.precios = [250, 170, 600, 230, 250, 200, 180, 190, 190]
        self.entry_com = []
        self.texto_com = []
        self.variable_com = []
        i = 0
        for comida in self.lista:
            # Checkbuttons:
            self.variable_com.append("")
            self.variable_com[i] = tk.IntVar()
            self.checkcomida = tk.Checkbutton(
                self,
                text=comida.title().upper(),
                font=("Courier", 15, "bold"),
                onvalue=1,
                offvalue=0,
                fg="#FEFFFF",
                bg="#006900",
                # Color de fondo al hacer click:
                activebackground="#006900",
                # Color de frente al hacer click:
                activeforeground="#FEFFFF",
                # Color del checkbox:
                selectcolor="#006900",
                variable=self.variable_com[i],
                command=lambda x=i: revisar_checkbox(
                    self.variable_com[x], self.entry_com[x], self.texto_com[x]
                ),
            )
            self.checkcomida.grid(row=i, column=0, sticky=W, ipady=5)

            # Entries:
            self.texto_com.append("")
            self.texto_com[i] = tk.StringVar()
            self.texto_com[i].set("0")
            self.entry_com.append("")
            self.entry_com[i] = tk.Entry(
                self,
                font=("Rome", 16, "bold"),
                bd=1,
                width=3,
                state=DISABLED,
                textvariable=self.texto_com[i],
            )
            self.entry_com[i].grid(row=i, column=1)
            i += 1

    def subtotal_com(self):
        i = 0
        subtotal_com = 0
        for cantidad in self.texto_com:
            numero = self.texto_com[i].get()
            subtotal_com = subtotal_com + (int(numero) * int(self.precios[i]))
            i += 1
        return subtotal_com


class PanelBebidas(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self.config(
            text="          BEBIDAS",
            font=("Rome", 15, "bold"),
            bd=0,
            fg="#FEFFFF",
            bg="#006900",
            relief=FLAT,
        )
        self.pack(side=LEFT, ipadx=5)

        self.lista = [
            "Villavicencio",
            "Coca-Cola",
            "Fanta",
            "Sprite",
            "Aquarius",
            "Corona",
            "Quilmes",
            "Copa Malbec",
        ]
        self.precios = [100, 150, 150, 150, 140, 300, 200, 900, 1090]
        self.entry_beb = []
        self.texto_beb = []
        self.variable_beb = []
        i = 0
        for bebida in self.lista:
            # Checkbuttons:
            self.variable_beb.append("")
            self.variable_beb[i] = tk.IntVar()
            self.checkbebida = tk.Checkbutton(
                self,
                text=bebida.title().upper(),
                font=("Courier", 15, "bold"),
                onvalue=1,
                offvalue=0,
                fg="#FEFFFF",
                bg="#006900",
                # Color de fondo al hacer click:
                activebackground="#006900",
                # Color de frente al hacer click:
                activeforeground="#FEFFFF",
                # Color del checkbox:
                selectcolor="#006900",
                variable=self.variable_beb[i],
                command=lambda x=i: revisar_checkbox(
                    self.variable_beb[x], self.entry_beb[x], self.texto_beb[x]
                ),
            )
            self.checkbebida.grid(row=i, column=0, sticky=W, ipady=5)

            # Entries:
            self.texto_beb.append("")
            self.texto_beb[i] = tk.StringVar()
            self.texto_beb[i].set("0")
            self.entry_beb.append("")
            self.entry_beb[i] = tk.Entry(
                self,
                font=("Rome", 16, "bold"),
                bd=1,
                width=3,
                state=DISABLED,
                textvariable=self.texto_beb[i],
            )
            self.entry_beb[i].grid(row=i, column=1)
            i += 1

    def subtotal_beb(self):
        i = 0
        subtotal_beb = 0
        for cantidad in self.texto_beb:
            numero = self.texto_beb[i].get()
            subtotal_beb = subtotal_beb + (int(numero) * int(self.precios[i]))
            i += 1
        return subtotal_beb


class PanelPostres(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master)
        self.config(
            text="          POSTRES",
            font=("Rome", 15, "bold"),
            bd=0,
            fg="#FEFFFF",
            bg="#006900",
            relief=FLAT,
        )
        self.pack(side=LEFT, ipadx=7)

        self.lista = [
            "Volcán",
            "Tiramisú",
            "Pana Cotta",
            "Gelato",
            "Cannoli",
            "Zuccotto",
            "Crostata",
            "Seada",
        ]
        self.precios = [300, 350, 350, 400, 250, 100, 100, 250, 250]
        self.entry_pos = []
        self.texto_pos = []
        self.variable_pos = []
        i = 0
        for postre in self.lista:
            # Checkbuttons:
            self.variable_pos.append("")
            self.variable_pos[i] = tk.IntVar()
            self.checkpostre = tk.Checkbutton(
                self,
                text=postre.title().upper(),
                font=("Courier", 15, "bold"),
                onvalue=1,
                offvalue=0,
                fg="#FEFFFF",
                bg="#006900",
                # Color de fondo al hacer click:
                activebackground="#006900",
                # Color de frente al hacer click:
                activeforeground="#FEFFFF",
                # Color del checkbox:
                selectcolor="#006900",
                variable=self.variable_pos[i],
                command=lambda x=i: revisar_checkbox(
                    self.variable_pos[x], self.entry_pos[x], self.texto_pos[x]
                ),
            )
            self.checkpostre.grid(row=i, column=0, sticky=W, ipady=5)

            # Entries:
            self.texto_pos.append("")
            self.texto_pos[i] = tk.StringVar()
            self.texto_pos[i].set("0")
            self.entry_pos.append("")
            self.entry_pos[i] = tk.Entry(
                self,
                font=("Rome", 16, "bold"),
                bd=1,
                width=3,
                state=DISABLED,
                textvariable=self.texto_pos[i],
            )
            self.entry_pos[i].grid(row=i, column=1)
            i += 1

    def subtotal_pos(self):
        i = 0
        subtotal_pos = 0
        for cantidad in self.texto_pos:
            numero = self.texto_pos[i].get()
            subtotal_pos = subtotal_pos + (int(numero) * int(self.precios[i]))
            i += 1
        return subtotal_pos


class PanelDerecho(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=0, relief=FLAT, bg="#006900")
        self.pack(side=RIGHT, padx=10)


class PanelCalculadora(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=2, relief=FLAT, bg="#006900")
        self.pack(side=TOP)
        # Entry:
        self.entry = tk.Entry(self, font=("Rome", 16, "bold"), width=22, bd=1)
        self.entry.grid(
            row=0,
            column=0,
            columnspan=35,
        )
        # Buttons:
        self.botones = [
            "7",
            "8",
            "9",
            "+",
            "4",
            "5",
            "6",
            "-",
            "1",
            "2",
            "3",
            "×",
            "R",
            "B",
            "0",
            "/",
        ]
        self.botones_guardados = []
        fila = 1
        columna = 0
        for boton in self.botones:
            self.boton = tk.Button(
                self,
                font=("Rome", 15, "bold"),
                text=boton.title(),
                fg="#FEFFFF",
                bg="#006900",
                bd=1,
                width=5,
                relief=FLAT,
            )
            self.boton.grid(row=fila, column=columna)
            columna += 1
            if columna == 4:
                fila += 1
                columna = 0
            self.botones_guardados.append(self.boton)

        self.botones_guardados[0].config(command=lambda: self.presionar_boton("7"))
        self.botones_guardados[1].config(command=lambda: self.presionar_boton("8"))
        self.botones_guardados[2].config(command=lambda: self.presionar_boton("9"))
        self.botones_guardados[3].config(command=lambda: self.presionar_boton("+"))
        self.botones_guardados[4].config(command=lambda: self.presionar_boton("4"))
        self.botones_guardados[5].config(command=lambda: self.presionar_boton("5"))
        self.botones_guardados[6].config(command=lambda: self.presionar_boton("6"))
        self.botones_guardados[7].config(command=lambda: self.presionar_boton("-"))
        self.botones_guardados[8].config(command=lambda: self.presionar_boton("1"))
        self.botones_guardados[9].config(command=lambda: self.presionar_boton("2"))
        self.botones_guardados[10].config(command=lambda: self.presionar_boton("3"))
        self.botones_guardados[11].config(command=lambda: self.presionar_boton("*"))
        self.botones_guardados[12].config(command=lambda: self.boton_total())
        self.botones_guardados[13].config(command=lambda: self.boton_borrar())
        self.botones_guardados[14].config(command=lambda: self.presionar_boton("0"))
        self.botones_guardados[15].config(command=lambda: self.presionar_boton("/"))

    def presionar_boton(self, numero):
        self.entry.insert(END, numero)

    def boton_borrar(self):
        self.entry.delete(0, END)

    def boton_total(self):
        operador = self.entry.get()
        try:
            total = str(eval(operador))
        except (SyntaxError, ZeroDivisionError):
            self.entry.delete(0, END)
            self.entry.insert(END, "Error")
        else:
            self.entry.delete(0, END)
            self.entry.insert(END, total)


class PanelRecibo(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=0, relief=FLAT, bg="gray")
        self.pack()
        # Panel:
        self.text = tk.Text(
            self,
            font=("Rome", 12, "bold"),
            bd=1,
            width=31,
            height=14,
        )
        self.text.grid(row=0, column=0)


class PanelBotones(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bd=2, relief=FLAT, bg="#980000")
        self.pack()
        # Buttons:
        self.botones = ["Total", "Recibo", "Guardar", "Reset"]
        self.botones_guardados = []
        i = 0
        for boton in self.botones:
            self.boton = tk.Button(
                self,
                text=boton.title(),
                font=("Rome", 12, "bold"),
                fg="#FEFFFF",
                bg="#980000",
                bd=2,
                width=6,
                relief=FLAT,
            )
            self.boton.grid(row=0, column=i)
            self.botones_guardados.append(self.boton)
            i += 1
        self.botones_guardados[0].config(command=self.boton_total)
        self.botones_guardados[1].config(command=self.boton_recibo)
        self.botones_guardados[2].config(command=self.boton_guardar)
        self.botones_guardados[3].config(command=self.boton_reset)

    def boton_total(self):
        subtotal_com = comidas.subtotal_com()
        subtotal_beb = bebidas.subtotal_beb()
        subtotal_pos = postres.subtotal_pos()

        self.subtotal = subtotal_com + subtotal_beb + subtotal_pos
        self.impuesto = self.subtotal * 0.07
        self.total = self.subtotal + self.impuesto

        costos.varcom.set(f" ${subtotal_com}")
        costos.varbeb.set(f" ${subtotal_beb}")
        costos.varpos.set(f" ${subtotal_pos}")
        costos.varsubtotal.set(f" ${self.subtotal}")
        costos.varimpuesto.set(f" ${round(self.impuesto,2)}")
        costos.vartotal.set(f" ${round(self.total,2)}")

    def boton_recibo(self):
        # Limpiar el visor
        recibo.text.delete(0.0, END)
        # Determinar número de recibo y fecha actual
        num_recibo = randint(10000, 99999)
        fecha = datetime.datetime.now()

        # Llenar el visor
        recibo.text.insert(END, "                FACTURA B - DATOS\n")
        recibo.text.insert(END, "-" * 55 + "\n")
        recibo.text.insert(
            END,
            f"Recibo N°{num_recibo}\nFecha: {fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}\n",
        )
        recibo.text.insert(END, "-" * 55 + "\n")
        recibo.text.insert(END, "Alimento - Cantidad - Precio\n")

        i = 0
        for elemento in comidas.texto_com:
            if elemento.get() > "0":
                precio = comidas.precios[i] * int(elemento.get())
                recibo.text.insert(
                    END,
                    f"{comidas.lista[i]} - {elemento.get()} - ${precio}\n",
                )
            i += 1

        i = 0
        for elemento in bebidas.texto_beb:
            if elemento.get() > "0":
                precio = bebidas.precios[i] * int(elemento.get())
                recibo.text.insert(
                    END,
                    f"{bebidas.lista[i]} - {elemento.get()} - ${precio}\n",
                )
            i += 1

        i = 0
        for elemento in postres.texto_pos:
            if elemento.get() > "0":
                precio = postres.precios[i] * int(elemento.get())
                recibo.text.insert(
                    END,
                    f"{postres.lista[i]} - {elemento.get()} - ${precio}\n",
                )
            i += 1

        recibo.text.insert(END, "-" * 55 + "\n")
        recibo.text.insert(
            END,
            f"Subtotal: ${self.subtotal}\nImpuestos: ${round(self.impuesto,2)}\nTotal: ${round(self.total,2)}\n",
        )
        recibo.text.insert(END, "-" * 55 + "\n¡Gracias por comer en Mama Mia's!")

    def boton_guardar(self):
        try:
            archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
            archivo.write(recibo.text.get(0.0, END))
            archivo.close()
        except AttributeError:
            messagebox.showerror("Error", "¡Su recibo no ha podido ser guardado!")
        else:
            messagebox.showinfo("Recibo", "¡Su recibo ha sido guardado!")

    def boton_reset(self):
        recibo.text.delete(0.0, END)
        for comida in comidas.entry_com:
            comida.config(state=DISABLED)
        for bebida in bebidas.entry_beb:
            bebida.config(state=DISABLED)
        for postre in postres.entry_pos:
            postre.config(state=DISABLED)

        for variable in comidas.variable_com:
            variable.set(0)
        for variable in bebidas.variable_beb:
            variable.set(0)
        for variable in postres.variable_pos:
            variable.set(0)

        for casilla in comidas.texto_com:
            casilla.set("0")
        for casilla in bebidas.texto_beb:
            casilla.set("0")
        for casilla in postres.texto_pos:
            casilla.set("0")

        costos.varcom.set("")
        costos.varbeb.set("")
        costos.varpos.set("")
        costos.varsubtotal.set("")
        costos.varimpuesto.set("")
        costos.vartotal.set("")


# Funciones:
def config_basica():
    app.geometry("1020x630")
    app.resizable(0, 0)
    app.title("Gestor de Restaurante")
    app.config(bg="#F1F1F1")
    app.iconphoto(True, tk.PhotoImage(file="icon.png"))


def revisar_checkbox(variable, entry, texto):
    if variable.get() == 1:
        entry.config(state=NORMAL)
        if entry.get() == "0":
            entry.delete(0, END)
        entry.focus()
    else:
        entry.config(state=DISABLED)
        texto.set("0")


# Variables:
app = Tk()

# Main:
config_basica()
superior = PanelSuperior(app)

izquierdo = PanelIzquierdo(app)
costos = PanelCostos(izquierdo)
comidas = PanelComidas(izquierdo)
bebidas = PanelBebidas(izquierdo)
postres = PanelPostres(izquierdo)

derecho = PanelDerecho(app)
calculadora = PanelCalculadora(derecho)
recibo = PanelRecibo(derecho)
botones = PanelBotones(derecho)


# Mantener la ventana abierta:
app.mainloop()
