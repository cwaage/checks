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
    def test_pass_3(self):
        """Accepts String "Amelia Output 6\n """
        self.spawn("./array_input").stdin("Amelia").stdout("6\n").exit(0)
