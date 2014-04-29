import Tkinter as tk

class Application(tk.Frame):

	def __init__(self, parent = None):
		tk.Frame.__init__(self, parent)
		self.parent = parent
		self.createWidgets()
		self.setupUI()

	def setupUI(self):
		self.parent.title("Center Window and Quit Button")
		self.grid(sticky=tk.N+tk.S+tk.W+tk.E)
		self.centerWindow()

	def createWidgets(self):
		frame = tk.Frame(self, relief='raised', borderwidth=1)
		frame.grid(column=0,row=0,columnspan=3,rowspan=3,sticky=tk.N+tk.S+tk.W+tk.E)
		self.quitButton = tk.Button(self,text="Quit", command=self.quit_pressed)
		self.quitButton.grid(column=2,row=3)
		self.okButton = tk.Button(self, text="Ok")
		self.okButton.grid(column=1,row=3)
	def centerWindow(self):
		app_width = 400
		app_height = 250

		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()

		x = (sw - app_width)/2
		y = (sh - app_height)/2
		self.parent.geometry('%dx%d+%d+%d' % (app_width, app_height, x, y))

	def quit_pressed(self):
		self.parent.destroy()


# Main Body
root = tk.Tk()
app = Application(root)
root.mainloop()

