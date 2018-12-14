from check50 import *

class Simple_Insert(Checks):

    @check()
    def exists(self):
        """simpleInsert.c exists"""
        self.require("simpleInsert.c")
        
    @check("exists")
    def compiles(self):
        """simpleInsert.c compiles"""
        self.spawn("clang -o simpleInsert simpleInsert.c -lcs50 -lm").exit(0)
        
    @check("compiles")
    def test_pass_low(self):
        """Adds -7.7 to Array  Yields: -7.70 -3.50 5.60 7.00 8.25 9.67 18.30 """
        self.spawn("./simpleInsert").stdin("-7.7").stdout("-7.70 -3.50 5.60 7.00 8.25 9.67 18.30").exit(0)
