import random
from tkinter import *
from tkinter import ttk
import sys

class Game(Tk):
    def __init__(self):
        super().__init__()

        self.title("Rock Paper Scissors Lizard Spock")
        self.intro = ttk.Frame(self, padding = "20 10 10 10")
        self.intro.grid(column = 0, row = 0)
        self.mainframe = ttk.Frame(self, padding = "10 10 10 10")
        self.mainframe.grid(column = 0, row = 1, sticky = (N, W, E, S))

        self.choice = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

        self.player_score = 0
        self.comp_score = 0

        #Labels
        self.intro = ttk.Label(self.intro, text = "Welcome to Rock-Paper-Scissors-Lizard-Spock! Click a button to play.", font = 10, justify = CENTER)
        self.player_choice_text = ttk.Label(self.mainframe, text = "Your Choice:   ", font = 10)
        self.player_choice = ttk.Label(self.mainframe, text = "", font = 10)
        self.comp_choice_text = ttk.Label(self.mainframe, text = "Computer's Choice:   ", font = 10)
        self.comp_choice = ttk.Label(self.mainframe, text = "", font = 10)
        self.player_score_text = ttk.Label(self.mainframe, text = "Your Score:    ", font = 10)
        self.comp_score_text = ttk.Label(self.mainframe, text = "Computer's Score:    ", font = 10)
        self.player = ttk.Label(self.mainframe, text = self.player_score, font = 10)
        self.comp = ttk.Label(self.mainframe, text = self.comp_score, font = 10)
        self.results = ttk.Label(self.mainframe, text = f" \n ", font = 10)

        #Button Images
        self.rockphoto = PhotoImage(file = r"Rock3.png")
        self.paperphoto = PhotoImage(file = r"Paper3.png")
        self.scissorsphoto = PhotoImage(file = r"Scissors3.png")
        self.lizardphoto = PhotoImage(file = r"Lizard3.png")
        self.spockphoto = PhotoImage(file = r"Spock3.png")

        #Buttons
        self.rock_button = Button(self.mainframe, image = self.rockphoto, width = 150, height = 150, command = self.rock)
        self.paper_button = Button(self.mainframe, image = self.paperphoto, width = 150, height = 150, font = 10, command = self.paper)
        self.scissors_button = Button(self.mainframe, image = self.scissorsphoto, width = 150, height = 150, command = self.scissors)
        self.lizard_button = Button(self.mainframe, image = self.lizardphoto, width = 150, height = 150, command = self.lizard)
        self.spock_button = Button(self.mainframe, image = self.spockphoto, width = 150, height = 150, command = self.spock)
        self.reset_button = Button(self.mainframe, text = "Reset", font = 10, width = 10, command = self.reset).grid(column = 3, row = 7)
        self.quit_button = Button(self.mainframe, text = "Stop", font = 10, width = 10, command = self.quit).grid(column = 3, row = 8)

        #Gridding
        self.intro.grid(column = 0, row = 0)
        self.player_choice_text.grid(column = 1, row = 3, sticky = "e")
        self.player_choice.grid(column = 2, row = 3, sticky = "w")
        self.comp_choice_text.grid(column = 3, row = 3, columnspan = 2, sticky = "e")
        self.comp_choice.grid(column = 5, row = 3, sticky = "w")
        self.player_score_text.grid(column = 1, row = 5, sticky = "e")
        self.player.grid(column = 2, row = 5, sticky = "w")
        self.comp_score_text.grid(column = 3, row = 5, columnspan = 2, sticky = "e")
        self.comp.grid(column = 5, row = 5, sticky = "w")
        self.results.grid(column = 2, row = 4, columnspan = 3)
        self.rock_button.grid(column = 1, row = 1, padx = 5, pady = "0 20")
        self.paper_button.grid(column = 2, row = 1, padx = 5, pady = "0 20")
        self.scissors_button.grid(column = 3, row = 1, padx = 5, pady = "0 20")
        self.lizard_button.grid(column = 4, row = 1, padx = 5, pady = "0 20")
        self.spock_button.grid(column = 5, row = 1, padx = 5, pady = "0 20")

    
    def rock(self):
        b = random.choice(self.choice)
        
        if b == "Paper":
            result = f"Paper covers rock!  \nComputer wins."
        elif b == "Scissors":
            result = f"Rock breaks scissors! \nYou win."
        elif b == "Lizard":
            result = f"Rock crushes lizard! \nYou win."
        elif b == "Spock":
            result = f"Spock vapourises rock! \nComputer wins."
        else:
            result = "It's a draw!\n"
        self.player_choice.config(text = "Rock")
        self.comp_choice.config(text = b)
        self.results.config(text = result, justify = CENTER)
        if b == "Scissors" or b == "Lizard":
            self.player_score += 1
            self.player.config(text = self.player_score)
        elif b == "Paper" or b == "Spock":
            self.comp_score += 1
            self.comp.config(text = self.comp_score)

    def paper(self):
        b = random.choice(self.choice)
        if b == "Rock":
            result = f"Paper covers rock! \nYou win."
        elif b == "Scissors":
            result = f"Scissors cut paper! \nComputer wins."
        elif b == "Lizard":
            result = f"Lizard eats paper! \nComputer wins."
        elif b == "Spock":
            result = f"Paper disproves Spock! \nYou win."
        else:
            result = "It's a draw!\n"
        self.player_choice.config(text = "Paper")
        self.comp_choice.config(text = b)
        self.results.config(text = result, justify = CENTER)
        if b == "Rock" or b == "Spock":
            self.player_score += 1
            self.player.config(text = self.player_score)
        elif b == "Paper" or b == "Lizard":
            self.comp_score += 1
            self.comp.config(text = self.comp_score)

    def scissors(self):
        b = random.choice(self.choice)
        if b == "Rock":
            result = f"Rock breaks scissors! \nComputer wins."
        elif b == "Paper":
            result = f"Scissors cut paper! \nYou win."
        elif b == "Lizard":
            result = f"Scissors decapitate lizard! \nYou win."
        elif b == "Spock":
            result = f"Spock smashes scissors! \nComputer wins."
        else:
            result = "It's a draw!\n"
        self.player_choice.config(text = "Scissors")
        self.comp_choice.config(text = b)
        self.results.config(text = result, justify = CENTER)
        if b == "Paper" or b == "Lizard":
            self.player_score += 1
            self.player.config(text = self.player_score)
        elif b == "Rock" or b == "Spock":
            self.comp_score += 1
            self.comp.config(text = self.comp_score)

    def lizard(self):
        b = random.choice(self.choice)
        if b == "Rock":
            result = f"Rock crushes lizard! \nComputer wins."
        elif b == "Paper":
            result = f"Lizard eats paper! \nYou win."
        elif b == "Scissors":
            result = f"Scissors decapitate lizard! \nComputer wins."
        elif b == "Spock":
            result = f"Lizard poisons Spock! \nYou win."
        else:
            result = "It's a draw!\n"
        self.player_choice.config(text = "Lizard")
        self.comp_choice.config(text = b)
        self.results.config(text = result, justify = CENTER)
        if b == "Spock" or b == "Scissors":
            self.player_score += 1
            self.player.config(text = self.player_score)
        elif b == "Paper" or b == "Rock":
            self.comp_score += 1
            self.comp.config(text = self.comp_score)

    def spock(self):
        b = random.choice(self.choice)
        if b == "Rock":
            result = f"Spock vapourises rock! \nYou win."
        elif b == "Paper":
            result = f"Paper disproves Spock! \nComputer wins."
        elif b == "Scissors":
            result = f"Spock smashes scissors! \nYou win."
        elif b == "Lizard":
            result = f"Lizard poisons Spock! \nComputer wins."
        else:
            result = "It's a draw!\n"
        self.player_choice.config(text = "Spock")
        self.comp_choice.config(text = b)
        self.results.config(text = result, justify = CENTER)
        if b == "Rock" or b == "Scissors":
            self.player_score += 1
            self.player.config(text = self.player_score)
        elif b == "Paper" or b == "Lizard":
            self.comp_score += 1
            self.comp.config(text = self.comp_score)
        
    def reset(self):
        self.player_choice.config(text = "")
        self.comp_choice.config(text = "")
        self.player_score = 0
        self.comp_score = 0
        self.player.config(text = self.player_score)
        self.comp.config(text = self.comp_score)
        self.results.config(text = f" \n ")

    def quit(self):
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.mainloop()