from check50 import *


class Weave(Checks):

    @check()
    def exists(self):
        """weave.c exists"""
        self.require("weave.c")

    @check("exists")
    def compiles(self):
        """weave.c compiles"""
        self.spawn("clang -std=c11 -o weave weave.c -lcs50 -lm").exit(0)

    @check("compiles")
    def test_fail_no_args(self):
        """Correctly handles no arguments"""
        self.spawn("./weave").stdout("").exit(1)
        
    @check("compiles")
    def test_fail_too_manyh_args(self):
        """Correctly handles too many arguments"""
        self.spawn("./weave bob cat jones").stdout("").exit(1)  
    
    @check("compiles")
    def test_pass_cat_dog_inputs(self):
        """Correctly handles \"./weave cat dog\" """
        self.spawn("./weave cat dog").stdout("cot\n").exit(0)
        
    @check("compiles")
    def test_pass_mice_elephants_inputs(self):
        """Correctly handles \"./weave mice elephants\" """
        self.spawn("./weave mice elephants").stdout("mlcp\n").exit(0) 

    @check("compiles")
    def test_pass_spaceship_yeet_inputs(self):
        """Correctly handles \"./weave spaceship yeet\" """
        self.spawn("./weave spaceship yeet").stdout("seat\n").exit(0) 
