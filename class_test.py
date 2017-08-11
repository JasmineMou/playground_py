class test():
	def __init__(self, a,b):
		self.a = a
		self.b = b


	def set_c(self,c):
		self.c = c

	def get_c(self):
		print(self.c)


t1 = test('A','B')
t1.set_c('C')
t1.get_c()
