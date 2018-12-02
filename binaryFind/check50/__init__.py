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
        
    @check("compiles")
    def test_found_22(self):
        """Finds 22 at index = 4, count = 4"""
        self.spawn("./binaryFind").stdin("22").stdout("4 4").exit(0) 
        
    @check("compiles")
    def test_found_7(self):
        """Finds 7 at index = 2, count = 4"""
        self.spawn("./binaryFind").stdin("7").stdout("2 4").exit(0) 

    @check("compiles")
    def test_found_49(self):
        """Finds 49 at index = 9, count = 3"""
        self.spawn("./binaryFind").stdin("49").stdout("9 3").exit(0)

    @check("compiles")
    def test_found_65(self):
        """Finds 65 at index = 13, count = 3"""
        self.spawn("./binaryFind").stdin("65").stdout("13 3").exit(0) 

    @check("compiles")
    def test_found_2(self):
        """Finds 2 at index = 0, count = 4"""
        self.spawn("./binaryFind").stdin("2").stdout("0 4").exit(0)
        
    @check("compiles")
    def test_notfound_neg2(self):
        """Does Not Find -2 prints -1, count = 4"""
        self.spawn("./binaryFind").stdin("-2").stdout("-1 4").exit(0) 
        
    @check("compiles")
    def test_notfound_75(self):
        """Does Not Find 75 prints -1, count = 4"""
        self.spawn("./binaryFind").stdin("75").stdout("-1 4").exit(0) 

