import pandas as pd
import tkinter as tk

class GUI:
    def __init__(self):
        self.l = Logic()
    
    def start(self):
        window = tk.Tk()    
        label = tk.Label(text="test")
        label.pack()
        window.mainloop()   

class Logic:
    
    def send_query(self):
        pass


main = GUI()
main.start()
