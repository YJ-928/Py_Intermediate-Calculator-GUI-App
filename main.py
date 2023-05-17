from tkinter import *
# ----------------------------------------- CONSTANTS ----------------------------------- #
index = 0
expression = ""
DISPLAY_FONT = ("Airel", 24)
BUTTON_FONT = ("Airel", 18)

# ------------------------- CALCULATING THE EXPRESSION --------------------------- #
def calculate():
    """Calculates the user inputs by fetching them from list"""
    global index,expression,count
    try:
        result = str(eval(expression))
        new_index = len(result)
    except SyntaxError:
        pass
    except UnboundLocalError:
        pass
    else:
        display.delete(0, END)
        index = 0
        display.insert(index,result)
        index = new_index + 1


# ----------------------------- FUNCTIONS ---------------------------------- #
def clear_func():
    """Clears the display"""
    global index,expression
    display.delete(0,END)
    index = 0
    expression = ""

def back_func():
    """Removes one item from expression"""
    global index,expression
    expression = expression[:-1]
    index -= 1
    display.delete(0,END)
    display.insert(0,expression)

def divide_func():
    """Inserts Divide sign"""
    global index,expression
    display.insert(index,"/")
    expression += "/"
    index += 1


def multiply_func():
    """Inserts multiply sign"""
    global index,expression
    display.insert(index, "*")
    expression += "*"
    index += 1


def subtract_func():
    """Inserts subtract sign"""
    global index,expression
    display.insert(index, "-")
    expression += "-"
    index += 1


def add_func():
    """Inserts add sign"""
    global index,expression
    display.insert(index, "+")
    expression += "+"
    index += 1


def insert_decimal():
    """Inserts '.'(decimal) Num"""
    global index,expression
    display.insert(index, ".")
    expression += "."
    index += 1

def insert_nine():
    """Inserts 9 Num"""
    global index,expression
    display.insert(index,"9")
    expression += "9"
    index += 1


def insert_eight():
    """Inserts 8 Num"""
    global index,expression
    display.insert(index, "8")
    expression += "8"
    index += 1


def insert_seven():
    """Inserts 7 Num"""
    global index,expression
    display.insert(index, "7")
    expression += "7"
    index += 1


def insert_six():
    """Inserts 6 Num"""
    global index,expression
    display.insert(index, "6")
    expression += "6"
    index += 1


def insert_five():
    """Inserts 5 Num"""
    global index,expression
    display.insert(index, "5")
    expression += "5"
    index += 1


def insert_four():
    """Inserts 4 Num"""
    global index,expression
    display.insert(index, "4")
    expression += "4"
    index += 1


def insert_three():
    """Inserts 3 Num"""
    global index,expression
    display.insert(index, "3")
    expression += "3"
    index += 1


def insert_two():
    """Inserts 2 Num"""
    global index,expression
    display.insert(index, "2")
    expression += "2"
    index += 1


def insert_one():
    """Inserts 1 Num"""
    global index,expression
    display.insert(index, "1")
    expression += "1"
    index += 1


def insert_zero():
    """Inserts 0 Num"""
    global index,expression
    display.insert(index, "0")
    expression += "0"
    index += 1


def key_pressed(event):
   """Displaying The Keyboard key that was pressed by the user"""
   global index,expression
   display.insert(index, event.char)
   index += 1
   expression += event.char



# ------------------------ UI SETUP FOR CALCULATOR --------------------- #
window = Tk()
window.title("Simple Calculator By YJ-928")
# window.geometry("500x600")
window.config(padx=50,pady=50,bg="Black")

# main cal display
display = Entry(width=15,font=DISPLAY_FONT, highlightthickness=0)
display.grid(row=0,column=0,columnspan=4)

# cal buttons
# first row
clear = Button(width=17, text="Clear", fg="Red", bg="Black",
               font=BUTTON_FONT, highlightthickness=0, command=clear_func)
clear.grid(row=2, column=0, columnspan=4)

# second row of calc
back = Button(width=12,text="Back", fg="Yellow", bg="Black",
               font=BUTTON_FONT, highlightthickness=0, command=back_func)
