from check50 import *

class Array_Input(Checks):
	
	@check()
	def exists(self):
 		"""array_input.c exists"""
  		self.require("array_input.c")

	@check("exists")
  	def compiles(self):
  		"""array_input.c compiles"""
  		self.spawn("clang -o array_input array_input.c -lcs50 -lm").exit(0)
        
	@check("compiles")
	def test_reject_zero(self):
		"""rejects input 0"""
		self.spawn("./array_input").stdin("0").reject()
        
	@check("compiles")
	def test_reject_eleven(self):
		"""rejects input 11"""
		self.spawn("./array_input").stdin("11").reject()
	
	@check("compiles")
	def test_reject_paris(self):
		"""rejects a non-numeric input of "Paris" """
		self.spawn("./array_input").stdin("Paris").reject()
	# @check("compiles")
    	# def test_c_100(self):
       		# """Convert from Celcius True Temp 100 Yields 212.0\n"""
        	# self.spawn("./array_input").stdin("1").stdin("100").stdout("212.0\n").exit(0)
