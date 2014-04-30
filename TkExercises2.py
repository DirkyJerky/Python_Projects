import Tkinter as tk

class Application(tk.Frame):

		def __init__(self, parent = None):
			tk.Frame.__init__(self, parent)
			self.parent = parent
			self.setupUI()
			self.createWidgets()

		def setupUI(self):
			self.parent.title("Checkout the checkbox")
			#self.parent.grid()
			self.centerWindow()


		def createWidgets(self):
			self.emptyframe =tk.Frame(self.parent)
			self.emptyframe.grid(row=0,column=0)
			self.buttonFrame = tk.Frame(self.parent)
			self.buttonFrame.grid(row=1,column=0,sticky="e")

			self.ok = tk.Button(self.buttonFrame,text="Ok")
			self.quit = tk.Button(self.buttonFrame,text="Quit",command=self.quitapp)
			self.ok.grid(row=0,column=0, sticky="e")
			self.quit.grid(row=0,column=1, sticky="e")
			self.parent.grid_columnconfigure(0,weight=1)
			self.parent.grid_rowconfigure(0,weight=1)
		def centerWindow(self):
			app_width = 400
			app_height = 250

			sw = self.parent.winfo_screenwidth()
			sh = self.parent.winfo_screenheight()

			x = (sw - app_width)/2
			y = (sh - app_height)/2
			self.parent.geometry('%dx%d+%d+%d' % (app_width, app_height, x, y))

		def quitapp(self):
			self.parent.destroy()


# Main Body
root = tk.Tk()
app = Application(root)
root.mainloop()

