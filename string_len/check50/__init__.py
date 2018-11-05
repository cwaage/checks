from check50 import *

class String_Len(Checks):

    @check()
    def exists(self):
        """string_len.c exists"""
        self.require("string_len.c")
        
    @check("exists")
    def compiles(self):
        """string_len.c compiles"""
        self.spawn("clang -o string_len string_len.c -lcs50 -lm").exit(0)
        
    @check("compiles")
    def test_reject_Maia(self):
      """rejects a non-numeric input of "Maia" """
      self.spawn("./string_len").stdin("Maia").reject()
		
    @check("compiles")
    def test_reject_Ewan(self):
      """rejects a non-numeric input of "Ewan" """
      self.spawn("./string_len").stdin("Ewan").reject()
