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
	def test_41_cents(self):
		"""Input of string Waage yields and output of Waage\n"""
		self.spawn("./test").stdin("Waage").stdout("Waage\n").exit(0)
