#!/bin/python
'''
Created on July 18 2020
@author: Jermaine Jackson
This is a data repository of courses, students and instructors to helps University
faculty and students to create study plans
'''

import unittest
from typing import Any, List, Optional, Sequence, Iterator, DefaultDict, Tuple, Set
import os
import datetime
from typing.io import IO
from Student_Repository_Jermaine_Jackson import University, Student, Instructor


class RepositoryUnitTest(unittest.TestCase):

    def test_init_repository(self) -> None:
        """ testing init and exceptions """
        university_data: University = University('/Users/jermainejackson/PycharmProjects/ssw810/University_Files1')
        self.assertEqual(university_data.grade_file_reader(),"Error can't open /Users/jermainejackson/PycharmProjects/ssw810/University_Files1/grades.txt")

        university_data: University = University('/Users/jermainejackson/PycharmProjects/ssw810/University_Files')
        self.assertNotEqual(university_data.grade_file_reader(),
                         "Error can't open /Users/jermainejackson/PycharmProjects/ssw810/University_Files1/grades.txt")


    def test_student_repository(self) -> None:
        """ testing students repository and display data """
        university_data: University = University('/Users/jermainejackson/PycharmProjects/ssw810/University_Files')
        self.assertEqual(university_data.students_data.files_summary_student['10103']['Name'],'Baldwin, C')
        self.assertEqual(university_data.students_data.files_summary_student['10103']['Completed Courses'], ['SSW 567', 'SSW 564', 'SSW 687', 'CS 501'])
        self.assertEqual(university_data.students_data.files_summary_student['10115']['Name'],'Wyatt, X')
        self.assertEqual(university_data.students_data.files_summary_student['10115']['Completed Courses'], ['SSW 567', 'SSW 564', 'SSW 687', 'CS 545'])
        self.assertEqual(university_data.students_data.files_summary_student['10172']['Name'],'Forbes, I')
        self.assertEqual(university_data.students_data.files_summary_student['10172']['Completed Courses'], ['SSW 555', 'SSW 567'])
        self.assertEqual(university_data.students_data.files_summary_student['10175']['Name'],'Erickson, D')
        self.assertEqual(university_data.students_data.files_summary_student['10175']['Completed Courses'], ['SSW 567', 'SSW 564', 'SSW 687'])
        self.assertEqual(university_data.students_data.files_summary_student['10183']['Name'],'Chapman, O')
        self.assertEqual(university_data.students_data.files_summary_student['10183']['Completed Courses'], ['SSW 689'])
        self.assertEqual(university_data.students_data.files_summary_student['11399']['Name'],'Cordova, I')
        self.assertEqual(university_data.students_data.files_summary_student['11399']['Completed Courses'], ['SSW 540'])
        self.assertEqual(university_data.students_data.files_summary_student['11461']['Name'],'Wright, U')
        self.assertEqual(university_data.students_data.files_summary_student['11461']['Completed Courses'], ['SYS 800', 'SYS 750', 'SYS 611'])
        self.assertEqual(university_data.students_data.files_summary_student['11658']['Name'],'Kelly, P')
        self.assertEqual(university_data.students_data.files_summary_student['11658']['Completed Courses'], ['SSW 540'])
        self.assertEqual(university_data.students_data.files_summary_student['11714']['Name'],'Morton, A')
        self.assertEqual(university_data.students_data.files_summary_student['11714']['Completed Courses'], ['SYS 611', 'SYS 645'])
        self.assertEqual(university_data.students_data.files_summary_student['11788']['Name'],'Fuller, E')
        self.assertEqual(university_data.students_data.files_summary_student['11788']['Completed Courses'], ['SSW 540'])
        print (university_data.students_data.pretty_print())


    def test_instructor_repository(self) -> None:
        """ testing instructor repository and display data """
        university_data: University = University('/Users/jermainejackson/PycharmProjects/ssw810/University_Files')
        self.assertEqual(university_data.instructor_data.files_summary_instructor['98765'], {('Einstein, A', 'SFEN', 'SSW 567', 4), ('Einstein, A', 'SFEN', 'SSW 540', 3)})
        self.assertEqual(university_data.instructor_data.files_summary_instructor['98764'], {('Feynman, R', 'SFEN', 'SSW 687', 3), ('Feynman, R', 'SFEN', 'CS 501', 1),
                                                                                             ('Feynman, R', 'SFEN', 'SSW 564', 3), ('Feynman, R', 'SFEN', 'CS 545', 1)})
        self.assertEqual(university_data.instructor_data.files_summary_instructor['98763'],{('Newton, I', 'SFEN', 'SSW 555', 1), ('Newton, I', 'SFEN', 'SSW 689', 1)})
        self.assertEqual(university_data.instructor_data.files_summary_instructor['98760'],{('Darwin, C', 'SYEN', 'SYS 645', 1), ('Darwin, C', 'SYEN', 'SYS 611', 2),
                                                                                            ('Darwin, C', 'SYEN', 'SYS 800', 1), ('Darwin, C', 'SYEN', 'SYS 750', 1)})
        print(university_data.instructor_data.pretty_print())


    def test_grades_repository(self) -> None:
        """ testing grades repository and display data """
        university_data: University = University('/Users/jermainejackson/PycharmProjects/ssw810/University_Files')
        self.assertEqual(university_data.files_summary_grades[0],('10103', 'SSW 567', 'A', '98765'))
        self.assertEqual(university_data.files_summary_grades[1], ('10103', 'SSW 564', 'A-', '98764'))
        self.assertEqual(university_data.files_summary_grades[2], ('10103', 'SSW 687', 'B', '98764'))
        self.assertEqual(university_data.files_summary_grades[3], ('10103', 'CS 501', 'B', '98764'))
        self.assertEqual(university_data.files_summary_grades[4], ('10115', 'SSW 567', 'A', '98765'))
        self.assertEqual(university_data.files_summary_grades[5], ('10115', 'SSW 564', 'B+', '98764'))
        self.assertEqual(university_data.files_summary_grades[6], ('10115', 'SSW 687', 'A', '98764'))
        self.assertEqual(university_data.files_summary_grades[7], ('10115', 'CS 545', 'A', '98764'))
        self.assertEqual(university_data.files_summary_grades[8], ('10172', 'SSW 555', 'A', '98763'))
        self.assertEqual(university_data.files_summary_grades[9], ('10172', 'SSW 567', 'A-', '98765'))
        self.assertEqual(university_data.files_summary_grades[10], ('10175', 'SSW 567', 'A', '98765'))
        self.assertEqual(university_data.files_summary_grades[11], ('10175', 'SSW 564', 'A', '98764'))
        self.assertEqual(university_data.files_summary_grades[12], ('10175', 'SSW 687', 'B-', '98764'))
        self.assertEqual(university_data.files_summary_grades[13], ('10183', 'SSW 689', 'A', '98763'))
        self.assertEqual(university_data.files_summary_grades[14], ('11399', 'SSW 540', 'B', '98765'))
        self.assertEqual(university_data.files_summary_grades[15], ('11461', 'SYS 800', 'A', '98760'))
        self.assertEqual(university_data.files_summary_grades[16], ('11461', 'SYS 750', 'A-', '98760'))
        self.assertEqual(university_data.files_summary_grades[17], ('11461', 'SYS 611', 'A', '98760'))
        self.assertEqual(university_data.files_summary_grades[18], ('11658', 'SSW 540', 'F', '98765'))
        self.assertEqual(university_data.files_summary_grades[19], ('11714', 'SYS 611', 'A', '98760'))
        self.assertEqual(university_data.files_summary_grades[20], ('11714', 'SYS 645', 'C', '98760'))
        self.assertEqual(university_data.files_summary_grades[21], ('11788', 'SSW 540', 'A', '98765'))




if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)