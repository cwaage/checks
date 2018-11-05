from check50 import *

class Swap_Vals(Checks):

	@check()
	def exists(self):
		"""swap_values.c exists"""
		self.require("swap_values.c")

	@check("exists")
	def compiles(self):
		"""swap_values.c compiles"""
		self.spawn("clang -o swap_values swap_values.c -lcs50 -lm").exit(0)
        
	@check("compiles")
	def test_reject_zero(self):
		"""rejects an input of 0"""
		self.spawn("./swap_values").stdin("0").reject()
	
	@check("compiles")
	def test_reject_daniel(self):
		"""rejects a non-numeric input of "Daniel" """
		self.spawn("./swap_values").stdin("Daniel").reject()
		
    #@check("compiles")
    #def test_reject_zoe(self):
	    #"""rejects a non-numeric input of "Maya" """
	    #self.spawn("./swap_values").stdin("Maya").reject()
        
    #@check("compiles")
    #def test_fail_2(self):
	    #"""Reject Array Size 2 """
	    #self.spawn("./swap_values").stdin("2").reject(0)
        
    #@check("compiles")
    #def test_fail_12(self):
	    #"""Reject Array Size 12 """
	    #self.spawn("./swap_values").stdin("12").reject(0)
        
    #@check("compiles")
    #def test_pass_3(self):
	    #"""Accepts Array Size 4 && values 2 , 9 , 20 , 50 | Output 9 2 50 20 """
	    #self.spawn("./swap_values").stdin("2").stdin("9").stdin("20").stdin("50").stdout("9 2 50 20 ").exit(0)
		
    #@check("compiles")
    #def test_pass_5(self):
	    #"""Accepts Array Size 5 && values 99 , -1 , 42 , 150, 500 | Output -1 99 150 42 500 """
	    #self.spawn("./swap_values").stdin("5").stdin("99").stdin("-1").stdin("42").stdin("150").stdin("500").stdout("-1 99 150 42 500 ").exit(0)
