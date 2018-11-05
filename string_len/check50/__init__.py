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
    def test_reject_27(self):
      """rejects a numeric input of 27 """
      self.spawn("./string_len").stdin(27).reject()
		
    @check("compiles")
    def test_reject_4.0(self):
      """rejects a numeric input of 4.0 """
      self.spawn("./string_len").stdin(4.0).reject()
