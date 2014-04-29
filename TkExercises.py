##################################
# Ian Roth
#
#  TkExercises.py
#
#  Exercises
###################################

### Module imports ###
import Tkinter as tk
###  Global Variables  ###

### Classes ###
class Application(tk.Frame):
	"""Main App class"""
	def __init__(self, parent = None,title = ""):
		tk.Frame.__init__(self,parent)
		self.parent = parent
		self.pack()
		self.parent.title(title)
		self.parent.maxsize(500,500)
		self.parent.minsize(500,500)
		#self.parent.geometry("%dx%d+%d+%d"%(256,256,self.parent.screenwidth,0))
		self.createWigits()
	def createWigits(self):
		self.l1 = tk.Label(self,text="Red Sun",bg="red",fg="white")
		self.l2 = tk.Label(self,text="Green Grass",bg="green")
		self.l3 = tk.Label(self,text="Blue Sky",bg="blue",fg="white")
		self.l4 = tk.Label(self,text="Red",bg="red",fg="white")
		self.l5 = tk.Label(self,text="Green",bg="green")
		self.l6 = tk.Label(self,text="Blue",bg="blue",fg="white")
		self.l1.grid(column=0,row=0,sticky="NSEW")
		self.l2.grid(column=0,row=1,sticky="NSEW")
		self.l3.grid(column=0,row=2,sticky="NSEW")
		self.l4.grid(column=2,row=4,sticky="",padx=5)
		self.l5.grid(column=3,row=4,sticky="",padx=5)
		self.l6.grid(column=4,row=4,sticky="",padx=5)


### Function Definitions ###

### Main body ###
root = tk.Tk()
app = Application(root,"all?")
app.mainloop()