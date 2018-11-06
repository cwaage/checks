from check50 import *

class Flip_String(Checks):

    @check()
    def exists(self):
        """flip_string.c exists"""
        self.require("flip_string.c")
        
    @check("exists")
    def compiles(self):
        """flip_string.c compiles"""
        self.spawn("clang -o flip_string flip_string.c -lcs50 -lm").exit(0)
        
    # @check("compiles")
    # def test_pass_amelia(self):
        # """Accepts String "amelia"  Yields "AmElIa" """
        # self.spawn("./flip_string").stdin("amelia").stdout("AmElIa").exit(0)
        
    # @check("compiles")
    # def test_pass_Skylar(self):
        # """Accepts String "sKYLAR"  Yields "SkYlAr" """
        # self.spawn("./flip_string").stdin("sKYLAR").stdout("SkYlAr").exit(0)
        
    # @check("compiles")
    # def test_pass_Kat(self):
        # """Accepts String "KATaya"  Yields "kAtAyA" """
        # self.spawn("./flip_string").stdin("KATaya").stdout("kAtAyA").exit(0)
