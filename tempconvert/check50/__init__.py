from check50 import *

class Temp_Convert(Checks):

	@check()
	def exists(self):
		"""temp_convert.c exists"""
		self.require("temp_convert.c")

	@check("exists")
	def compiles(self):
		"""temp_convert.c compiles"""
		self.spawn("clang -o temp_convert temp_convert.c -lcs50 -lm").exit(0)

	# @check("compiles")
	# def test_c_100(self):
		# """Convert from Celcius True Temp 100 Yields 212.0\n"""
		# self.spawn("./temp_convert").stdin("1").stdin("100").stdout("212.0\n").exit(0) 
	
  	# @check("compiles")
	# def test_f_212(self):
		# """Convert from Celcius False Temp 212 Yields 100.0\n"""
		# self.spawn("./temp_convert").stdin("0").stdin("212").stdout("100.0\n").exit(0)
    
    	# @check("compiles")
    	# def test_c_25(self):
      		# """Convert from Celcius True Temp 100 Yields 212.0\n"""
      		# self.spawn("./temp_convert").stdin("1").stdin("25").stdout("77.0\n").exit(0)
