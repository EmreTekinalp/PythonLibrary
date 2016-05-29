"""
@author: Emre Tekinalp
@contact: e.tekinalp@icloud.com
@since: May 28th 2016
@brief: Example of the strategy pattern.

        Unit tests to be found under:
        test/unit/test_strategy_pattern.py
"""


from abc import abstractmethod


class Language(object):

    """Language Base class."""

    @abstractmethod
    def speak(self):
        """Abstract speak function which needs to be overriden by subclass."""
        pass
    # end def speak
# end class Language


class English(Language):

    """English class subclassing Language class."""

    def speak(self):
        """Speak function printing spoken language."""
        print 'I speak english'
    # end def speak
# end class English


class German(Language):

    """German class subclassing Language class."""

    def speak(self):
        """Speak function printing spoken language."""
        print 'I speak german'
    # end def speak
# end class German


class French(Language):

    """French class subclassing Language class."""

    def speak(self):
        """Speak function printing spoken language."""
        print 'I speak french'
    # end def speak
# end class French


class Chinese(Language):

    """Chinese class subclassing Language class."""

    def speak(self):
        """Speak function printing spoken language."""
        print 'I speak chinese'
    # end def speak
# end class Chinese


class Person(object):

    """Base class of a person object."""

    def __init__(self):
        """Initialize Person class."""
        # private vars
        self._language = Language()
    # end def __init__       

    def set_language(self, language):
        """Setter function to set the private language object."""
        self._language = language
    # end def set_language

    @abstractmethod
    def speak(self):
        """Speak function calling speak method of private language object."""
        self._language.speak()
    # end def speak

    def __repr__(self):
        """Override builtin repr function to return class name."""
        return '\n%s:' % self.__class__.__name__
    # end def __repr__
# end class Person


class Student(Person):

    """Student class."""

    def __init__(self):
        """Initialize Student class."""
        self.set_language(English())
    # end def __init__
# end class Student


class Teacher(Person):

    """Teacher class."""

    def __init__(self):
        """Initialize Teacher class."""
        self.set_language(German())
    # end def __init__
# end class Teacher


class Doctor(Person):

    """Doctor class."""

    def __init__(self):
        """Initialize Doctor class."""
        self.set_language(French())
    # end def __init__
# end class Doctor


class Professor(Person):

    """Professor class."""

    def __init__(self):
        """Initialize Professor class."""
        self.set_language(Chinese())
    # end def __init__
# end class Professor
