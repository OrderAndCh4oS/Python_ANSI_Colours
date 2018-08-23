import unittest

from ansi_colours import AnsiColours as colour


class TestAnsiColours(unittest.TestCase):

    def test_methods(self):
        self.assertEqual(colour.black("black"), "\033[0;30mblack\033[0m")
        self.assertEqual(colour.blue("blue"), "\033[0;34mblue\033[0m")
        self.assertEqual(colour.cyan("cyan"), "\033[0;36mcyan\033[0m")
        self.assertEqual(colour.green("green"), "\033[0;32mgreen\033[0m")
        self.assertEqual(colour.red("red"), "\033[0;31mred\033[0m")
        self.assertEqual(colour.purple("purple"), "\033[0;35mpurple\033[0m")
        self.assertEqual(colour.yellow("yellow"), "\033[0;33myellow\033[0m")
        self.assertEqual(colour.light_grey("light_grey"), "\033[0;37mlight_grey\033[0m")


if __name__ == '__main__':
    unittest.main()
