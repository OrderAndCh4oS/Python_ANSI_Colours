
from ansi_colours import AnsiColours


def test_methods():
    assert AnsiColours.black("black") == "\033[0;30mblack\033[0m"
    assert AnsiColours.blue("blue") == "\033[0;34mblue\033[0m"
    assert AnsiColours.cyan("cyan") == "\033[0;36mcyan\033[0m"
    assert AnsiColours.green("green") == "\033[0;32mgreen\033[0m"
    assert AnsiColours.red("red") == "\033[0;31mred\033[0m"
    assert AnsiColours.purple("purple") == "\033[0;35mpurple\033[0m"
    assert AnsiColours.yellow("yellow") == "\033[0;33myellow\033[0m"
    assert AnsiColours.light_grey("light_grey") == "\033[0;37mlight_grey\033[0m"
