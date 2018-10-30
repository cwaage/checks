from check50 import *

class Test_Assign(Checks):

	@check()
	def exists(self):
		"""test.c exists"""
		self.require("test.c")

	@check("exists")
	def compiles(self):
		"""test.c compiles"""
		self.spawn("clang -o test test.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_Waage_string(self):
		"""Input of string Waage yields and output of Waage\n"""
		self.spawn("./test").stdin("Waage").stdout("Waage\n").exit(0)
		
	@check("compiles")
	def test_RubberDuck_string(self):
		"""Input of string Rubber Duck yields and output of Rubber Duck\n"""
		self.spawn("./test").stdin("Rubber Duck").stdout("Rubber Duck\n").exit(0)
