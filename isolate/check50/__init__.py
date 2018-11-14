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
        
    @check("compiles")
    def test_fail_no_args(self):
        """Accepts Strings "Correctly Hands Too Few Arguments"""
        self.spawn("./isolate").stdout("").exit(1)  

    @check("compiles")
    def test_fail_two_many_args(self):
        """Accepts Strings "Correctly Hands Too Many Arguments"""
        self.spawn("./isolate Luke Thian Skylar").stdout("").exit(1) 

    @check("compiles")
    def test_pass_dog_cat(self):
        """Accepts Strings "dog cat"  Yields "D\\n o\\n g\\n C\\n a\\n t\\n" """
        self.spawn("./isolate Dog Cat").stdout("D\n").stdout("o\n").stdout("g\n").stdout("C\n").stdout("a\n").stdout("t\n").exit(0)
