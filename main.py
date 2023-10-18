from tkinter import *

root = Tk()
root.title("Calculadora Python")
root.geometry("4008x355")
root.minsize(408,355)
root.maxsize(408,355)

numero1 = ""
divisão = FALSE
multiplica = FALSE
adição = FALSE
subtração = FALSE

root.configure(background="#000000")

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg="#ffffff", bg="#202121", font=("Futura",25,"bold"), justify=CENTER )
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2 
)
#Funções operadores
def botão_click(num):
    e.insert(END, num)
def botão_divisao():
    global numero1
    global divisão
    divisão = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botão_multiplica():
    global numero1
    global multiplica
    multiplica = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botão_subtração():
    global numero1
    global subtração
    subtração = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botão_adição():
    global numero1
    global adição
    adição = TRUE
    numero1 = e.get()
    e.delete(0, END)
def botão_limpar():
    e.delete(0, END)
def botão_igual():
    global subtração
    global adição
    global multiplica
    global divisão
    numero2 = e.get()
    e.delete(0, END)
    if adição == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        adição = FALSE
    if multiplica == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplica = FALSE
    if subtração == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtração = FALSE
    if divisão == TRUE:
        e.insert(0, int(numero1) / int(numero2))
        divisão = FALSE
botão_de_divisão = Button(root,
                          text="÷",
                          padx=40,
                          pady=20,
                          command=botão_divisao,
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
) 
botão_de_divisão.grid(row=0, column=4)
#primeira fileira 
um = Button(root,
                          text="1",
                          padx=40,
                          pady=20,
                          command=lambda: botão_click(1),
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
um.grid(row=1, column=1)
dois = Button(root,
                          text="2",
                          padx=40,
                          pady=20,
                          command=lambda: botão_click(2),
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
dois.grid(row=1, column=2)
tres = Button(root,
                          text="3",
                          padx=40,
                          pady=20,
                          command=lambda: botão_click(3),
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
tres.grid(row=1, column=3)
multiplica = Button(root,
                          text="×",
                          padx=40,
                          pady=20,
                          command=botão_multiplica,
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
multiplica.grid(row=1, column=4)
#segunda fileira
quatro = Button(root,
                          text="4",
                          padx=40,
                          pady=20,
                          command=lambda: botão_click(4),
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
quatro.grid(row=2, column=1)
cinco = Button(root,
                          text="5",
                          padx=40,
                          pady=20,
                          command=lambda: botão_click(5),
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
cinco.grid(row=2, column=2)
seis = Button(root,
                          text="6",
                          padx=40,
                          pady=20,
                          command=lambda: botão_click(6),
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
seis.grid(row=2, column=3)
menos = Button(root,
                          text="–",
                          padx=40,
                          pady=20,
                          command=botão_subtração,
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
menos.grid(row=2, column=4)
#terceira fileira
sete = Button(root,
                          text="7",
                          padx=40,
                          pady=20,
                          command=lambda: botão_click(7),
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
sete.grid(row=3, column=1)
oito= Button(root,
                          text="8",
                          padx=40,
                          pady=20,
                          command=lambda: botão_click(8),
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
oito.grid(row=3, column=2)
nove= Button(root,
                          text="9",
                          padx=40,
                          pady=20,
                          command=lambda: botão_click(9),
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
nove.grid(row=3, column=3)
mais = Button(root,
                          text="+",
                          padx=40,
                          pady=20,
                          command=botão_adição,
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
mais.grid(row=3, column=4)
#quarta fileira
zero = Button(root,
                          text="0",
                          padx=91,
                          pady=20,
                          command=lambda: botão_click(0),
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
zero.grid(row=4, column=1, columnspan=2)
limpa = Button(root,
                          text="c",
                          padx=40,
                          pady=20,
                          command=botão_limpar,
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
limpa.grid(row=4, column=3)
igual = Button(root,
                          text="=",
                          padx=40,
                          pady=20,
                          command=botão_igual,
                          fg="#ffffff",
                          activeforeground="#ffffff",
                          bg="#ff7300",
                          activebackground="#ff7300",
                          relief=FLAT,
                          font=("futura", 12, "bold")
)
igual.grid(row=4, column=4)
root.mainloop()
