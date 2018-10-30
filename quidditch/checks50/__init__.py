from check50 import *

class quidditch(Checks):

	@check()
	def exists(self):
		"""quidditch.c exists"""
		self.require("quidditch.c")

	@check("exists")
	def compiles(self):
		"""quidditch.c compiles"""
		self.spawn("clang -o quidditch quidditch.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_in_five(self):
		"""Input of 5 yields and output of 10\n"""
		self.spawn("./quidditch").stdin("5").stdout("10\n").exit(0)
	
	@check("compiles")
	def test_in_neg_five(self):
		"""Input of 10 yields and output of 15\n"""
		self.spawn("./quidditch").stdin("10").stdout("15\n").exit(0)
