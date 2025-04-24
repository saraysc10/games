import random
import tkinter.messagebox as msgbox
import tkinter.simpledialog as simpledialog
import math

def game():
    pair=['odd','even']
    msgbox.showinfo("Hello","Welcome to the game!")
    operator = simpledialog.askstring("Choose", "Choose 'odd' or 'even:'")
    if operator.lower().strip() not in pair:
        msgbox.showwarning("Error", "You did not choose odd or even. Please start again! ")
        return
    player=simpledialog.askinteger("Choose","Type a number from 1 to 10:")


    if math.isnan(player):
        msgbox.showwarning("Error", "Choose a number")
    elif player>10:
        msgbox.showwarning("Error", "Choose a number lower than 10!")
        return

    robot=random.randint(1,10)


    msgbox.showinfo("Robot:", f"You chose: {player}\n Robot chose:{robot}")



    if (player+robot)%2==0 and operator.lower().strip()=='even':
        result="The result is Even! Player won."
    elif (player+robot)%2==1 and operator.lower().strip()=='odd':
        result="The result is Odd! Player won!"
    elif (player + robot) % 2 == 0 and operator.lower().strip() == 'odd':
        result="The result is Even! Robot Won!"
    elif (player + robot) % 2 == 1 and operator.lower().strip() == 'even':
        result="The result is Odd! Robot Won!"

    """Final Result"""
    msgbox.showinfo("Result:", result)


if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    root.withdraw()
    game()
