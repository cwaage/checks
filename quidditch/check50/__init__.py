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
	def test_2_true(self):
		"""Input of 2 Goald and True for Caught Snitch\n"""
		self.spawn("./quidditch").stdin("2").stdin("1").stdout("Your team's final score is: 170\n").exit(0)
	
