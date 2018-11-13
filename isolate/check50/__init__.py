from check50 import *

class Isolate(Checks):

    @check()
    def exists(self):
        """isolate.c exists"""
        self.require("isolate.c")
        
    @check("exists")
    def compiles(self):
        """isolate.c compiles"""
        self.spawn("clang -o isolate isolate.c -lcs50 -lm").exit(0)
        
    @check("compiles")
    def test_pass_amelia(self):
        """Accepts Strings "dog cat"  Yields "d o g c a t" """
        self.spawn("./isolate dog cat").stdout("d\n").stdout("o\n").stdout("g\n").stdout("c\n").stdout("a\n").stdout("t\n").exit(0)
