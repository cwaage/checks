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
        """rejects a input 0"""
        self.spawn("./array_input").stdin("0").reject()
		

    @check("compiles")
    def test_reject_paris(self):
	    """rejects a non-numeric input of "Paris" """
	    self.spawn("./array_input").stdin("Paris").reject()
		
	@check("compiles")
	def test_in_four(self):
		"""Input of 4 yields and {5,6,7,8} output of 5 6 7 8 """
		self.spawn("./array_input").stdin("4").stdin("5").stdin("6").stdin("7").stdin("8").stdout("5 6 7 8 ").exit(0)
