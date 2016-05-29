"""
@author: Emre Tekinalp
@contact: e.tekinalp@icloud.com
@since: May 28th 2016
@brief: Unit tests on decorator pattern module
"""


from src.design_pattern import decorator_pattern


def unit_test():
    """Unit Test function for Decoratpr design pattern."""
    computer = decorator_pattern.Computer()
    computer = decorator_pattern.Disk(computer)
    computer = decorator_pattern.Monitor(computer)
    computer = decorator_pattern.CompactDisc(computer)

    print 'I take my %s with me.' % computer.description()
# end def unit_test


unit_test()
