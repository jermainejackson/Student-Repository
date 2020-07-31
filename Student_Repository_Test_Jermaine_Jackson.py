#!/bin/python
'''
Created on July 26 2020
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

    university_data: University = University('/Users/jermainejackson/PycharmProjects/ssw810/University_Files')

    def test_student_repository(self) -> None:
        """ testing students repository and display data """
        self.assertEqual(self.university_data.students_data.files_summary_student['10103']['Name'],'Baldwin, C')
        self.assertEqual(self.university_data.students_data.files_summary_student['10103']['Major'],
                         'SFEN')
        self.assertEqual(self.university_data.students_data.files_summary_student['10103']['Completed Courses'],
                         ['SSW 567', 'SSW 564', 'SSW 687', 'CS 501'])

        self.assertEqual(sorted(list((set(self.university_data.process_majors()[('SFEN', 'R')])
                    - set(self.university_data.students_data.files_summary_student['10103']['Completed Courses'])))), ['SSW 540', 'SSW 555'])


        self.assertEqual([x for x in (list(set(self.university_data.process_majors()[('SFEN', 'E')])
                - set(self.university_data.students_data.files_summary_student['10103']['Completed Courses'])))
               if not set(self.university_data.process_majors()[('SFEN', 'E')]).intersection(set(self.university_data.students_data.files_summary_student['10103']['Completed Courses']))
               ],[])

        self.assertEqual(sorted([x for x in (list(set(self.university_data.process_majors()[('SFEN', 'E')])
                - set(self.university_data.students_data.files_summary_student['10172']['Completed Courses'])))
               if not set(self.university_data.process_majors()[('SFEN', 'E')]).intersection(set(self.university_data.students_data.files_summary_student['10172']['Completed Courses']))
               ]),['CS 501', 'CS 513', 'CS 545'])

        self.assertEqual((self.university_data.students_data.files_summary_student['10103']['GPA']['10103']
               /len(self.university_data.students_data.files_summary_student['10103']['Completed Courses'])),3.4375)



    def test_instructor_repository(self) -> None:
        """ testing instructor repository and display data """
        self.assertEqual(self.university_data.instructor_data.files_summary_instructor['98765'], {('Einstein, A', 'SFEN', 'SSW 567', 4), ('Einstein, A', 'SFEN', 'SSW 540', 3)})
        self.assertEqual(self.university_data.instructor_data.files_summary_instructor['98764'], {('Feynman, R', 'SFEN', 'SSW 687', 3), ('Feynman, R', 'SFEN', 'CS 501', 1),
                                                                                             ('Feynman, R', 'SFEN', 'SSW 564', 3), ('Feynman, R', 'SFEN', 'CS 545', 1)})
        self.assertEqual(self.university_data.instructor_data.files_summary_instructor['98763'],{('Newton, I', 'SFEN', 'SSW 555', 1), ('Newton, I', 'SFEN', 'SSW 689', 1)})
        self.assertEqual(self.university_data.instructor_data.files_summary_instructor['98760'],{('Darwin, C', 'SYEN', 'SYS 645', 1), ('Darwin, C', 'SYEN', 'SYS 611', 2),
                                                                                            ('Darwin, C', 'SYEN', 'SYS 800', 1), ('Darwin, C', 'SYEN', 'SYS 750', 1)})


    def test_major_repository(self) -> None:
        """ testing major repository and display data """
        self.assertEqual(self.university_data.files_summary_majors[('SFEN', 'R')],
                         ['SSW 540', 'SSW 564', 'SSW 555', 'SSW 567'])
        self.assertEqual(self.university_data.files_summary_majors[('SFEN', 'E')],
                         ['CS 501', 'CS 513', 'CS 545'])
        self.assertEqual(self.university_data.files_summary_majors[('SYEN', 'R')],
                         ['SYS 671', 'SYS 612', 'SYS 800'])
        self.assertEqual(self.university_data.files_summary_majors[('SYEN', 'E')],
                         ['SSW 810', 'SSW 565', 'SSW 540'])



    def test_grades_repository(self) -> None:
        """ testing grades repository and display data """
        self.assertEqual(self.university_data.files_summary_grades[0],('10103', 'SSW 567', 'A', '98765'))
        self.assertEqual(self.university_data.files_summary_grades[1], ('10103', 'SSW 564', 'A-', '98764'))
        self.assertEqual(self.university_data.files_summary_grades[2], ('10103', 'SSW 687', 'B', '98764'))
        self.assertEqual(self.university_data.files_summary_grades[3], ('10103', 'CS 501', 'B', '98764'))
        self.assertEqual(self.university_data.files_summary_grades[4], ('10115', 'SSW 567', 'A', '98765'))
        self.assertEqual(self.university_data.files_summary_grades[5], ('10115', 'SSW 564', 'B+', '98764'))
        self.assertEqual(self.university_data.files_summary_grades[6], ('10115', 'SSW 687', 'A', '98764'))
        self.assertEqual(self.university_data.files_summary_grades[7], ('10115', 'CS 545', 'A', '98764'))
        self.assertEqual(self.university_data.files_summary_grades[8], ('10172', 'SSW 555', 'A', '98763'))
        self.assertEqual(self.university_data.files_summary_grades[9], ('10172', 'SSW 567', 'A-', '98765'))
        self.assertEqual(self.university_data.files_summary_grades[10], ('10175', 'SSW 567', 'A', '98765'))
        self.assertEqual(self.university_data.files_summary_grades[11], ('10175', 'SSW 564', 'A', '98764'))
        self.assertEqual(self.university_data.files_summary_grades[12], ('10175', 'SSW 687', 'B-', '98764'))
        self.assertEqual(self.university_data.files_summary_grades[13], ('10183', 'SSW 689', 'A', '98763'))
        self.assertEqual(self.university_data.files_summary_grades[14], ('11399', 'SSW 540', 'B', '98765'))
        self.assertEqual(self.university_data.files_summary_grades[15], ('11461', 'SYS 800', 'A', '98760'))
        self.assertEqual(self.university_data.files_summary_grades[16], ('11461', 'SYS 750', 'A-', '98760'))
        self.assertEqual(self.university_data.files_summary_grades[17], ('11461', 'SYS 611', 'A', '98760'))
        self.assertEqual(self.university_data.files_summary_grades[18], ('11658', 'SSW 540', 'F', '98765'))
        self.assertEqual(self.university_data.files_summary_grades[19], ('11714', 'SYS 611', 'A', '98760'))
        self.assertEqual(self.university_data.files_summary_grades[20], ('11714', 'SYS 645', 'C', '98760'))
        self.assertEqual(self.university_data.files_summary_grades[21], ('11788', 'SSW 540', 'A', '98765'))

    def test_display_results(self) -> None:
        """
        print the results for majors, students and professors
        """
        self.university_data.pretty_print()
        self.university_data.students_data.pretty_print()
        self.university_data.instructor_data.pretty_print()





if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)