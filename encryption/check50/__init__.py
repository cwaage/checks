from check50 import *

class Encryption(Checks):

	@check()
	def exists(self):
		"""encryption.c exists """
		self.require("encryption.c")

	@check("exists")
	def compiles(self):
		"""encryption.c compiles"""
		self.spawn("clang -o encryption encryption.c -lcs50 -lm").exit(0)
		
	@check("compiles")
	def test_175_114(self):
		"""Test 175 and 114 Yields Success\n"""
		self.spawn("./encryption").stdin("175").stdin("114").stdout("Success\n").exit(0)

	@check("compiles")
	def test_140_475(self):
		"""Test 140 and 475 Yields Success\n"""
		self.spawn("./encryption").stdin("140").stdin("475").stdout("Success\n").exit(0)
		
	@check("compiles")
	def test_84_475(self):
		"""Test 84 and  Yields Success\n"""
		self.spawn("./encryption").stdin("84").stdin("475").stdout("Failed\n").exit(0)	
