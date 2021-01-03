'''FRAME:Frames are rectangular regions on the screen.It is used to organize a
group of widgets.It works like a container.
ENTRY WIDGET:Entry widgets are the basic widgets of Tkinter used to get input,
i.e. text strings, from the user of an application. This widget allows the user
to enter a single line of text. If the user enters a string, which is longer
than the available display space of the widget, the content will be scrolled.
GRID:The Grid geometry manager puts the widgets in a 2-dimensional table. The
master widget is split into a number of rows and columns, and each “cell” in
the resulting table can hold a widget.
BUTTON:The Button widget is used to add buttons in a Python application. These
buttons can display text or images that convey the purpose of the buttons. You
can attach a function or a method to a button which is called automatically
when you click the button.'''

#Importing tkinter library.
import tkinter as tk
'''from tkinter import * imports every exposed object in Tkinter into your curr-
ent namespace.'''
from tkinter import *
#globally declare the expression variable.
expression=""
#Define a function to update the expression in the entry box.
def press(num):
    #point to the global expression variable
    global expression
    #concatenate the string to expression.
    expression=expression+str(num)
    #update the expression using set method.
    result.set(expression)
#Defining another function to evaluate the final expression.
def eval_final():
    #handle errors using try and except.
    try:
        global expression
        #evaluate the expression and convert the result to strings
        total=str(eval(expression))
        #update this to the result.
        result.set(total)
        #initialise the expression to empty string.
        expression=""
    #using an except to raise errors like zero division errors.
    except:
        result.set("math error")
        #initialise the expression to empty string.
        expression=""
# Returns the answer of the computation.
def ans():
    try:
        global expression
        #evaluate the expression and convert the result to strings
        total=str(eval(expression))
        #update this to the result.
        return result.set(total)
    except:
        pass
#Clear
def cls():
    global expression
    expression=""
    result.set(expression)
#Clear the screen.
def delete():
    global expression
    expression=""
    result.set(expression)
#import math library.
import math
#function definitions.
#Inverse of a number.
def inv():
    global expression
    result.set(1/(float(expression)))
#cosine of a number.
def cos():
    global expression
    #writing an if statement if expression is in fractional form.
    if "/" in expression:
        numerator=expression.split("/")[0]#splitting numerator with the backslash.
        denominator=expression.split("/")[1]#splitting denominator with the backslash.
        result.set(math.cos(float(numerator)/float(denominator)))
    else:
        result.set(math.cos(float(expression)))
#sine of a number.
def sin():
    global expression
    if "/" in expression:
        numerator=expression.split("/")[0]
        denominator=expression.split("/")[1]
        result.set(math.sin(float(numerator)/float(denominator)))
    else:
        result.set(math.sin(float(expression)))
#tangent of a number.
def tan():
    global expression
    if "/" in expression:
        numerator=expression.split("/")[0]
        denominator=expression.split("/")[1]
        result.set(math.tan(float(numerator)/float(denominator)))
    else:
        result.set(math.tan(float(expression)))
#cos inverse of a number.
def cosInv():
    global expression
    if "/" in expression:
        numerator=expression.split("/")[0]
        denominator=expression.split("/")[1]
        result.set(math.acos(float(numerator)/float(denominator)))
    else:
        result.set(math.acos(float(expression)))
#sin inverse of a number.
def sinInv():
    global expression
    if "/" in expression:
        numerator=expression.split("/")[0]
        denominator=expression.split("/")[1]
        result.set(math.asin(float(numerator)/float(denominator)))
    else:
        result.set(math.asin(float(expression)))
#tan inverse of a number.
def tanInv():
    global expression
    if "/" in expression:
        numerator=expression.split("/")[0]
        denominator=expression.split("/")[1]
        result.set(math.atan(float(numerator)/float(denominator)))
    else:
        result.set(math.atan(float(expression)))
#square root of a number.
def sqr_root():
    global expression
    if "/" in expression:
        numerator=expression.split("/")[0]
        denominator=expression.split("/")[1]
        result.set(math.sqrt(float(numerator)/float(denominator)))
    else:
        result.set(math.sqrt(float(expression)))
#natural logarithm of a number.
def logs():
    global expression
    if "/" in expression:
        numerator=expression.split("/")[0]
        denominator=expression.split("/")[1]
        result.set(math.log(float(numerator)/float(denominator)))
    else:
        result.set(math.log(float(expression)))
#logarithm with base 10 of a number.
def logsten():
    global expression
    if "/" in expression:
        numerator=expression.split("/")[0]
        denominator=expression.split("/")[1]
        result.set(math.log10(float(numerator)/float(denominator)))
    else:
        result.set(math.log10(float(expression)))
