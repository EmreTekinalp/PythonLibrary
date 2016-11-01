"""
@package: abbreviation.abbreviation
@brief: Abbreviation algorithm abbreviating list of strings
@author: Emre Tekinalp
@contact: e.tekinalp@icloud.com
@data: Oct 31st, 2016
"""

__version__ = '0.1.0'
__author__ = 'Emre Tekinalp'
__docformat__ = 'reStructuredText'

import string
import logging

logging.basicConfig(format='', level=logging.DEBUG)

# Abbreviation constants
UPPERCASE = 0
LOWERCASE = 1
CAPITALIZE = 2
NEUTRAL = 3


class Abbreviation(object):

    """Abbreviation algorithm class which gets a list of string elements and
    returns a dict or list with the original string and its abbreviation.
    """

    def __init__(self, include_special_char=None, exclude_abbreviation=None,
                 output='dict'):
        """Initialize Abbreviation class.

        :param include_special_char: Include given items in computation
        :param exclude_abbreviation: Exclude given items in computation.
        :param output: Output a 'dict' or a 'list'

        exclude_abbreviation example:
        >>> # name: [abbreviations in diff length]
        >>> {'Friday': ['FR', 'FRI', 'FRID']}
        """
        # private args
        self._include_special_char = include_special_char
        self._exclude_abbreviation = exclude_abbreviation
        self._output = output
        self._case = None
        self._length = 0
    # end def __init__

    def abbreviate(self, data, length=3, case=UPPERCASE, duplicates=False):
        """Call abbreviation algorithm and return data.

        :param data: List data of string elements
        :param case: UPPERCASE return uppercase letters
                     LOWERCASE return lowercase letters
                     CAPITALIZE return capitalized letters
        :param length: Length of the abbreviated letters, minimum is 2
        :param duplicates: Remove duplicates in abbreviation
        """
        self._case = case
        self._length = length

        result = dict()

        for word in data:
            if self._check_exclusion(word, self._exclude_abbreviation, result):
                continue
            # end if skip exclusion
            word = self._check_word(word)
            w = dict()
            ln = self._length
            if ln > len(word):
                ln = len(word)
            # end if length length
            for i, c in enumerate(word):
                w[i] = c
            # end for dict key value
            abb = self._iterate_word(w)
            if len(abb) == ln:
                result[word] = self._sort_word(abb)
                result[word] = self._list_to_string(result[word])
            elif len(abb) < ln:
                result[word] = self._sort_word(self._increase_word(w, abb, ln))
                result[word] = self._list_to_string(result[word])
            else:
                result[word] = self._sort_word(self._decrease_word(w, abb, ln))
                result[word] = self._list_to_string(result[word])
            # end if result key value
        # end for iterate data

        if not duplicates:
            self._remove_duplicates(result)
        # end if remove duplicates

        if self._output == 'list':
            result = [[key, value] for key, value in result.items()]
        # end if convert dict to list
        print len(result), result
        return result
    # end def abbreviate

    def _check_exclusion(self, word, exclusion, result, check=False):
        """Check the word for special characters, remove and return result.

        :param word: word to check
        :param result: Final resulting dictionary
        :param check: Check length of given word, return true or false
        """
        if not exclusion:
            return None
        # end if no exclusion given
        if word in exclusion.keys():
            for val in exclusion[word]:
                if len(val) == self._length:
                    result[word] = val
                    check = True
                    break
                # end if add new abbreviation
            # end for iterate value in exclusion
            if check:
                return True
            # end if skip item
        # end if word in exclusion
    # end def _check_exclusion

    def _check_word(self, word):
        """Check the word for special characters, remove and return result.

        :param word: word to check
        """
        chars = string.punctuation
        if self._include_special_char:
            for ch in self._include_special_char:
                if ch in chars:
                    chars = '%s%s' % (chars.split(ch)[0], chars.split(ch)[1])
                else:
                    msg = 'include_special_char: character not valid %s' % ch
                    raise ValueError(msg)
                # end if remove character from specials
            # end for iterate include special characters
        # end if include special char initialized
        for ch in chars:
            if ch in word:
                word = ''.join(w.capitalize() for w in word.split(ch))
            # end if check special character
        # end for iterate special characters
        return word
    # end def _check_word

    @staticmethod
    def _iterate_word(word):
        """Iterate the given word and return it.

         paramword <dict> word to iterate
        """
        result = dict()
        for w in word.items():
            if not w[0]:
                result[w[0]] = w[1]
            # end if 0 index
            if w[1].isupper():
                result[w[0]] = w[1]
            # end if isupper
        # end for iterate word dict
        return result
    # end def _iterate_word

    @staticmethod
    def _sort_word(word):
        """Reorder the dictionary and return a list.

        :param word <dict> dict to convert to list and sort
        """
        indices = list(word.keys())
        indices.sort()
        return [word[i] for i in indices]
    # end def _sort_word

    def _increase_word(self, word, abbreviation, length):
        """Abbreviation is smaller than 3 characters, increase and return.

        :param abbreviation <dict> abbreviated characters
        :param word <dict> Word to apply the filter on
        :param length <int> Length of the word
        """
        if len(abbreviation) == length:
            return abbreviation
        # end if recursion
        for key in abbreviation.keys():
            if key in word:
                del(word[key])
            # end if delete item
        # end for iteration
        res = self._add_char(self._filter_vowels(word, length), abbreviation)
        return self._increase_word(word, res, length)
    # end def _increase_word

    @staticmethod
    def _filter_vowels(elements, length):
        """Helper function to filter out all vowels characters of the
        given word and return the result.

        :param elements: Word to apply the filter on
        :param length: Length of the word
        """
        vowels = ('a', 'e', 'i', 'o', 'u')
        for key in elements.keys():
            if elements[key] in vowels:
                if not len(elements) < length:
                    del(elements[key])
                # end if delete item
            # end if check vowels
        # end for iterate word keys
        return elements
    # end def _filter_vowels

    @staticmethod
    def _add_char(elements, abbreviation):
        """Based on the given abbreviation and word find the next char.

        :param abbreviation <dict> abbreviated characters
        :param elements <dict> Word to apply the filter on
        """
        for w in elements:
            if len(abbreviation.keys()) > 1:
                if abbreviation.keys()[1] > w > abbreviation.keys()[0]:
                    abbreviation[w] = elements[w]
                    break
                else:
                    abbreviation[w] = elements[w]
                    break
                # end if add to abbreviation
            else:
                if w > abbreviation.keys()[0]:
                    abbreviation[w] = elements[w]
                    break
                # end if add to abbreviation
            # end if length check
        # end for iteration
        return abbreviation
    # end def _add_char

    def _list_to_string(self, items):
        """Convert a given list into a string, set case for each character.

        :param items <list> List to convert to string
        """
        return self._setup_case(''.join(item for item in items))
    # end def _list_to_string

    def _setup_case(self, word):
        """Setup the word to upper, lower or capitalized case.

        :param word: String to setup the case mode
        """
        if self._case == UPPERCASE:
            return word.upper()
        elif self._case == LOWERCASE:
            return word.lower()
        elif self._case == CAPITALIZE:
            return word.capitalize()
        elif self._case == NEUTRAL:
            return word
        else:
            msg = 'case: Use constant UPPERCASE, LOWERCASE or CAPITALIZE!'
            raise ValueError(msg)
        # end if setup case
    # end def _setup_case

    def _decrease_word(self, word, abbreviation, length):
        """Abbreviation is bigger than 3 characters, decrease and return.

        :param word <dict> dict to delete elements
        :param abbreviation <dict> abbreviated characters
        :param length <int> Length of the word
        """
        if len(abbreviation) == length:
            return abbreviation
        # end if recursion
        for key in abbreviation.keys():
            if key in word:
                del(word[key])
            # end if delete item
        # end for iteration
        result = self._subtract_char(abbreviation)
        return self._decrease_word(result, word, length)
    # end def _decrease_word

    def _subtract_char(self, abbreviation):
        """Based on the given abbreviation and word find the next char.

        :param abbreviation <dict> abbreviated characters
        """
        del(abbreviation[max(abbreviation.keys())])
        return abbreviation
    # end def _subtract_char

    def _remove_duplicates(self, result, rest=dict()):
        """Remove duplicates from the given dictionary.

        :param result <dict> Storing all values mutating given dictionary
        """
        excess = set(result.values())

        converted = self._convert_dict(result)
        difference = self._allocate_dict_duplicates(converted, excess)
        length = [s for s in range(self._length)][1:]
        for value in difference.values():
            letters = value.values()[0][1:]
            for i in length:
                if self._compare_to_dict(value, letters, result, i, rest):
                    break
                # end if added new element
            # end for iterate length
        # end for iterate dict values
        for k, v in rest.items():
            if v not in result.values():
                result[k] = v
                del(rest[k])
            # end if update result and rest
            if result[k] != v:
                if result.values().count(result[k]) == 1:
                    del(rest[k])
                # end if delete from rest
            # end if result not in value
        # end for iterate rest items
        print 'duplicates >>>', rest
        if rest:
            logging.debug('For %s names I could not create individual '
                          'abbreviations: %s' % (len(rest), rest))
        # end if logging report
    # end def _remove_duplicates

    def _convert_dict(self, elements, result=dict(), index=0):
        """Convert key and values of given dictionary into value and create
        an index number as a key. Mutate the given dictionary.

        :param elements <dict> Storing all the abbreviations and nodenames
        :param result <dict> Storing all values in a new dictionary
        :param index <int> Unsigned integer to iterate the depth level
        """
        for key, value in elements.items():
            result[index] = {value: key}
            index += 1
        # end for
        return result
    # end def _convert_dict

    def _allocate_dict_duplicates(self, elements, excess, diff=dict()):
        """Return duplicates in given dictionary as a new dictionary.

        :param elements <dict> Storing all the abbreviations and nodenames
        :param excess <dict> Storing only the duplicates
        :param diff <dict> Storing the differences of intersecting values
        """
        temp = dict()
        for e in excess:
            for key, value in elements.items():
                if e not in value:
                    continue
                # end if check existence of item
                if e not in temp:
                    temp[e] = value
                else:
                    diff[key] = value
                # end if get difference
            # end for iterate dict values
        # end for iterate excess values
        return diff
    # end def _allocate_dict_duplicates

    def _compare_to_dict(self, item, letters, elements, index, rest):
        """Compare redundant item with whole dictionary and individualize.

        :param item <dict> Nodename as key and abbreviation as value
        :param letters <string> NodeName string to iterate through each char
        :param elements <dict> The whole dictionary of abbreviations
        :param index <int> Index number of the abbreviation to replace the char
        :param rest <dict> Output of non abbreviatable nodeNames
        """
        if not letters:
            for k, v in elements.items():
                if item.keys()[0] == v:
                    if item.values()[0] == k:
                        rest[k] = v
                    # end if add to undefinable rest
                    if self._iterate_abbreviation({v: k}, k, elements, index):
                        break
                    # end if item added to elements
                # end if item exist in elements
            # end for iterate elements
            return
        # end if no letters left
        key, value = item.items()[0]
        abb = self._setup_case(key.replace(key[index], letters[0]))
        if abb not in elements.values():
            elements[value] = abb
            return True
        # end if key not in elements values
        return self._compare_to_dict(item, letters[1:], elements, index, rest)
    # end def _compare_to_dict

    def _iterate_abbreviation(self, item, letters, elements, index):
        """Iterate, compare and return given abbreviation to whole dictionary.

        :param item <dict> Nodename as key and abbreviation as value
        :param letters <string> NodeName string to iterate through each char
        :param elements <dict> The whole dictionary of abbreviations
        :param index <int> Index number of abbreviation to replace the char
        """
        for letter in letters:
            key, value = item.items()[0]
            abb = self._setup_case(key.replace(key[index], letter))
            if abb not in elements.values():
                elements[value] = abb
                return True
            # end if key not in elements values
        # end if iterate letters
    # end def _iterate_abbreviation
# end class Abbreviation


def test_abbreviation():
    """Setup function to test Abbreviation class"""
    # from maya import cmds
    import os, json
    data = ['Friday']
    # data += cmds.allNodeTypes()
    file_name = 'maya_nodes.json'
    data_path = os.path.join(__file__, os.pardir, os.pardir, 'data')
    file_path = os.path.join(os.path.abspath(data_path), file_name)
    with open(file_path) as json_data:
        data = json.load(json_data)
    # end with get data from file
    abb = Abbreviation(exclude_abbreviation={'Friday': ['FR', 'FRI', 'FRID'],
                                             'pointConstraint': ['PO']})
    result = abb.abbreviate(data, length=3)
    print(len(result))
    # for k, v in result.items():
    #     print k, v
    # print(result['polyCube'], result['pointConstraint'])
# end def test_abbreviation
