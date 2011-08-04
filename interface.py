import sys, string

#interpreter, homogenises input
class interpreter:
	def __init__(self, richard):
		self.richard = richard
	def read(self):
		self.o=''
		while self.o == '':
			#read in the input, make sure it's ok
			self.i = sys.stdin.readline()
			string.lower(self.i)
			#iterate through the input, while slicing off the \n and extra whitespace
			for a in self.i[:-1].strip():
				if a in string.lowercase:
					self.o = self.o + a
			#all the default actions are here
			if self.o == 'drinkcoffee':
				self.richard.drink_coffee()
				self.o=''
			elif self.o == 'placatecat':
				self.richard.placate_cat()
				self.o=''
			elif self.o == 'checklevels':
				self.richard.check_levels()
				self.o=''
		return self.o
	def reread(self):
		return self.o


