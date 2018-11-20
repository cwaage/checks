from check50 import *

class last_index(Checks):

    @check()
    def exists(self):
        """lastIndex.c exists"""
        self.require("lastIndex.c")
        
    @check("exists")
    def compiles(self):
        """lastIndex.c compiles"""
        self.spawn("clang -o lastIndex lastIndex.c -lcs50 -lm").exit(0)
   
    @check("compiles")
    def test_fail_no_args(self):
        """Accepts Strings Correctly Handles Too Few Arguments"""
        self.spawn("./lastIndex").stdout("").exit(1) 
        
    @check("compiles")
    def test_fail_too_many_args(self):
        """Accepts Strings Correctly Handles Too Many Arguments"""
        self.spawn("./lastIndex e Met").stdout("").exit(1) 
    
    @check("compiles")
    def test_pass_End_match_case(self):
        """Accepts Strings Correctly Handles Target \'T\' in String \"Thian\" """
        self.spawn("./lastIndex T").stdin("Thian").stdout("0").exit(0)
        
    @check("compiles")
    def test_pass_Middle_match_case(self):
        """Accepts Strings Correctly Handles Target \'k\' in String \"Heikkinen\" """
        self.spawn("./lastIndex k").stdin("Heikkinen").stdout("4").exit(0)
        
    @check("compiles")
    def test_pass_End_match_case(self):
        """Accepts Strings Correctly Handles Target \'o\' in String \"Dalusio\" """
        self.spawn("./lastIndex o").stdin("Dalusio").stdout("6").exit(0)
