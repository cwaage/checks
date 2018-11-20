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
    def test_pass_Begining_match_case(self):
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
        
    @check("compiles")
    def test_pass_Begining_Not_case(self):
        """Accepts Strings Correctly Handles Target \'t\' in String \"Thanksgiving\" """
        self.spawn("./lastIndex t").stdin("Thanksgiving").stdout("0").exit(0)
        
    @check("compiles")
    def test_pass_Middle_Not_case(self):
        """Accepts Strings Correctly Handles Target \'M\' in String \"Pumpkin\" """
        self.spawn("./lastIndex M").stdin("Pumpkin").stdout("2").exit(0)
        
    @check("compiles")
    def test_pass_End_Not_case(self):
        """Accepts Strings Correctly Handles Target \'G\' in String \"Stuffing\" """
        self.spawn("./lastIndex G").stdin("Stuffing").stdout("7").exit(0)
  
    @check("compiles")
    def test_pass_Not_Found(self):
        """Accepts Strings Correctly Handles Target \'z\' in String \"Lewis-Shunk\" """
        self.spawn("./lastIndex z").stdin("Lewis-Shunk").stdout("-1").exit(0)
        
    @check("compiles")
    def test_pass_Not_Found(self):
        """Accepts Strings Correctly Handles Target \'$\' in String \"Jenson\" """
        self.spawn("./lastIndex $").stdin("Jenson").stdout("-1").exit(0)
