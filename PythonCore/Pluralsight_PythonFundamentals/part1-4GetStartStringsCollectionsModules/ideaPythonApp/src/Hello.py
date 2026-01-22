import math
import sys
import random

class Hello:
    def demo(self):
        d = 10
        print(math.pow(d, d))

    def sayHell(self, a):
        try:
            print("Hello", str(a * a))
        except TypeError as e:
            print(f"Error: {e}", file=sys.stderr)

    def sayGoodMorningInPolish(self, name=None):
        """Prints good morning in Polish.

        Args:
            name (str, optional): Person's name. Defaults to None.
        """
        """Prints good morning in Polish."""
        print("Dzień dobry, {}!".format(name))

    def generateRandomNumbers(self, count=10):
        """Generate random numbers.

        Args:
            count (int, optional): Number of random numbers to generate. Defaults to 10.
        """
        for _ in range(count):
            print(random.randint(0, 100))

# Create an instance and call methods
if __name__ == "__main__":
    hello = Hello()
    hello.demo()
    hello.sayHell(212)
    hello.sayGoodMorningInPolish("Jan")
    hello.generateRandomNumbers()
