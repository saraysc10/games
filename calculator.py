import tkinter.messagebox as msgbox
import tkinter.simpledialog as simpledialog
import math
import operator

def calculator():

    msgbox.showinfo("Hello","Welcome to the calculator!")

    player=simpledialog.askinteger("Choose","Type a number:")
    operator=simpledialog.askstring("Choose","Type an operator:")
    player2=simpledialog.askinteger("Choose","Type a second number:")

    op = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y,
          '/': lambda x, y: x / y,
          '%': lambda x, y: x % y,
          '^': lambda x, y: x ^ y
          }

    if math.isnan(player) or math.isnan(player2):
        msgbox.showwarning("Error", "Choose a valid number")
        return
    elif operator not in op:
        msgbox.showwarning("Error", "Choose a valid operator")
        return
    else:
        result=op[operator](player,player2)
        msgbox.showinfo("Result:", f" {result}")



if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    root.withdraw()
    calculator()
