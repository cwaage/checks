from check50 import *

class glocal(Checks):

	@check()
	def exists(self):
		"""glocal.c exists"""
		self.require("glocal.c")

	@check("exists")
	def compiles(self):
		"""glocal.c compiles"""
		self.spawn("clang -o glocal glocal.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_in_five(self):
		"""Input of 5 yields and output of 10\n"""
		self.spawn("./glocal").stdin("5").stdout("10\n").exit(0)
	
	@check("compiles")
	def test_in_neg_five(self):
		"""Input of 10 yields and output of 15\n"""
		self.spawn("./glocal").stdin("10").stdout("15\n").exit(0)
	
	# @check("compiles")
    	# def test_reject_negative(self):
        	# """rejects a negative input like -.1"""
        	# self.spawn("./glocal").stdin("-1").reject()
		
	@check("compiles")
    	def test_reject_foo(self):
        	"""rejects a non-numeric input of "foo" """
        	self.spawn("./glocal").stdin("foo").reject()
