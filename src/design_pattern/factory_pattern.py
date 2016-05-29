"""
@author: Emre Tekinalp
@contact: e.tekinalp@icloud.com
@since: May 28th 2016
@brief: Example of the factory pattern.

        Unit tests to be found under:
        test/unit/test_factory_pattern.py
"""


from abc import abstractmethod


class Connection(object):

    """Connection class."""

    @abstractmethod
    def description(self):
        """description function which needs to be overriden by the subclass."""
        pass    
    # end def description
# end class Connection


class OracleConnection(Connection):

    """OracleConnection class."""

    def description(self):
        """description function."""
        return 'Oracle'
    # end def description
# end class OracleConnection


class SqlServerConnection(Connection):

    """SqlServerConnection class."""

    def description(self):
        """description function."""
        return 'SQL Server'
    # end def description
# end class SqlServerConnection


class MySqlConnection(Connection):

    """MySqlConnection class."""

    def description(self):
        """description function."""
        return "MySQL"
    # end def description
# end class MySqlConnection


class Factory(object):

    """Factory base class."""

    def __init__(self, object_type):
        """Initialize Computer class."""
        self._object_type = object_type
    # end def __init__

    def create_connection(self):
        """create connection function."""
        if self._object_type == 'Oracle':
            return OracleConnection()
        elif self._object_type == 'SQL Server':
            return SqlServerConnection()
        elif self._object_type == 'MySQL':
            return MySqlConnection()
        else:
            return Connection()
        # end if return connection objects
    # end def create_connection
# end class Computer
