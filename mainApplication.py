import tkinter as tk
import pygubu


class votingApplication:
    def __init__(self, master):
        self.interfaceBuilder = interfaceBuilder = pygubu.Builder()
        interfaceBuilder.add_from_file('designerFiles/mainMenu.ui')
        self.mainMenu = interfaceBuilder.get_object('mainMenu', master)


if __name__ == '__main__':
    root = tk.Tk()
    app = votingApplication(root)
    root.mainloop()
	# Testing
	# Add here