#factorial of a number.
def fact():
    global expression
    result.set(math.factorial(int(expression)))
#cube root of anumber.
def cb_root():
    global expression
    if "/" in expression:
        numerator=expression.split("/")[0]
        denominator=expression.split("/")[1]
        result.set((float(numerator)/float(denominator))**(1/3))
    else:
        result.set(float((expression))**(1/3))
#exponent of a number.
def expt():
    global expression
    e=2.718281828459045
    if "/" in expression:
        numerator=expression.split("/")[0]
        denominator=expression.split("/")[1]
        result.set(e**(float(numerator)/float(denominator)))
    else:
        result.set((e)**float(expression))
#Permuation
def eval_per():
    global expression
    n=str(expression.split(",")[0])#input of the type a,b is split to give [a,b].
    r=str(expression.split(",")[1])
    eval_1=math.factorial(int(n))/math.factorial(int(n)-int(r))
    result.set(int(eval_1))
#combination
def eval_combi():
    global expression
    n=str(expression.split(",")[0])
    r=str(expression.split(",")[1])
    eval_1=math.factorial(int(n))/((math.factorial(int(n)-int(r)))*(math.factorial(int(r))))
    result.set(int(eval_1))
#Create the main window for the application.
m=tk.Tk()
#Give title to the window
m.title("Scientific Calculator")
#Define the geometry of the window.
m.geometry("360x376")
#set window color.
m.configure(bg="steel blue")
#Adding an entry widget in the master window m
#Increasing the font of the entry widget.
large_font = ('Verdana',15)
#declaring result as a string variable.
result=StringVar()
#Adding an entry widget in the master window m
entry=tk.Entry(m,width=10, font = large_font, bd=10, bg = "ghost white",textvariable=result)
#Postioning of the entry grid.
entry.grid(row = 0, column=0, columnspan=4,sticky=EW)
#Creating a frame to add functions of a calculator.
frame2=tk.Frame(m)
frame2.grid(row=2,column=0)
'''Adding the functions nPr(),sqrt(),cos^-1(),cos(),7,4,1,0,(,pie to the frame in
the form of buttons.'''
button_per=tk.Button(frame2,text="nPr()",width=10,bg="azure3",command=eval_per)
button_per.grid(row=3,column=0)
button_trig=tk.Button(frame2,text="cos()",width=10,bg="SteelBlue3", command=cos)
button_trig.grid(row=4,column=0)
button_inver=tk.Button(frame2,text="cos^-1()",width=10,bg="SteelBlue3",command=cosInv)
button_inver.grid(row=5,column=0)
button_sqr=tk.Button(frame2,text="sqrt()",width=10,bg="light sea green",command=sqr_root)
button_sqr.grid(row=6,column=0)
button_num7=tk.Button(frame2,text="7",width=10,bg="IndianRed2",command=lambda:  press("7"))
button_num7.grid(row=7,column=0)
button_num4=tk.Button(frame2,text="4",width=10,bg="IndianRed2",command=lambda:  press("4"))
button_num4.grid(row=8,column=0)
button_num1=tk.Button(frame2,text="1",width=10,bg="IndianRed2",command=lambda:  press("1"))
button_num1.grid(row=9,column=0)
button_num0=tk.Button(frame2,text="0",width=10,bg="IndianRed2",command=lambda:  press("0"))
button_num0.grid(row=10,column=0)
button_opBrac=tk.Button(frame2,text="(",width=10,bg="SlateGray1",command=lambda:  press("("))
button_opBrac.grid(row=11,column=0)
button_pie=tk.Button(frame2,text="pie",width=10,bg="SlateGray1",command=lambda:  press("3.141592653589793238"))
button_pie.grid(row=12,column=0)
'''Creating another frame to add another column of functions.(U,D,R,L),cuberoot(
),sin^-1(),sin(),8,5,2,.,),e'''
frame3=tk.Frame(m)
frame3.grid(row=2,column=1)
button_arrow=tk.Button(frame3,text="log10() ",width=10,bg="azure3",command=logsten)#logarithm to base 10.
button_arrow.grid(row=3,column=1)
button_trigS=tk.Button(frame3,text="sin()",width=10,bg="SteelBlue3",command=sin)
button_trigS.grid(row=4,column=1)
button_inverS=tk.Button(frame3,text="sin^-1()",width=10,bg="SteelBlue3",command=sinInv)
button_inverS.grid(row=5,column=1)
button_cbrt=tk.Button(frame3,text="cuberoot()",width=10,bg="dark sea green",command=cb_root)
button_cbrt.grid(row=6,column=1)
button_num8=tk.Button(frame3,text="8",width=10,bg="IndianRed2",command=lambda:  press("8"))
button_num8.grid(row=7,column=1)
button_num5=tk.Button(frame3,text="5",width=10,bg="IndianRed2",command=lambda:  press("5"))
button_num5.grid(row=8,column=1)
button_num2=tk.Button(frame3,text="2",width=10,bg="IndianRed2",command=lambda:  press("2"))
button_num2.grid(row=9,column=1)
button_dot=tk.Button(frame3,text=".",width=10,bg="SlateGray1",command=lambda:  press("."))
button_dot.grid(row=10,column=1)
button_clsBrack=tk.Button(frame3,text=")",width=10,bg="SlateGray1",command=lambda:  press(")"))
button_clsBrack.grid(row=11,column=1)
button_e=tk.Button(frame3,text="e",width=10,bg="SlateGray1",command=lambda:  press("2.718281828459045"))
button_e.grid(row=12,column=1)
'''Creating a frame to add another column of functions.log(),tan^-1(),tan(),9,6,
3,f<-->d,C,exp,nCr.'''
frame4=tk.Frame(m)
frame4.grid(row=2,column=2)
button_log=tk.Button(frame4,text="logn()",width=10,bg="azure3",command=logs)#natural logarithm.
button_log.grid(row=3,column=2)
button_trigT=tk.Button(frame4,text="tan()",width=10,bg="SteelBlue3",command=tan)
button_trigT.grid(row=4,column=2)
button_invertrigT=tk.Button(frame4,text="tan^-1()",width=10,bg="SteelBlue3",command=tanInv)
button_invertrigT.grid(row=5,column=2)
button_num9=tk.Button(frame4,text=",(nPr&nCr)",width=10,bg="dark sea green",command=lambda: press(","))
button_num9.grid(row=6,column=2)
button_num6=tk.Button(frame4,text="9",width=10,bg="IndianRed2",command=lambda:  press("9"))
button_num6.grid(row=7,column=2)
button_num3=tk.Button(frame4,text="6",width=10,bg="IndianRed2",command=lambda:  press("6"))
button_num3.grid(row=8,column=2)
button_facD=tk.Button(frame4,text="3",width=10,bg="IndianRed2",command=lambda:  press("3"))
button_facD.grid(row=9,column=2)
button_exp=tk.Button(frame4,text="exp",width=10,bg="dark sea green",command=expt)
button_exp.grid(row=10,column=2)
button_cls=tk.Button(frame4,text="C",width=10,bg="LightPink1",command=cls)
button_cls.grid(row=11,column=2)
button_comb=tk.Button(frame4,text="nCr",width=10,bg="azure3",command=eval_combi)
button_comb.grid(row=12,column=2)
'''Creating another frame to add the functions to another column.x^-1,!,/,*,-,+,=,
ANS,AC,OFF.'''
frame5=tk.Frame(m)
frame5.grid(row=2,column=3)
button_inv=tk.Button(frame5,text="x^-1",width=10,bg="SteelBlue3",command=inv)
button_inv.grid(row=3,column=3)
button_fac=tk.Button(frame5,text="fact(!)",width=10,bg="light sea green",command=fact)
button_fac.grid(row=4,column=3)
button_div=tk.Button(frame5,text="/",width=10,bg="light sea green",command=lambda:  press("/"))
button_div.grid(row=5,column=3)
button_mul=tk.Button(frame5,text="*",width=10,bg="light sea green",command=lambda:  press("*"))
button_mul.grid(row=6,column=3)
button_sub=tk.Button(frame5,text="-",width=10,bg="light sea green",command=lambda:  press("-"))
button_sub.grid(row=7,column=3)
button_add=tk.Button(frame5,text="+",width=10,bg="light sea green",command=lambda:  press("+"))
button_add.grid(row=8,column=3)
button_eqls=tk.Button(frame5,text="=",width=10,bg="light sea green",command=eval_final)
button_eqls.grid(row=9,column=3)
button_rto=tk.Button(frame5,text="ANS",width=10,bg="LightPink1",command=ans)
button_rto.grid(row=10,column=3)
button_del=tk.Button(frame5,text="AC",width=10,bg="LightPink1",command=cls)
button_del.grid(row=11,column=3)
button_off=tk.Button(frame5,text="OFF",width=10,bg="red",command=m.quit)
button_off.grid(row=12,column=3)
m.mainloop()
