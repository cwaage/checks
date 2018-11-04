from check50 import *

class Mean(Checks):

    @check()
    def exists(self):
        """mean.c exists"""
        self.require("mean.c")

    @check("exists")
    def compiles(self):
        """mean.c compiles"""
        self.spawn("clang -o mean mean.c -lcs50 -lm").exit(0)
        	
    @check("compiles")
    def test_reject_tim(self):
	    """rejects a non-numeric input of "Tim" """
	    self.spawn("./mean").stdin("Tim").reject()
		
    @check("compiles")
    def test_reject_parker(self):
	    """rejects a non-numeric input of "Parker" """
	    self.spawn("./mean").stdin("Parker").reject()
		
    @check("compiles")
    def test_pass_5(self):
	    """Accepts Average with values values 5,4,9,27,3 Output 9.60 """
	    self.spawn("./mean").stdin("5").stdin("4").stdin("9").stdin("27").stdin("3").stdout("9.60\n").exit(0)

    @check("compiles")
    def test_pass_5_more(self):
	    """Accepts Average with values values 3,200,99,12,88 Output 80.40 """
	    self.spawn("./mean").stdin("3").stdin("200").stdin("99").stdin("12").stdin("88").stdout("88.40\n").exit(0)
