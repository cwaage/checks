from check50 import *

class Binary_Find(Checks):

    @check()
    def exists(self):
        """binaryFind.c exists"""
        self.require("binaryFind.c")
        
    @check("exists")
    def compiles(self):
        """binaryFind.c compiles"""
        self.spawn("clang -o binaryFind binaryFind.c -lcs50 -lm").exit(0)
        
    @check("compiles")
    def test_found_40(self):
        """Finds 40 at index = 6, count = 4"""
        self.spawn("./binaryFind").stdin("40").stdout("6 4").exit(0)
