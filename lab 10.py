#	Hash	table	with	linear	probing
class	HashTable:
	def	__init__(self,	size):
		self.size	=	size
		self.table	=	[None]	*	size
		
	def	hash_function(self,	key):
		return	key	%	self.size
	
	def	insert(self,	key):
		index	=	self.hash_function(key)
		while	self.table[index]	is	not	None:
			index	=	(index	+	1)	%	self.size
		self.table[index]	=	key
		
	def	search(self,	key):
		index	=	self.hash_function(key)
		start	=	index
		while	self.table[index]	is	not	None:
			if	self.table[index]	==	key:
				return	True
			index	=	(index	+	1)	%	self.size
			if	index	==	start:
				break
		return	False
	
	def	display(self):
		for	i	in	range(self.size):
			print(i,	":",	self.table[i])
			
ht	=	HashTable(7)
keys	=	[50,	21,	58,	17,	15,	49]
for	k	in	keys:
	ht.insert(k)
ht.display()
print("Search	21:",	ht.search(21))
print("Search	99:",	ht.search(99))