"""
@author: Emre Tekinalp
@contact: e.tekinalp@icloud.com
@since: May 28th 2016
@brief: Unit tests on strategy pattern module
"""


from src.design_pattern import strategy_pattern


def unit_test():
    """Test setup for strategy pattern."""
    student = strategy_pattern.Student()
    teacher = strategy_pattern.Teacher()
    doctor = strategy_pattern.Doctor()
    professor = strategy_pattern.Professor()

    # student
    print student
    student.speak()

    # teacher
    print teacher
    teacher.speak()
    teacher.set_language(strategy_pattern.English())
    teacher.speak()

    # doctor
    print doctor
    doctor.speak()
    doctor.set_language(strategy_pattern.English())
    doctor.speak()
    doctor.set_language(strategy_pattern.German())
    doctor.speak()

    # professor
    print professor
    professor.speak()
    professor.set_language(strategy_pattern.English())
    professor.speak()
    professor.set_language(strategy_pattern.German())
    professor.speak()
    professor.set_language(strategy_pattern.French())
    professor.speak()
# end def test

unit_test()
