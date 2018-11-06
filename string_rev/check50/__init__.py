from check50 import *

class String_Rev(Checks):

    @check()
    def exists(self):
        """string_rev.c exists"""
        self.require("string_rev.c")
        
    @check("exists")
    def compiles(self):
        """string_rev.c compiles"""
        self.spawn("clang -o string_rev string_rev.c -lcs50 -lm").exit(0)
        
    @check("compiles")
    def test_pass_gub(self):
        """Accepts String "bug"  Yields gub """
        self.spawn("./string_rev").stdin("bug").stdout("gub").exit(0)
