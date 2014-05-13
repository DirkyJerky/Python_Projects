import Tkinter as tk
import tkMessageBox

from Tkinter import *
 

class ChoiceBox(Entry):
    """ComboBox(parent, itemList=[], *args, kwargs)
       A simple ChoiceBox with checked menu items
       itemList may be a mix of list of strings and lists of tuples of (label, list of strings)
       for one level of sub menu items. *args and kwargs are passed to the Entry widget."""
 
    def __init__(self, parent, itemList=[], *args, **kwargs):
        Entry.__init__(self, parent, *args, **kwargs)
 
        self.pyvar = pyvar = StringVar(self)    # this is the sharing mechanism
        self.config(textvariable=pyvar)         # add the StringVar to self.
 
        self.popup = popup = Menu(self, tearoff=0)
        self.bind("<Button-1>", self.mousedown, add="+")
 
        for item in itemList:
            if type(item) == tuple:
                submenu = self.GetSubMenu(item[0])
                for subitem in item[1]:
                    self.AddCBMenuItem(submenu, subitem)
            else:
                self.AddCBMenuItem(popup, item)
 
    def GetSubMenu(self, label):
        menu = Menu(self, tearoff=0)
        self.popup.add_cascade(menu=menu, label=label)
        return menu
 
    def AddCBMenuItem(self, menu, label):
        menu.add_checkbutton(label=label,
                             command=self.MenuSelect,
                             variable=self.pyvar,   # add the StringVar to a menu.
                             onvalue=label, offvalue='')
 
    def mousedown(self, event):
        x = event.x_root - event.x
        y = event.y_root -  event.y
        self.popup.post(x, y)
        return 'break'
 
    def get(self):
        return self.pyvar.get()
 
    def clear(self):
        self.pyvar.set('')
 
    def MenuSelect(self):
        pass



class Application(tk.Frame):

		def __init__(self, parent = None):
			tk.Frame.__init__(self, parent)
			self.parent = parent
			self.setupUI()
			self.createWidgets()
			

		def setupUI(self):
			self.parent.title("Draw a Shape!")
			#self.parent.grid()
			self.centerWindow()


		def createWidgets(self):
			self.topframe = tk.Frame(self.parent,borderwidth=3)
			self.topframe.grid(row=0,column=0,sticky="nw")
			self.canvas = tk.Canvas(self.topframe,width="500")

			menubar = tk.Menu(self.parent)
			fileMenu = tk.Menu(menubar, tearoff=0)
			fileMenu.add_command(label="Exit", command=self.quitapp)
			fileMenu.add_command(label="Clear All", command=self.clearall)
			menubar.add_cascade(label="File", menu=fileMenu)
			drawmenu = tk.Menu(menubar, tearoff=0)
			drawmenu.add_command(label="Circle", command=self.draw_circle)
			drawmenu.add_command(label="Rectangle", command=self.quitapp)
			menubar.add_cascade(label="Draw", menu=drawmenu)
			self.parent.config(menu=menubar) 
			self.canvas.grid()
		def centerWindow(self):
			app_width = 500
			app_height = 500
			sw = self.parent.winfo_screenwidth()
			sh = self.parent.winfo_screenheight()
			self.x = (sw - app_width)/2
			self.y = (sh - app_height)/2
			self.parent.geometry('%dx%d+%d+%d' % (app_width, app_height, self.x, self.y))

		def quitapp(self):
			self.parent.destroy()
		def clearall(self):
			self.canvas.delete("all")
		def draw_circle(self):
			x = tk.StringVar()
			y = tk.StringVar()
			size = tk.StringVar()
			list_ = ["help","me","luke","!!"]

			x.set(0)
			y.set(0)
			size.set(50)


			self.promt = tk.Toplevel(self.parent)
			self.promt.title('Draw Circle')

			self.promt.mainframe = tk.Frame(self.promt,borderwidth=3)

			self.promt.posLab = tk.Label(self.promt.mainframe,text='Settings:',font='Times 10 bold',fg="black")
			self.promt.xlab = tk.Label(self.promt.mainframe,text="X-Pos (0-500):",font='Times 10 bold',fg="black")
			self.promt.ylab = tk.Label(self.promt.mainframe,text="Y-Pos (0-500):",font='Times 10 bold',fg="black")
			self.promt.xenter = tk.Entry(self.promt.mainframe, textvariable = x, relief='sunken',background='white')
			self.promt.yenter = tk.Entry(self.promt.mainframe, textvariable = y, relief='sunken',background='white')

			self.promt.SizePixel = tk.Label(self.promt.mainframe,text='Size(Pixels):',font='Times 10 bold',fg="black")
			self.promt.size = tk.Entry(self.promt.mainframe, textvariable = size, relief='sunken',background='white')
			self.promt.cb = ChoiceBox(self.promt.mainframe,list_)
			

			self.promt.mainframe.grid(column=0,row=0,sticky="nw")

			self.promt.posLab.grid(column=0,row=0,sticky="nw")
			self.promt.xlab.grid(column=0,row=1)
			self.promt.ylab.grid(column=2,row=1)
			self.promt.xenter.grid(column=1,row=1)
			self.promt.yenter.grid(column=3,row=1)

			self.promt.SizePixel.grid(column=0,row=3,sticky="nw")
			self.promt.size.grid(column=1,row=3)
			self.promt.cb.grid(column=0,row=4,sticky="nw")
			print self.promt.cb.get()
			#Sself.canvas.create_oval(0, 0, 50, 50,)


# Main Body
root = tk.Tk()
app = Application(root)
root.mainloop()