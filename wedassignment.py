class Player():
	"""Player Class"""
	def __init__(self,playername):
		self.name = playername
		self.health = 100
		self.maxhealth = 100
		self.inventory = Inventory()
	def getitem(self,slot):
		temp = self.inventory.slots.get("Slot"+str(slot), "Empty")
		if temp == "Empty":
			return "Empty"
		return temp[0]
	def getammount(self,slot):
		temp = self.inventory.slots.get("Slot"+str(slot), "Empty")
		if temp == "Empty":
			return "Empty"
		return temp[1]
	def get_item_info(self,slot):
		temp = self.inventory.slots.get("Slot"+str(slot), "Empty")
		if temp == "Empty":
			return "Empty"
		return temp
	def health_change(self,ammount):
		self.health += ammount
		if self.health > self.maxhealth:
			self.health = 100
			print "You have maximum health already"
		if self.health < 0:
			self.health = 0

class Inventory():
	"""Inventory class"""
	def __init__(self):
		self.maxcount = 4
		self.slots = {}
	def additem(self,item,ammount = 1):
		_item_in_inventory = False
		slots = self.slots.keys()
		count = -1
		item_in = ""
		for ob in slots:
			temp = self.slots[ob]
			if len(temp) > 0:
				if temp[0] == item:
					_item_in_inventory = True
					item_in = ob

		if len(self.slots) < self.maxcount or _item_in_inventory == True:
			if _item_in_inventory == False:
				name = "Slot"+str(len(self.slots)+1)
				temp = [item, ammount]
				self.slots[name] = temp
			elif _item_in_inventory == True:
				temp = self.slots[item_in]
				temp2 = [item, temp[1]+ammount]
				self.slots[item_in] = temp2
		else:
			 print "You cannot fit '%s' in your inventory"%(item)

	def print_inventory(self):
		print "You have:"
		slots = self.slots.keys()
		for ob in slots:
			temp = self.slots[ob]
			print ob+": "+str(temp[1])+" "+temp[0]

		
p1 = Player("Ian")
p1.inventory.additem("Stick")
p1.inventory.additem("Log")
p1.inventory.additem("Wood")
p1.inventory.additem("Blood")
print p1.get_item_info(1)
print p1.name
print p1.health
p1.inventory.print_inventory()



