#!/bin/python
'''
Created on July 18 2020
@author: Jermaine Jackson
This is a data repository of courses, students and instructors to helps University
faculty and students to create study plans
'''
import collections
import os
from collections import defaultdict
from typing import Any, List, Optional, Sequence, Iterator, DefaultDict, Tuple, Set, Dict
from datetime import date, datetime, timedelta
from typing.io import IO
from prettytable import PrettyTable



class University:
    '''
    Stores students, instructor and grades
    '''

    def __init__(self, directory: str) -> None:
        """
        initialize directory and files_summary
        """
        self.directory: str = directory
        self.files_summary_grades: List[str] = list()
        self.grades_data_file = 'grades.txt'

        self.grades_data = self.grade_file_reader()
        self.students_data: Student = Student(directory,self.files_summary_grades)
        self.instructor_data: Instructor = Instructor(directory,self.files_summary_grades)




    def grade_file_reader(self) -> None:
        '''
         process student data
         '''

        sep = '\t'
        fields = 4
        header = False

        try:
            fp: IO = open(os.path.join(self.directory, self.grades_data_file), 'r', encoding='utf-8')
        except FileNotFoundError:
            return (f"Error can't open {os.path.join(self.directory, self.grades_data_file)}")
        else:
            with fp:
                for number, line in enumerate(fp):
                    grades_fields = line.strip('\n').split(sep)
                    try:
                        if len(grades_fields) == fields:
                            self.files_summary_grades.append(tuple(grades_fields))
                        else:
                            print(
                                f"Warning file has {grades_fields} but expected {fields}")
                    except IndexError as e:
                        return (f"Error {e} in {os.path.join(self.directory, self.grades_data_file)} at line {line}")



        return self.files_summary_grades





class Student:
    """
    initialize directory and files_summary
    """
    def __init__(self, directory: str, grades: str) -> None:
        """
        initialize directory and files_summary
        """
        self.directory: str = directory
        self.files_summary_student: Dict[str, Dict[str, int]] = dict()
        self.grades = grades
        self.sep = '\t'
        self.fields = 3
        self.header = False
        self.student_data_file = 'students.txt'

        self.student_file_reader(grades)


    def student_file_reader(self, other: "Student") -> None:
        '''
        process student data
        '''
        student_id: Dict[str, str] = dict()
        number: str = 1
        line: str
        v: str
        id: str

        try:
            fp:IO = open(os.path.join(self.directory,self.student_data_file), 'r', encoding='utf-8')
        except FileNotFoundError:
            return (f"Warning can't open {os.path.join(self.directory,self.student_data_file)}")
            pass
        else:
            with fp:
                    for number, line in enumerate (fp):
                        student_fields: str = line.strip('\n').split(self.sep)
                        try:
                            if len(student_fields) == self.fields:
                                if sum([1 for v, v in enumerate(other) if v[0] == student_fields[0]]) == 0:
                                    print(
                                        f"Warning unknown student {student_fields[0]} in {os.path.join(self.directory, {os.path.join(self.directory,self.student_data_file)})} but not in grade file 'grades.txt'")
                                for id in other:
                                    if id[0] == student_fields[0]:
                                        if id[0] in student_id:
                                            student_id[student_fields[0]] =  student_id[student_fields[0]] + [id[1]]
                                        else:
                                            student_id[student_fields[0]] = [id[1]]
                                    if student_fields[0] in student_id:
                                        self.files_summary_student[student_fields[0]] = {'Name': student_fields[1],
                                                                                          'Completed Courses': student_id[student_fields[0]]}
                            else:
                                line_number: int = number+1
                                num_of_values: int = len(student_fields)
                                print (f"Warning : {os.path.join(self.directory,self.student_data_file)} has {num_of_values} fields on line {line_number} but expected {self.fields}")

                        except IndexError as e:
                            return (
                                f"Error {e} in {os.path.join(self.directory, self.student_data_file)} at line {line}")

                    return self.files_summary_student

    def pretty_print(self) -> None:
        """
        display the summary using pretty table format
        """
        res = PrettyTable()
        res.field_names = ["CWID", "Name", "Completed Courses"]
        for key, value in sorted(self.files_summary_student.items(), key = lambda x : (x[0][2])):
                res.add_row([key, value['Name'], value['Completed Courses']])
        print(f'Student summary')
        print(res)



class Instructor:
    """
    initialize directory and files_summary
    """
    def __init__(self, directory: str, grades: str) -> None:
        """
        initialize directory and files_summary
        """
        self.directory: str = directory
        self.files_summary_instructor: DefaultDict[str] = defaultdict(set)
        self.files_counts_classes: List[str] = list()
        self.grades = grades
        self.sep = '\t'
        self.fields = 3
        self.header = False
        self.instructor_data_file = 'instructors.txt'


        self.instructor_file_reader(grades)


    def instructor_file_reader(self, other: "Instructor") -> None:
        '''
        process instructor data and return results
        '''
        instructor_id: Dict[str, str] = dict()
        instruct_feq: Dict[str, str] = dict()
        number: str = 1
        id: str
        line: str

        for id in other:
            self.files_counts_classes.append((id[3],id[1]))

        for grade in self.files_counts_classes:
            if (grade in instruct_feq):
                instruct_feq[grade] += 1
            else:
                instruct_feq[grade] = 1


        try:
            fp: IO = open(os.path.join(self.directory, self.instructor_data_file), 'r', encoding='utf-8')
        except FileNotFoundError:
            return(f"Warning can't open {os.path.join(self.directory, self.instructor_data_file)}")
        else:
            with fp:
                for number, line in enumerate(fp):
                    instructor_fields: str = line.strip('\n').split(self.sep)
                    try:
                        if len(instructor_fields) == self.fields:
                            if sum([1 for v, v in enumerate(other) if v[3] == instructor_fields[0]]) == 0:
                                print(
                                    f"Warning unknown instructor {instructor_fields[0]} in {os.path.join(self.directory,self.instructor_data_file)} but not in grade file 'grades.txt'")
                            for id in other:
                                if id[3] == instructor_fields[0]:
                                    self.files_summary_instructor[instructor_fields[0]].add(
                                        (instructor_fields[1], instructor_fields[2], id[1], instruct_feq[(instructor_fields[0],id[1])] ))

                        else:
                            line_number: int = number + 1
                            num_of_values: int = len(instructor_fields)
                            print(
                                f"Warning : {os.path.join(self.directory, self.instructor_data_file)} has {num_of_values} fields on line {line_number} but expected {self.fields}")

                    except IndexError as e:
                        return (f"Error {e} in {os.path.join(self.directory, self.instructor_data_file)} at line {line}")

        return self.files_summary_instructor


    def pretty_print(self) -> None:
        """
        display the instructor summary using pretty table format
        """
        res = PrettyTable()
        res.field_names = ["CWID", "Name", "Dept", "Course", "Students"]
        for key, value in sorted(self.files_summary_instructor.items(), key = lambda x : (x[0][2])):
            for k in value:
                res.add_row([key, k[0], k[1], k[2], k[3]])
        print(f'Instructor summary')
        print(res)
