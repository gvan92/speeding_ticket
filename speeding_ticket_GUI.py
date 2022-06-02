#!/usr/bin/env python3

"""
Gregory Van

Description: A program with a GUI that helps a user calculate the speeding fine given the penalties, the speeding limit and the clocked speed.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from speedingfine import SpeedingFineCalculator
#Class for the Presentation layer
class SpeedingFineFrame(ttk.Frame):
    def __init__(self, parent):

        ttk.Frame.__init__(self, parent,padding="10 10 10 10")
        # Business tier class
        self.speedingFineCalculator = SpeedingFineCalculator()

        #Save the parent so we can call destroy on the parent window
        self.parent = parent
        
        # Define variables for text entry fields
        self.speedLimit= tk.DoubleVar()
        self.clockedSpeed= tk.DoubleVar()
        self.speedingFine= tk.DoubleVar()
       
        self.initComponents()
        
    def initComponents(self):
        self.pack()
        self.initMainFrame()
        self.initButtonsFrame()
        
 
    def initMainFrame(self):
        #Add implementation:
        #Create a new Frame object and use grid method to add it to the parent frame (self).
        #Create and place the 6 labels and 3 text entry boxes.
        #Connect the DoubleVar attributes declared in the constructor to the text entry boxes.

        mainFrame = ttk.Frame(self)

        mainFrame.grid(column=0, row=0)

        ttk.Label(mainFrame, text="Minimum: $" + str(SpeedingFineCalculator.minimumFine)).grid(
            column=0, row=0, sticky=tk.W, columnspan=2)

        ttk.Label(mainFrame, text="Penalty per MPH over the limit: $" + str(SpeedingFineCalculator.penaltyPerMPH)).grid(
            column=0, row=1, sticky=tk.W, columnspan=2)

        ttk.Label(mainFrame, text="Penalty for 50 MPH over the limit: $" + str(SpeedingFineCalculator.penalty50BeyondLimit)).grid(
            column=0, row=2, sticky=tk.W, columnspan=2)

        ttk.Label(mainFrame, text="Speed Limit:" + str()).grid(
            column=0, row=3, sticky=tk.W, padx=(0,100))
        ttk.Entry(mainFrame, width=25, textvariable=self.speedLimit).grid(
            column=1, row=3)

        ttk.Label(mainFrame, text="Clocked Speed:").grid(
            column=0, row=4, sticky=tk.W)
        ttk.Entry(mainFrame, width=25, textvariable=self.clockedSpeed).grid(
            column=1, row=4)

        ttk.Label(mainFrame, text="Speeding Fine:").grid(
            column=0, row=5, sticky=tk.W)
        ttk.Entry(mainFrame, width=25, textvariable=self.speedingFine, state="readonly").grid(
            column=1, row=5)
        
    def initButtonsFrame(self):
        #Add implementation:
        #Creates a new Frame object and use grid method to add it to the parent frame (self).
        #Create and place three buttons to this frame using grid method.
        #Add the corresponding event-handlers to the buttons.    
        buttonFrame = ttk.Frame(self)

        buttonFrame.grid(column=0, row=1)

        ttk.Button(buttonFrame, text="Calculate", command=self.calculateFine) \
            .grid(column=0, row=0, pady=20)
        ttk.Button(buttonFrame, text="Clear", command=self.clear) \
            .grid(column=1, row=0)
        ttk.Button(buttonFrame, text="Exit", command=self.parent.destroy) \
            .grid(column=2, row=0)
        
    def calculateFine(self):
        #Add implementation
        # Event-handler for the ‘Calculate’ button.
        # Read the values of Entry boxes corresponding to the speeding limit and clocked speed.
        # call the calculateSpeedingFine method on self.speedingFineCalculator object to calculate the fine,
        # populate the text entry box with the fine. 
        self.speedingFineCalculator.speedingLimit = float(
            self.speedLimit.get())
        self.speedingFineCalculator.clockedSpeed = float(
            self.clockedSpeed.get())
        self.speedingFine.set(self.speedingFineCalculator.calculateSpeedingFine(self.speedingFineCalculator.clockedSpeed))

    def clear(self):
        # Add implementation: clear all the text entry boxes
        self.speedLimit.set("0.0")
        self.clockedSpeed.set("0.0")
        self.speedingFine.set("0.0")
    
    def exit(self):
        self.parent.destroy()

        

def main():
    root = tk.Tk()
    root.title("Speeding Fine Calculator of Funnyville")
    SpeedingFineFrame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    
