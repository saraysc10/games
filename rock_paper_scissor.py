
import random
import tkinter.messagebox as msgbox
import tkinter.simpledialog as simpledialog

def jogar():
    options = ["rock", "paper", "scissors"]

    # Welcome phrase
    msgbox.showinfo("Rock, Paper and Scissors", "Welcome to the game!")

    # Ask the player to choose
    player = simpledialog.askstring("Choose", "Type rock, paper or scissors:").lower()

    if player not in options:
        msgbox.showwarning("Error", "Invalid selection! Please try again.")
        return

    # # Make the computer choose
    computer = random.choice(options)

    # Mostrar escolhas
    msgbox.showinfo("Result", f"You chose: {player}\nComputer chose: {computer}")

    # Verificação de vencedor
    if player == computer:
        result = "Even!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        result = "You won! 🎉"
    else:
        result = "You lost! 😢"

    # Show final result
    msgbox.showinfo("Final Result: ", result)

# Importante: Executar o jogo apenas se este arquivo for executado diretamente
if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter
    jogar()