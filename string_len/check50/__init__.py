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
    def test_pass_0(self):
        """Accepts String ""  Yields 0\\n """
        self.spawn("./string_len").stdin("").stdout("0\n").exit(0)

    @check("compiles")
    def test_pass_AK(self):
        """Accepts String "Amelia" Yields 6\\n """
        self.spawn("./string_len").stdin("Amelia").stdout("6\n").exit(0)
        
    @check("compiles")
    def test_pass_ewan(self):
        """Accepts String "Ewan" Yields 4\\n """
        self.spawn("./string_len").stdin("Ewan").stdout("4\n").exit(0)

    @check("compiles")
    def test_pass_crazy(self):
        """Accepts String "sdkgbjs+ \/Wz" Yields 13\\n """
        self.spawn("./string_len").stdin("sdkgbjs+ \/Wz").stdout("13\n").exit(0)
