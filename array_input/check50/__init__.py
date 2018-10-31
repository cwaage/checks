from check50 import *

class Array_Input(Checks):

    @check()
    def exists(self):
        """array_input.c exists"""
        self.require("array_input.c")

    @check("exists")
    def compiles(self):
        """array_input.c compiles"""
        self.spawn("clang -o array_input array_input.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_c_100(self):
        """Convert from Celcius True Temp 100 Yields 212.0\n"""
        self.spawn("./array_input").stdin("1").stdin("100").stdout("212.0\n").exit(0)

    @check("compiles")
    def test_f_212(self):
        """Convert from Celcius False Temp 212 Yields 100.0\n"""
        self.spawn("./array_input").stdin("0").stdin("212").stdout("100.0\n").exit(0)

    @check("compiles")
    def test_c_25(self):
            """Convert from Celcius True Temp 25 Yields 77.0\n"""
            self.spawn("./array_input").stdin("1").stdin("25").stdout("77.0\n").exit(0)
