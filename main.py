import unittest
from unittest.mock import patch
from io import StringIO


class Greeter:
    @staticmethod
    def greet(name, time=None):
        if time is None:
            time = 0

        trimmed_name = name.strip()
        capitalized_name = trimmed_name.capitalize()

        if 6 <= time < 12:
            greeting = f"Good morning {capitalized_name}"
        elif 18 <= time < 22:
            greeting = f"Good evening {capitalized_name}"
        else:
            greeting = f"Good night {capitalized_name}"

        print(greeting)
        return greeting


class GreeterTest(unittest.TestCase):
    def test_greet_console_logging(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            greeter = Greeter()
            greeter.greet("john")
            output = mock_stdout.getvalue().strip()

        self.assertEqual(output, "Good night John")


if __name__ == '__main__':
    unittest.main()
