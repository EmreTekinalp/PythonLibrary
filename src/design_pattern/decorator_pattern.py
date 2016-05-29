"""
@author: Emre Tekinalp
@contact: e.tekinalp@icloud.com
@since: May 28th 2016
@brief: Example of the decorator pattern.

        Unit tests to be found under:
        test/unit/test_decorator_pattern.py
"""


from abc import abstractmethod


class Computer(object):

    """Computer base class which is existing code in this example.

    And with the usage of the Decorator class the goal is to wrap the
    extensions around this class.

    Golden rule here:
    Encapsulate code for modifications and keep it open for extensions.
    """

    def __init__(self):
        """Initialize Computer class."""
        pass
    # end def __init__

    def description(self):
        """Public function returning a description."""
        return 'computer'
    # end def description
# end class Computer


class Decorator(Computer):

    """Decorator class subclassing from computer working as a wrapper."""

    @abstractmethod
    def description(self):
        """Abstract public function which needs to be overriden by subclass."""
        pass
    # end def description
# end class Decorator


class Disk(Decorator):

    """Disk class."""

    def __init__(self, component):
        """Initialize Disk class."""
        self.component = component 
    # end def __init__

    def description(self):
        """Public function returning a description."""
        return '%s and a disk' % self.component.description()
    # end def description
# end class Disk


class Monitor(Decorator):

    """Monitor class."""

    def __init__(self, component):
        """Initialize Monitor class."""
        self.component = component 
    # end def __init__

    def description(self):
        """Public function returning a description."""
        return '%s and a monitor' % self.component.description()
    # end def description
# end class Monitor


class CompactDisc(Decorator):

    """CompactDisc class."""

    def __init__(self, component):
        """Initialize CompactDisc class."""
        self.component = component 
    # end def __init__

    def description(self):
        """Public function returning a description."""
        return '%s and a CD' % self.component.description()
    # end def description
# end class CompactDisc
