from tkinter import *
from math import *
import tkinter.messagebox

expression = ""

def press(num):

    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():

    global expression

    if(expression==""):

        x = expression_field.get()
        expression = expression + x

    try:

        total = str(eval(expression))
        equation.set(total)
        if(float(total)==0):
            expression=""

        else:
            expression = total

    except:
        equation.set("Error")
        expression = " "
        pass


def clear():
    global expression
    expression = ""
    equation.set("")

def ScientifiC():
    gui.resizable(width=False, height=False)
    gui.geometry("680x410+0+0")

def StandarD():
    gui.resizable(width=False, height=False)
    gui.geometry("275x410+0+0")

def iExit():
    iExit = tkinter.messagebox.askyesno("Calculator","Do you want to Exit ?")
    if iExit > 0:
        gui.destroy()
        return

#========================================================================================================================================================================

if __name__ == "__main__":

    gui = Tk()

    gui.configure(background="Beige")

    gui.title("Calculator")

    gui.resizable(width = False, height = False)

    gui.geometry("275x390+0+0")

    equation = StringVar()

#=========================================================================================================================================================================

    menubar = Menu(gui)

    filemenu= Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=filemenu)
    filemenu.add_command(label="Standard",command = StandarD)
    filemenu.add_command(label="Scientific",command =  ScientifiC)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command = iExit )

    gui.config(menu=menubar)

    labeldisplay = Label(gui,text = "Scientific Calculator",font=('arial',22,'bold'),justify=CENTER).grid(row=0,column=4,columnspan=5,pady=1)
    labelldisplay = Label(gui, text="Developed by Mohammad Bilal", font=('arial', 10, 'bold'), justify=RIGHT).grid(row=6,column=6,columnspan=5)

    #========================================================================================================================================================================

    expression_field = Entry(gui,font=('Arial',15,'bold'),textvariable=equation,bd=25,insertwidth=2,bg="Gainsboro",justify='right').grid(row=0, column=0, columnspan=4, pady=2)

#========================================================================================================================================================================
    btn7 = Button(gui, text="7", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press(7), bd=4, bg="LightSlateGrey").grid(row=2, column=0, pady=1, padx=1)
    btn8 = Button(gui, text="8", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press(8), bd=4, bg="LightSlateGrey").grid(row=2, column=1, pady=1, padx=1)
    btn9 = Button(gui, text="9", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press(9), bd=4, bg="LightSlateGrey").grid(row=2, column=2, pady=1, padx=1)
    btndiv = Button(gui, text="÷", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press('/'), bd=4, bg="FireBrick").grid(row=2, column=3, pady=1, padx=1)

#========================================================================================================================================================================

    btn4 = Button(gui, text="4", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press(4), bd=4, bg="LightSlateGrey").grid(row=3, column=0, pady=1, padx=1)
    btn5 = Button(gui, text="5", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press(5), bd=4, bg="LightSlateGrey").grid(row=3, column=1, pady=1, padx=1)
    btn6 = Button(gui, text="6", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press(6), bd=4, bg="LightSlateGrey").grid(row=3, column=2, pady=1, padx=1)
    btnmul = Button(gui, text="x", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press('*'), bd=4, bg="FireBrick").grid(row=3, column=3, pady=1, padx=1)


#========================================================================================================================================================================

    btn1 = Button(gui, text="1", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press(1), bd=4, bg="LightSlateGrey").grid(row=4, column=0, pady=1, padx=1)
    btn2 = Button(gui, text="2", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press(2), bd=4, bg="LightSlateGrey").grid(row=4, column=1, pady=1, padx=1)
    btn3 = Button(gui, text="3", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press(3), bd=4, bg="LightSlateGrey").grid(row=4, column=2, pady=1, padx=1)
    btnadd = Button(gui, text="+", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press('+'), bd=4, bg="FireBrick").grid(row=4, column=3, pady=1, padx=1)


#========================================================================================================================================================================
    btndot = Button(gui, text=".", width=3, height=1, font=('Arial', 20, 'bold'),command=lambda: press('.'), bd=4, bg="grey").grid(row=5, column=0, pady=1, padx=1)
    btn0 = Button(gui, text="0", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press(0), bd=4, bg="LightSlateGrey").grid(row=5, column=1, pady=1, padx=1)
    btnequal = Button(gui, text="=", width=3, height=1, font=('Arial', 20, 'bold'), command= equalpress, bd=4, bg="grey").grid(row=5, column=2, pady=1, padx=1)
    btnsub = Button(gui, text="-", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press('-'), bd=4, bg="FireBrick").grid(row=5, column=3, pady=1, padx=1)

