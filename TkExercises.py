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
		self.l1.pack()
		self.l2.pack()
		self.l3.pack()


### Function Definitions ###

### Main body ###
root = tk.Tk()
app = Application(root,"haha")
app.mainloop()