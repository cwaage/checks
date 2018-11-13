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
