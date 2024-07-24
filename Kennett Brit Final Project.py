""" Final Pokemon Element Checker
    Brit Kennett 2/26/2024
    This program is a variation of the classic rock paper scissors game. It has been
    modified to determine the winner of a pokemon battle based entirely on the elemental
    typing of that pokemon. User will choose which type they will use and the computer
    will randomly choose their pokemon typing. The results will display which element
    would win.
"""

from tkinter.font import Font         # JCT added for label font 
from tkinter import PhotoImage  
from ButtonEdit_breezypythongui import EasyFrame            # Edited breezypythongui to allow button background colors
import random

class RPSGame(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Water Grass Fire Game")

        # Label and field for the result
        self.addLabel(text = "Choose Your Pokemon", row = 1, column = 0, \
                      background = "lightgrey", font = "Roman")             #set background color to match window, set font
        self.addLabel(text = "Results", row = 1, column = 2, \
                      background = "lightgrey", font = "Modern")             #set background color to match window, set font

        #result field
        self.resultField = self.addTextField(text = "", row = 1, column = 2, width = 27)
        

       
        
        # Buttons for Elemental Typing Water, Grass, Fire
        # Edited breezypythongui to allow background colors for buttons
        self.addButton(text = "Water", row = 3, column = 0, command = lambda: self.play("Water"), \
                       background = "deepskyblue", font = "papyrus")
        self.addButton(text = "Grass", row = 3, column = 1, command = lambda: self.play("Grass"), \
                       background = "chartreuse", font = "papyrus")
        self.addButton(text = "Fire", row = 3, column = 2, command = lambda: self.play("Fire"), \
                       background = "orangered", font = "papyrus")

        #add quit button
        self.addButton(text = "Quit", row = 4, column = 1, command = self.quit, \
                       background = "white", font = "stencil")
        #add clear button
        self.addButton(text = "Clear", row = 4, column = 0, command = self.clear, \
                       background = "white", font = "stencil")
        
        #change buttons to row 2 image to row 1

        # Set Background Color
        self.setBackground("lightgrey")

        #Image placement
        imageLabel=self.addLabel(text ="",row=2,column=0,
                      sticky="NSEW")
        
        #image2
        imageLabel2=self.addLabel(text ="",row=2,column=1,
                      sticky="NSEW")
        
        #image3
        imageLabel3=self.addLabel(text ="",row=2,column=2,
                      sticky="NSEW")
        

        # Load the image file and associate it with the image label
        self.image=PhotoImage(file="images/water.gif")
        imageLabel["image"]=self.image
        #load image2
        self.image2=PhotoImage(file="images/grass.gif")
        imageLabel2["image"]=self.image2
        #load image3
        self.image3=PhotoImage(file="images/fire.gif")
        imageLabel3["image"]=self.image3

        # Set the font and color of the caption
        """removed text labels BK"""
        #font = Font(family="Verdana",size=20,slant="italic")
        #textLabel["font"] = font
        #textLabel["foreground"]="deepskyblue"
        #font = Font(family="Verdana",size=20,slant="italic")
        #textLabel2["font"] = font
        #textLabel2["foreground"]="chartreuse"
        #font = Font(family="Verdana",size=20,slant="italic")
        #textLabel3["font"] = font
        #textLabel3["foreground"]="orangered"
        #   JCT add above for display of image ----------------------


        
    # define play for the actual game portion
    def play(self, user_choice):
        """Play the game"""
        choices = ["Water", "Grass", "Fire"]
        computer_choice = random.choice(choices)

        # Determine the result
        if user_choice == computer_choice:
            result = "Ties"
        elif (user_choice == "Water" and computer_choice == "Fire") or \
             (user_choice == "Grass" and computer_choice == "Water") or \
             (user_choice == "Fire" and computer_choice == "Grass"):
            result = "Wins!"
        else:
            result = "Loses"

        # Display the result in new window
        self.messageBox(title = "Results",
                        message = f"{user_choice} vs {computer_choice}: {user_choice} {result}")
        self.resultField.setText(f"{user_choice} vs {computer_choice}: {user_choice} {result}")

    #define quit button
    def quit(self):
        self.master.destroy()
    #define clear button
    def clear(self):
        self.resultField = self.addTextField(text = "", row = 1, column = 2, width = 27)
        
# Instantiate and pop up the window.
if __name__ == "__main__":
    RPSGame().mainloop()
