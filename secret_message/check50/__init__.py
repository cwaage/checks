from check50 import *

class SecretMessage(Checks):

    @check()
    def exists(self):
      """secret_message.c exists"""
      self.require("secret_message.c")

    @check("exists")
    def compiles(self):
      """secret_message.c compiles"""
      self.spawn("clang -o secret_message secret_message.c -lcs50 -lm").exit(0)
 
    @check("compiles")
    def test_pass_25_values(self):
      """Check Output of the Secret Message: Help me, Obi-Wan Kenobi. You're my only hope!"""
      self.spawn("./secret_message").stdout("Help me, Obi-Wan Kenobi. You're my only hope!").exit(0)
