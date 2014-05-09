import Tkinter as tk
import tkMessageBox

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
			x = (sw - app_width)/2
			y = (sh - app_height)/2
			self.parent.geometry('%dx%d+%d+%d' % (app_width, app_height, x, y))

		def quitapp(self):
			self.parent.destroy()
		def clearall(self):
			self.canvas.delete("all")
		def draw_circle(self):
			promt = tk.Toplevel(self.parent)
			promt.title('Draw Circle')


# Main Body
root = tk.Tk()
app = Application(root)
root.mainloop()