from check50 import *


class Computer_Average(Checks):

    @check()
    def exists(self):
        """computeAve.c exists"""
        self.require("computeAve.c")

    @check("exists")
    def compiles(self):
        """computeAve.c compiles"""
        self.spawn("clang -std=c11 -o computeAve computeAve.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_fail_no_args(self):
        """Correctly handles no arguments"""
        self.spawn("./computeAve").stdout("").exit(1)
        
    @check("compiles")
    def test_fail_too_manyh_args(self):
        """Correctly handles too many arguments"""
        self.spawn("./computeAve 5 10").stdout("").exit(1)  
        
    @check("compiles")
    def test_pass_5_inputs(self):
        """Correctly handles too many arguments"""
        self.spawn("./computeAve 5").stdin("5.99").stdin("4.50").stdin("200.02").stdin("100.50").stdin("20.02").stdout("Your average deposit is $66.21").exit(1)   
