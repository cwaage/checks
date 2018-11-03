from check50 import *

class Fib25(Checks):

    @check()
    def exists(self):
      """fib_25.c exists"""
      self.require("fib_25.c")

    @check("exists")
    def compiles(self):
      """fib_25.c compiles"""
      self.spawn("clang -o fib_25 fib_25.c -lcs50 -lm").exit(0)
 
    @check("compiles")
    def test_pass_25_values(self):
      """Check Output of the First 25 Fibonacci Values"""
      """0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 """
      self.spawn("./fib_25").stdout("0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 ").exit(0)
