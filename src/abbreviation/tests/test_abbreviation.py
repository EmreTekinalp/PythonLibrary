"""
@package: tests.test_abbreviation
@brief: Unit test for abbreviation algorithm
@author: Emre Tekinalp
@contact: e.tekinalp@icloud.com
@data: Oct 31st, 2016
"""

__version__ = '0.1.0'
__author__ = 'Emre Tekinalp'
__docformat__ = 'reStructuredText'

# python
import os
import json
import logging
import string
import unittest

# third party modules
from abbreviation import abbreviation

FORMAT = '\n%(levelname)s: line %(lineno)s in %(filename)s -> %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)


class TestAbbreviation(unittest.TestCase):
    """Unit test case for Abbreviation class."""

    def setUp(self):
        print('%s setUp()' % self.__class__.__name__)

    def tearDown(self):
        print('%s tearDown()' % self.__class__.__name__)

    def test_abbreviate_on_maya_nodes_data(self):
        """Test abbreviate method using maya_nodes.json file."""
        print('\nTesting abbreviate on maya_nodes.json...')
        # get data
        file_name = 'maya_nodes.json'
        data_path = os.path.join(__file__, os.pardir, os.pardir, 'data')
        file_path = os.path.join(os.path.abspath(data_path), file_name)
        with open(file_path) as json_data:
            data = json.load(json_data)
        # end with get data from file

        a = abbreviation.Abbreviation()
        for n in range(3, 6):
            print('Testing with length = %s:' % n)
            print('maya nodes >>>', len(data))
            self.assertRaises(Exception, a.abbreviate(data, n))
            print('OK')
        # end for linear O(n) iterating length of abbr, ranging from 1 to 10
    # end def test_abbreviate_on_maya_nodes_data

    def test_abbreviate_on_countries_data(self):
        """Test abbreviate method using countries.json file."""
        print('\nTesting abbreviate on countries.json...')
        # get data
        file_name = 'countries.json'
        data_path = os.path.join(__file__, os.pardir, os.pardir, 'data')
        file_path = os.path.join(os.path.abspath(data_path), file_name)
        with open(file_path) as json_data:
            data = json.load(json_data)
        # end with get data from file

        a = abbreviation.Abbreviation()
        print('DATA LENGTH:', len(data))
        for n in range(1, 11):
            print('Testing with length = %s:' % n)
            self.assertRaises(Exception, a.abbreviate(data, n))
            print('OK')
        # end for linear O(n) iterating length of abbr, ranging from 1 to 10
    # end def test_abbreviate_on_countries_data

    def test_abbreviate_on_arbitrary_data(self):
        """Test abbreviate method on arbitrary data."""
        print('\nTesting abbreviate on arbitrary data...')
        # get data
        data = [0, 12, 3, ' ', list(), dict(), '123', '7%5',
                'W0rds4u', 'T3st', 'Hel&&&loW0()rlD']
        data += [s for s in string.punctuation]
        data += [{'Word': 123, 'Foobar': 'Germany', 123: 'working'}]

        a = abbreviation.Abbreviation()
        for n in range(1, 4):
            print('Testing with length = %s:' % n)
            self.assertRaises(Exception, a.abbreviate(data, n))
            print('OK')
        # end for linear O(n) iterating length of abbr, ranging from 1 to 4

        data = {'Word': 123, 'Foobar': 'Germany', 123: 'working'}
        print('Testing with dictionary as data and length = 3:')
        self.assertRaises(Exception, a.abbreviate(data, 3))
        print('OK')
    # end def test_abbreviate_on_arbitrary_data

    @unittest.expectedFailure
    def test_abbreviate_on_zero_length(self):
        """Test abbreviate method on inputs causing errors."""
        print('\nTesting abbreviate on zero length...')
        a = abbreviation.Abbreviation()
        self.assertRaises(Exception, a.abbreviate([], -1))
    # end def test_abbreviate_on_zero_length

    @unittest.expectedFailure
    def test_abbreviate_on_negative_length(self):
        """Test abbreviate method on inputs causing errors."""
        print('\nTesting abbreviate on negative length...')
        a = abbreviation.Abbreviation()
        print('Expecting to fail, test is OK')
        self.assertRaises(Exception, a.abbreviate([], -2))
    # end def test_abbreviate_on_negative_length

    @unittest.expectedFailure
    def test_abbreviate_on_wrong_data_type(self):
        """Test abbreviate method on wrong data type."""
        print('\nTesting abbreviate on wrong data type...')
        a = abbreviation.Abbreviation()
        print('Expecting to fail, test is OK')
        self.assertRaises(Exception, a.abbreviate('asd', 2))
    # end def test_abbreviate_on_wrong_data_type

    def test_abbreviate_on_valid_case(self):
        """Test abbreviate method on case mode."""
        print('\nTesting abbreviate on valid case mode...')
        # get data
        file_name = 'maya_nodes.json'
        data_path = os.path.join(__file__, os.pardir, os.pardir, 'data')
        file_path = os.path.join(os.path.abspath(data_path), file_name)
        with open(file_path) as json_data:
            data = json.load(json_data)
        # end with get data from file

        a = abbreviation.Abbreviation()
        for case in [0, 1, 2, 3, abbreviation.UPPER, abbreviation.LOWER,
                     abbreviation.CAPITALIZE, abbreviation.NEUTRAL]:
            print('Testing with case = %s:' % case)
            self.assertRaises(Exception, a.abbreviate(data, 3, case))
            print('OK')
        # end for iterate constant case variables and numerical values
    # end def test_abbreviate_on_valid_case

    @unittest.expectedFailure
    def test_abbreviate_on_invalid_case(self):
        """Test abbreviate method on invalid case mode."""
        print('\nTesting abbreviate on invalid case mode...')
        a = abbreviation.Abbreviation()
        print('Testing with case = -1')
        print('Expecting to fail, test is OK')
        self.assertRaises(Exception, a.abbreviate([], 1, -1))
    # end def test_abbreviate_on_invalid_case

    def test_abbreviate_on_maya_nodes_exclude_characters(self):
        """Test abbreviate method on maya nodes including special characters"""
        print('\nTesting abbreviate on maya nodes including special chars...')
        # get data
        file_name = 'maya_nodes.json'
        data_path = os.path.join(__file__, os.pardir, os.pardir, 'data')
        file_path = os.path.join(os.path.abspath(data_path), file_name)
        with open(file_path) as json_data:
            data = json.load(json_data)
        # end with get data from file

        excludes = ['_', '#', '.', 'a', 'E', 'o', 'nim']
        a = abbreviation.Abbreviation(exclude_characters=excludes)
        self.assertRaises(Exception, a.abbreviate(data, 2))
    # end def test_abbreviate_on_maya_nodes_exclude_characters

    @unittest.expectedFailure
    def test_abbreviate_on_arbitrary_data_exclude_characters(self):
        """Test abbreviate method on arbitrary data."""
        print('\nTesting abbreviate on arbitrary data include special char...')
        # get data
        data = [0, 12, 3, ' ', list(), dict(), 'W0rds4u', 'T3st']
        data += [s for s in string.punctuation]
        data += ['Hel&&loW0()rlD', 843, 7 % 5, '1234']
        data += [{'Word': 123, 'Foobar': 'Germany', 123: 'working'}]

        excludes = ['_', '#', '-']
        a = abbreviation.Abbreviation(exclude_characters=excludes)
        for n in range(1, 4):
            print('Testing with length = %s:' % n)
            self.assertRaises(Exception, a.abbreviate(data, n))
        # end for linear O(n) iterating length of abbr, ranging from 1 to 4
    # end def test_abbreviate_on_arbitrary_data_exclude_characters

    def test_abbreviate_on_maya_nodes_excluding_abbreviation(self):
        """Test abbreviate method on maya nodes including special characters"""
        print('\nTesting abbreviate on maya nodes excluding abbreviations...')
        # get data
        file_name = 'maya_nodes.json'
        data_path = os.path.join(__file__, os.pardir, os.pardir, 'data')
        file_path = os.path.join(os.path.abspath(data_path), file_name)
        with open(file_path) as json_data:
            data = json.load(json_data)
        # end with get data from file

        exclusions = {'pointConstraint': ['PC', 'PCN'], 'remapValue': ['RMV']}
        a = abbreviation.Abbreviation(exclude_abbreviation=exclusions)
        self.assertRaises(Exception, a.abbreviate(data, 3))
    # end def test_abbreviate_on_maya_nodes_excluding_abbreviation

    def test_abbreviate_on_arbitrary_data_excluding_abbreviation(self):
        """Test abbreviate method on arbitrary data."""
        print('\nTesting abbreviate on arbitrary data excluding abbreviation')
        # get data
        data = [0, 12, 3, ' ', list(), dict(), 'W0rds4u', 'T3st']
        data += [s for s in string.punctuation]
        data += ['Hel&&loW0()rlD', 843, 7 % 5, '1234']
        data += [{'Word': 123, 'Foobar': 'Germany', 123: 'working'}]

        exclusions = {'Foobar': ['GE', 'GER'], 'Word': ['12', '123']}
        a = abbreviation.Abbreviation(exclude_abbreviation=exclusions)
        for n in range(1, 4):
            print('Testing with length = %s:' % n)
            self.assertRaises(Exception, a.abbreviate(data, n))
            print('OK')
        # end for linear O(n) iterating length of abbr, ranging from 1 to 4

        data = {'Word': 123, 'Foobar': 'Germany', 123: 'working'}
        print('Testing with dictionary as data and length = 3:')
        self.assertRaises(Exception, a.abbreviate(data, 3))
        print('OK')
    # end def test_abbreviate_on_arbitrary_data_excluding_abbreviation

    def test_abbreviate_on_maya_nodes_with_list_output(self):
        """Test abbreviate method on maya nodes outputting a list."""
        print('\nTesting abbreviate on maya nodes outputting a list...')
        # get data
        file_name = 'maya_nodes.json'
        data_path = os.path.join(__file__, os.pardir, os.pardir, 'data')
        file_path = os.path.join(os.path.abspath(data_path), file_name)
        with open(file_path) as json_data:
            data = json.load(json_data)
        # end with get data from file

        a = abbreviation.Abbreviation(output='list')
        self.assertRaises(Exception, a.abbreviate(data, 3))
    # end def test_abbreviate_on_maya_nodes_with_list_output

    def runTest(self):
        self.test_abbreviate_on_maya_nodes_data()
        self.test_abbreviate_on_countries_data()
        self.test_abbreviate_on_arbitrary_data()
        self.test_abbreviate_on_zero_length()
        self.test_abbreviate_on_negative_length()
        self.test_abbreviate_on_wrong_data_type()
        self.test_abbreviate_on_valid_case()
        self.test_abbreviate_on_invalid_case()
        self.test_abbreviate_on_maya_nodes_excluding_abbreviation()
        self.test_abbreviate_on_arbitrary_data_excluding_abbreviation()
        self.test_abbreviate_on_maya_nodes_with_list_output()
# end class TestAbbreviation


def create_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestAbbreviation())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = create_test_suite()
    runner.run(test_suite)
