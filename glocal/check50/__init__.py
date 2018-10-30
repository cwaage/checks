from check50 import *

class Test_Assign(Checks):

	@check()
	def exists(self):
		"""glocal.c exists"""
		self.require("glocal.c")

	@check("exists")
	def compiles(self):
		"""glocal.c compiles"""
		self.spawn("clang -o test glocal.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_in_five(self):
		"""Input of 5 yields and output of 10\n"""
		self.spawn("./test").stdin("5").stdout("10\n").exit(0)
	
	@check("compiles")
	def test_in_neg_five(self):
		"""Input of -5 yields and output of 0\n"""
		self.spawn("./test").stdin("-5").stdout("0\n").exit(0)
