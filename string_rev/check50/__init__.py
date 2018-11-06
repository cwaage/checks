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
        """Accepts String "bug"  Yields "gub" """
        self.spawn("./string_rev").stdin("bug").stdout("gub").exit(0)
        
    @check("compiles")
    def test_pass_CSP(self):
        """Accepts String "!PSC PA evol I"  Yields "I love AP CSP!" """
        self.spawn("./string_rev").stdin("!PSC PA evol I").stdout("I love AP CSP!").exit(0)
        
    @check("compiles")
    def test_pass_OBG(self):
        """Accepts String "aivilO"  Yields "Olivia" """
        self.spawn("./string_rev").stdin("aivilO").stdout("Olivia").exit(0)

    @check("compiles")
    def test_pass_Ewan(self):
        """Accepts String "nawE"  Yields "Ewan" """
        self.spawn("./string_rev").stdin("nawE").stdout("Ewan").exit(0)
