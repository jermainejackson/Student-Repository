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
        self.assertEqual(self.university_data.students_data.files_summary_student['10103']['Name'],'Jobs, S')
        self.assertEqual(self.university_data.students_data.files_summary_student['10115']['Name'], 'Bezos, J')
        self.assertEqual(self.university_data.students_data.files_summary_student['10183']['Name'], 'Musk, E')
        self.assertEqual(self.university_data.students_data.files_summary_student['11714']['Name'], 'Gates, B')


        self.assertEqual(self.university_data.students_data.files_summary_student['10103']['Major'],
                         'SFEN')

        self.assertEqual(self.university_data.students_data.files_summary_student['10115']['Major'],
                         'SFEN')

        self.assertEqual(self.university_data.students_data.files_summary_student['10183']['Major'],
                         'SFEN')

        self.assertEqual(self.university_data.students_data.files_summary_student['11714']['Major'],
                         'CS')

        self.assertEqual(sorted(self.university_data.students_data.files_summary_student['10103']['Completed Courses']),
                         ['CS 501', 'SSW 810'])

        self.assertEqual(sorted(self.university_data.students_data.files_summary_student['10115']['Completed Courses']),
                         ['SSW 810'])

        self.assertEqual(sorted(self.university_data.students_data.files_summary_student['10183']['Completed Courses']),
                         ['SSW 555', 'SSW 810'])

        self.assertEqual(sorted(self.university_data.students_data.files_summary_student['11714']['Completed Courses']),
                         ['CS 546', 'CS 570', 'SSW 810'])

        self.assertEqual(sorted(list((set(self.university_data.majors_data[('SFEN', 'R')])
                    - set(self.university_data.students_data.files_summary_student['10103']['Completed Courses'])))), ['SSW 540', 'SSW 555'])

        self.assertEqual(sorted(list((set(self.university_data.majors_data[('SFEN', 'R')])
                    - set(self.university_data.students_data.files_summary_student['10115']['Completed Courses'])))), ['SSW 540', 'SSW 555'])

        self.assertEqual(sorted(list((set(self.university_data.majors_data[('SFEN', 'R')])
                    - set(self.university_data.students_data.files_summary_student['10183']['Completed Courses'])))), ['SSW 540'])

        self.assertEqual(sorted(list((set(self.university_data.majors_data[('CS', 'R')])
                    - set(self.university_data.students_data.files_summary_student['11714']['Completed Courses'])))), [])

        self.assertEqual(sorted([x for x in (list(set(self.university_data.process_majors()[('SFEN', 'E')])
                                           - set(self.university_data.students_data.files_summary_student['10103']['Completed Courses'])))
                          if not set(self.university_data.process_majors()[('SFEN', 'E')]).intersection(
                set(self.university_data.students_data.files_summary_student['10103']['Completed Courses']))
                          ]), [])

        self.assertEqual(sorted([x for x in (list(set(self.university_data.process_majors()[('SFEN', 'E')])
                                           - set(self.university_data.students_data.files_summary_student['10115']['Completed Courses'])))
                          if not set(self.university_data.process_majors()[('SFEN', 'E')]).intersection(
                set(self.university_data.students_data.files_summary_student['10115']['Completed Courses']))
                          ]), ['CS 501', 'CS 546'])


        self.assertEqual(sorted([x for x in (list(set(self.university_data.process_majors()[('SFEN', 'E')])
                                           - set(self.university_data.students_data.files_summary_student['10183']['Completed Courses'])))
                          if not set(self.university_data.process_majors()[('SFEN', 'E')]).intersection(
                set(self.university_data.students_data.files_summary_student['10183']['Completed Courses']))
                          ]), ['CS 501', 'CS 546'])


        self.assertEqual(sorted([x for x in (list(set(self.university_data.process_majors()[('SFEN', 'E')])
                                           - set(self.university_data.students_data.files_summary_student['11714']['Completed Courses'])))
                          if not set(self.university_data.process_majors()[('SFEN', 'E')]).intersection(
                set(self.university_data.students_data.files_summary_student['11714']['Completed Courses']))
                          ]), [])


        self.assertEqual(round((self.university_data.students_data.files_summary_student['10103']['GPA']['10103']
               /len(self.university_data.students_data.files_summary_student['10103']['Completed Courses'])),2),3.38)


        self.assertEqual(round((self.university_data.students_data.files_summary_student['10115']['GPA']['10115']
               /len(self.university_data.students_data.files_summary_student['10115']['Completed Courses'])),2),4.0)

        self.assertEqual(round((self.university_data.students_data.files_summary_student['10183']['GPA']['10183']
               /len(self.university_data.students_data.files_summary_student['10183']['Completed Courses'])),2),4.0)

        self.assertEqual(round((self.university_data.students_data.files_summary_student['11714']['GPA']['11714']
               /len(self.university_data.students_data.files_summary_student['11714']['Completed Courses'])),2),3.5)



    def test_instructor_repository(self) -> None:
        """ testing instructor repository and display data """
        self.assertEqual(self.university_data.instructor_data.files_summary_instructor['98764'],
                         {('Cohen, R', 'SFEN', 'CS 546', 1)})

        self.assertEqual(self.university_data.instructor_data.files_summary_instructor['98763'],
                         {('Rowland, J', 'SFEN', 'SSW 810', 4), ('Rowland, J', 'SFEN', 'SSW 555', 1)})

        self.assertEqual(self.university_data.instructor_data.files_summary_instructor['98762'],
                         {('Hawking, S', 'CS', 'CS 501', 1),
                          ('Hawking, S', 'CS', 'CS 546', 1),
                          ('Hawking, S', 'CS', 'CS 570', 1)})



    def test_major_repository(self) -> None:
        """ testing major repository and display data """
        self.assertEqual(sorted(self.university_data.files_summary_majors[('SFEN', 'R')]),
                         ['SSW 540', 'SSW 555', 'SSW 810'])
        self.assertEqual(sorted(self.university_data.files_summary_majors[('SFEN', 'E')]),
                         ['CS 501', 'CS 546'])

        self.assertEqual(sorted(self.university_data.files_summary_majors[('CS', 'R')]),
                         ['CS 546', 'CS 570'])
        self.assertEqual(sorted(self.university_data.files_summary_majors[('CS', 'E')]),
                         ['SSW 565', 'SSW 810'])


    def test_db_student_grades(self) -> None:
        """ testing database student data """

        self.university_data.student_grades_table_db('/Users/jermainejackson/binaries/hw11.sqlite.db')
        self.assertEqual(self.university_data.student_grades_db[0],
                         ('Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'))

        self.assertEqual(self.university_data.student_grades_db[1],
                         ('Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'))

        self.assertEqual(self.university_data.student_grades_db[2],
                         ('Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'))

        self.assertEqual(self.university_data.student_grades_db[3],
                         ('Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'))

        self.assertEqual(self.university_data.student_grades_db[4],
                         ('Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'))

        self.assertEqual(self.university_data.student_grades_db[5],
                         ('Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'))

        self.assertEqual(self.university_data.student_grades_db[6],
                         ('Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'))

        self.assertEqual(self.university_data.student_grades_db[7],
                         ('Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'))

        self.assertEqual(self.university_data.student_grades_db[8],
                         ('Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J'))



    def test_display_results(self) -> None:
        """
        print the results for majors, students and professors
        """
        self.university_data.pretty_print_majors()
        self.university_data.students_data.pretty_print()
        self.university_data.instructor_data.pretty_print()
        self.university_data.pretty_print_student_grades_table_db()



if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)