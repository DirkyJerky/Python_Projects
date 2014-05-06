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
			self.answerVar = tk.StringVar()

			self.topframe = tk.LabelFrame(self.parent, text="Pick a number",font='Times 14 bold',borderwidth=3)
			self.midframe = tk.LabelFrame(self.parent, text="Pick a number",font='Times 14 bold',borderwidth=3)
			self.outputframe = tk.LabelFrame(self.parent, text="Product",font='Times 14 bold',fg="red",borderwidth=3)
			

			self.topframe.grid(row=0,column=0,sticky="nw")
			self.midframe.grid(row=1,column=0,sticky="nw")
			self.outputframe.grid(row=3,column=0,sticky="nw")

			self.scale1 = tk.Scale(self.topframe, from_=0, to=100, orient=tk.HORIZONTAL, tickinterval=10,length=360, command=self.setProduct)
			self.scale2 = tk.Scale(self.midframe, from_=0, to=100, orient=tk.HORIZONTAL, tickinterval=10,length=360, command=self.setProduct)
			
			self.output = tk.Label(self.outputframe,textvariable=self.answerVar,font='Times 16 bold',fg="black")
			
			self.output.grid(ipadx=5,sticky='nw')
			self.scale1.grid(ipadx=5,sticky='nw')
			self.scale2.grid(ipadx=5,sticky='nw')

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

		def setProduct(self,val):
			first = self.scale1.get()
			second = self.scale2.get()	    
			product = first * second	    
			ansText = "{0} x {1} = {2}".format(first, second, product)
			self.answerVar.set(ansText)


# Main Body
root = tk.Tk()
app = Application(root)
root.mainloop()