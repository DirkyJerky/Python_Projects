class Player():
	"""Player Class"""
	def __init__(self,playername):
		self.name = playername
		self.health = 100
		self.inventory = Inventory()
class Inventory():
	"""Inventory class"""
	def __init__(self):
		self.maxcount = 10
		self.createdslots = 0
		self.slots = []
	def additem(self):
		



p1.inventory.slots[0]

p1.getitem(0)