back.grid(row=4, column=0, columnspan=3)
divide = Button(width=2, text="/", fg="Blue", bg="Black",
                font=BUTTON_FONT, highlightthickness=0, command=divide_func)
divide.grid(row=4, column=3)

# third row of calc
seven = Button(width=2,text="7", fg="Orange", bg="Black",
               font=BUTTON_FONT, highlightthickness=0, command=insert_seven)
seven.grid(row=6, column=0)
eight = Button(width=2,text="8", fg="Orange", bg="Black",
               font=BUTTON_FONT, highlightthickness=0, command=insert_eight)
eight.grid(row=6, column=1)
nine = Button(width=2,text="9", fg="Orange", bg="Black",
              font=BUTTON_FONT, highlightthickness=0, command=insert_nine)
nine.grid(row=6, column=2)
multiply = Button(width=2, text="*", fg="Blue", bg="Black",
                  font=BUTTON_FONT, highlightthickness=0, command=multiply_func)
multiply.grid(row=6, column=3)


# fourth row of calc
four = Button(width=2, text="4", fg="Orange", bg="Black",
              font=BUTTON_FONT, highlightthickness=0, command=insert_four)
four.grid(row=8, column=0)
five = Button(width=2, text="5", fg="Orange", bg="Black",
              font=BUTTON_FONT, highlightthickness=0, command=insert_five)
five.grid(row=8, column=1)
six = Button(width=2, text="6", fg="Orange", bg="Black",
             font=BUTTON_FONT, highlightthickness=0, command=insert_six)
six.grid(row=8, column=2)
minus = Button(width=2, text="-", fg="Blue", bg="Black",
               font=BUTTON_FONT, highlightthickness=0, command=subtract_func)
minus.grid(row=8, column=3)

# fifth row of calc
one = Button(width=2, text="1", fg="Orange", bg="Black",
             font=BUTTON_FONT, highlightthickness=0, command=insert_one)
one.grid(row=10, column=0)
two = Button(width=2, text="2", fg="Orange", bg="Black",
             font=BUTTON_FONT, highlightthickness=0, command=insert_two)
two.grid(row=10, column=1)
three = Button(width=2, text="3", fg="Orange", bg="Black",
               font=BUTTON_FONT, highlightthickness=0, command=insert_three)
three.grid(row=10, column=2)
plus = Button(width=2, text="+", fg="Blue", bg="Black",
              font=BUTTON_FONT, highlightthickness=0, command=add_func)
plus.grid(row=10, column=3)

# sixth row of calc
zero = Button(width=7, text="0", fg="Orange", bg="Black",
              font=BUTTON_FONT, highlightthickness=0, command=insert_zero)
zero.grid(row=12, column=0,columnspan=2)
decimal = Button(width=2, text=".", fg="Blue", bg="Black",
              font=BUTTON_FONT, highlightthickness=0, command=insert_decimal)
decimal.grid(row=12, column=2)
equal = Button(width=2, text="=", fg="White", bg="Black",
               font=BUTTON_FONT, highlightthickness=0,command=calculate)
equal.grid(row=12, column=3)

# blanks between number lines for spacing
# between row-0 & row-2
blank = Label(fg="Black", bg="Black", highlightthickness=0, font=("Airel",15))
blank.grid(row=1,column=0,columnspan=4)
# between row-2 & row-4
blank = Label(fg="Black", bg="Black", highlightthickness=0, font=("Airel", 15))
blank.grid(row=3, column=0, columnspan=4)
# between row-4 & row-6
blank = Label(fg="Black", bg="Black", highlightthickness=0, font=("Airel", 15))
blank.grid(row=5, column=0, columnspan=4)
# between row-6 & row-8
blank = Label(fg="Black", bg="Black", highlightthickness=0, font=("Airel", 15))
blank.grid(row=7, column=0, columnspan=4)
# between row-8 & row-10
blank = Label(fg="Black", bg="Black", highlightthickness=0, font=("Airel", 15))
blank.grid(row=9, column=0, columnspan=4)
# between row-10 & row-12
blank = Label(fg="Black", bg="Black", highlightthickness=0, font=("Airel", 15))
blank.grid(row=11, column=0, columnspan=4)

# Inserting Keyboard key presses into display
window.bind("<Key>", key_pressed)

window.mainloop()