#========================================================================================================================================================================
    btnbl = Button(gui, text="(", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press("("), bd=4,bg="grey").grid(row=1, column=0, pady=1, padx=1)
    btnbr = Button(gui, text=")", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press(")"), bd=4,bg="grey").grid(row=1, column=1, pady=1, padx=1)
    btnsclear = Button(gui, text="C", width=3, height=1, font=('Arial', 20, 'bold'), command= clear, bd=4, bg="grey").grid(row=1, column=2, pady=1, padx=1)
    btnmod = Button(gui, text="%", width=3, height=1, font=('Arial', 20, 'bold'), command=lambda: press('%'), bd=4,bg="FireBrick").grid(row=1, column=3, pady=1, padx=1)

#=============================================================================================================================================================================

    btnpi = Button(gui, text="π", width=5, height=1, font=('Arial', 20, 'bold'), command= lambda:press("pi"), bd=4, bg="Gainsboro").grid(row=1, column=4, pady=1, padx=1)
    btnpow = Button(gui, text="X²", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda:press("**2"), bd=4, bg="Gainsboro").grid(row=1, column=5, pady=1, padx=1)
    btnapowx = Button(gui, text="X³", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("**3"),bd=4, bg="Gainsboro").grid(row=1, column=6, pady=1, padx=1)
    btnlog = Button(gui, text="log", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("log("), bd=4, bg="Gainsboro").grid(row=1, column=7, pady=1, padx=1)

#========================================================================================================================================================================

    btnsin = Button(gui, text="sin", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("sin("), bd=4,bg="LightSlateGrey").grid(row=2, column=4, pady=1, padx=1)
    btncos = Button(gui, text="cos", width=5, height=1, font=('Arial', 20, 'bold'), command= lambda:press("cos("), bd=4, bg="LightSlateGrey").grid(row=2, column=5, pady=1, padx=1)
    btntan = Button(gui, text="tan", width=5, height=1, font=('Arial', 20, 'bold'), command= lambda:press("tan("), bd=4, bg="LightSlateGrey").grid(row=2, column=6, pady=1, padx=1)
    btnlg = Button(gui, text="log2", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("log2("), bd=4, bg="Gainsboro").grid(row=2, column=7, pady=1, padx=1)

# ========================================================================================================================================================================

    btnsinh = Button(gui, text="sinh", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("sinh("), bd=4,bg="LightSlateGrey").grid(row=3, column=4, pady=1, padx=1)
    btncosh = Button(gui, text="cosh", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("cosh("), bd=4,bg="LightSlateGrey").grid(row=3, column=5, pady=1, padx=1)
    btntanh = Button(gui, text="tanh", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("tanh("), bd=4,bg="LightSlateGrey").grid(row=3, column=6, pady=1, padx=1)
    btnlgg= Button(gui, text="log10", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("log10("), bd=4,bg="Gainsboro").grid(row=3, column=7, pady=1, padx=1)

# ========================================================================================================================================================================

    btnasinh = Button(gui, text="asinh", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("asinh("),bd=4, bg="LightSlateGrey").grid(row=4, column=4, pady=1, padx=1)
    btnacosh = Button(gui, text="acosh", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("acosh("), bd=4, bg="LightSlateGrey").grid(row=4, column=5, pady=1, padx=1)
    btnatanh = Button(gui, text="atanh", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("atanh("),bd=4, bg="LightSlateGrey").grid(row=4, column=6, pady=1, padx=1)
    btnfac = Button(gui, text="fact", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("factorial("), bd=4, bg="Gainsboro").grid(row=4, column=7, pady=1, padx=1)

#========================================================================================================================================================================

    btnrd = Button(gui, text="RAD", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("radians("), bd=4, bg="Gainsboro").grid(row=5, column=4, pady=1, padx=1)
    btnaexp = Button(gui, text="Exp", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("exp("),bd=4, bg="Gainsboro").grid(row=5, column=6, pady=1, padx=1)
    btndeg = Button(gui, text="DEG", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("degrees("),bd=4, bg="Gainsboro").grid(row=5, column=5, pady=1, padx=1)
    btnlggg = Button(gui, text="log1p", width=5, height=1, font=('Arial', 20, 'bold'), command=lambda: press("log1p("), bd=4, bg="Gainsboro").grid(row=5, column=7, pady=1, padx=1)

    gui.mainloop()
