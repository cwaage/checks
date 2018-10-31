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
