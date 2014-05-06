import Tkinter as tk

class Application(tk.Frame):

		def __init__(self, parent = None):
			tk.Frame.__init__(self, parent)
			self.parent = parent
			self.setupUI()
			self.createWidgets()
			

		def setupUI(self):
			self.parent.title("")
			#self.parent.grid()
			self.centerWindow()


		def createWidgets(self):
			self.Name = tk.StringVar()
			self.Adress = tk.StringVar()
			self.Phone = tk.StringVar()
			self.displaytext = tk.StringVar()

			self.topframe = tk.Frame(self.parent,borderwidth=3)
			self.midframe = tk.Frame(self.parent,borderwidth=3)
			
			self.topframe.grid(row=0,column=0,sticky="nw")
			self.midframe.grid(row=1,column=0,sticky="nw")

			self.NameLb = tk.Label(self.topframe,text="Name ",font='Times 14',fg="black")
			self.AdressLb = tk.Label(self.topframe,text="Adress ",font='Times 14',fg="black")
			self.PhoneLb = tk.Label(self.topframe,text="Phone ",font='Times 14',fg="black")

			self.displayBtn = tk.Button(self.topframe, text="Show Info", font="Times 10",command=self.showInfo)
			self.clearBtn = tk.Button(self.topframe, text="Clear Info", font="Times 10",command=self.clearInfo)

			self.text= tk.Label(self.midframe,textvariable= self.displaytext,font="Times 10")


			self.nameEntry = tk.Entry(self.topframe, textvariable = self.Name, relief='sunken',background='white')
			self.adressEntry = tk.Entry(self.topframe, textvariable = self.Adress, relief='sunken',background='white')
			self.phoneEntry = tk.Entry(self.topframe, textvariable = self.Phone, relief='sunken',background='white')

			self.text.grid()

			self.displayBtn.grid(column=1,columnspan=2,row=3)
			self.clearBtn.grid(column=3,columnspan=2,row=3)

			
			self.nameEntry.grid(column=1,row=0,columnspan=4)
			self.NameLb.grid(column=0,row=0)

			self.adressEntry.grid(column=1,row=1,columnspan=4)
			self.AdressLb.grid(column=0,row=1)

			self.phoneEntry.grid(column=1,row=2,columnspan=4)
			self.PhoneLb.grid(column=0,row=2)

			
		def showInfo(self):
			name = self.nameEntry.get()
			adress = self.adressEntry.get()
			phone = self.phoneEntry.get()
			Dis = "You entered '"+name+" , "+adress+" , "+phone
			if len(name) > 0 or len(adress) > 0 or len(phone) > 0:
				self.displaytext.set(Dis)
		def clearInfo(self):
			self.displaytext.set("")
			self.Name.set("")
			self.Adress.set("")
			self.Phone.set("")
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