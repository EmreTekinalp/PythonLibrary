"""
@author: Emre Tekinalp
@contact: e.tekinalp@icloud.com
@since: May 28th 2016
@brief: Unit tests on factory pattern module
"""


from src.design_pattern import factory_pattern


def unit_test():
    """Unit test function."""
    factory = factory_pattern.Factory('Oracle')
    connection = factory.create_connection()
    print 'Get the connection to %s.' % connection.description()
# end def unit_test


unit_test()
