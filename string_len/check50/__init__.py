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
    def test_pass_AK(self):
        """Accepts String "Amelia"  Output 6\n """
        self.spawn("./string_len").stdin("Amelia").stdout("6\n").exit(0)
        
    @check("compiles")
    def test_pass_ewan(self):
        """Accepts String "Ewan"  Output 4\n """
        self.spawn("./string_len").stdin("Ewan").stdout("4\n").exit(0)

    @check("compiles")
    def test_pass_crazy(self):
        """Accepts String "sdkgbjs  +\/"  Output 12\n """
        self.spawn("./string_len").stdin("sdkgbjs  \0\n=++").stdout("12\n").exit(0)
