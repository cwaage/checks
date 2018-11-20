from check50 import *

class last_index(Checks):

    @check()
    def exists(self):
        """lastIndex.c exists"""
        self.require("lastIndex.c")
        
    @check("exists")
    def compiles(self):
        """lastIndex.c compiles"""
        self.spawn("clang -o lastIndex lastIndex.c -lcs50 -lm").exit(0)
