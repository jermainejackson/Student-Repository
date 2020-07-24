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
        self.files_summary_majors: DefaultDict[str] = defaultdict()
        self.grades_data_file = 'grades.txt'
        self.majors_data_file = 'majors.txt'

        self.grades_data = self.grade_file_reader()
        self.majors_data = self.major_file_reader()

        self.students_data: Student = Student(directory,self.files_summary_grades,self.files_summary_majors)
        self.students_data.pretty_print()
        self.instructor_data: Instructor = Instructor(directory,self.files_summary_grades)
        self.instructor_data.pretty_print()





    def grade_file_reader(self) -> 'grade_file_reader':
        '''
         process student data
         '''

        sep = '|'
        fields = 4
        header = True

        try:
            fp: IO = open(os.path.join(self.directory, self.grades_data_file), 'r', encoding='utf-8')
        except FileNotFoundError:
            return (f"Error can't open {os.path.join(self.directory, self.grades_data_file)}")
        else:
            with fp:
                for number, line in enumerate(fp,1):
                    grades_fields = line.strip('\n').split(sep)
                    try:
                        if len(grades_fields) == fields:
                            if number == 1 and header == True:
                                pass
                            else:
                                self.files_summary_grades.append(tuple(grades_fields))
                        else:
                            print(
                                f"Warning file has {len(grades_fields)} fields but expected {fields} at line {number}")
                    except IndexError as e:
                        return (f"Error {e} in {os.path.join(self.directory, self.grades_data_file)} at line {number}")

        return self.files_summary_grades



    def major_file_reader(self) -> 'major_file_reader':
        '''
         process majors data
         '''

        sep = '\t'
        fields = 3
        header = True

        try:
            fp: IO = open(os.path.join(self.directory, self.majors_data_file), 'r', encoding='utf-8')
        except FileNotFoundError:
            return (f"Error can't open {os.path.join(self.directory, self.majors_data_file)}")
        else:
            with fp:
                for number, line in enumerate(fp, 1):
                    majors_fields: str = line.strip('\n').split(sep)
                    try:
                        if len(majors_fields) == fields:
                            if number == 1 and header == True:
                                pass
                            else:
                                if (majors_fields[0],majors_fields[1]) in self.files_summary_majors:
                                    self.files_summary_majors[majors_fields[0],majors_fields[1]].append(majors_fields[2])
                                else:
                                    self.files_summary_majors[majors_fields[0],majors_fields[1]]=[
                                        majors_fields[2]]

                        else:
                            print(
                                f"Warning file has {len(majors_fields)} fields but expected {fields}")
                    except IndexError as e:
                        return (f"Error {e} in {os.path.join(self.directory, self.majors_data_file)} at line {line}")



            res = PrettyTable()
            res.field_names = ["Major", "Required Courses", "Electives"]
            res.add_row(('SFEN', self.files_summary_majors[('SFEN', 'R')], self.files_summary_majors[('SFEN', 'E')]))
            res.add_row(('SYEN', sorted(self.files_summary_majors[('SYEN', 'R')]),
                         sorted(self.files_summary_majors[('SYEN', 'E')])))
            print(f'Majors summary')
            print(res)


        return self.files_summary_majors





class Student:
    """
    initialize directory and files_summary
    """
    def __init__(self, directory: str, grades: str, majors: str) -> None:
        """
        initialize directory and files_summary
        """
        self.directory: str = directory
        self.files_summary_student: Dict[str, Dict[str, int]] = dict()
        self.grades = grades
        self.majors = majors
        self.sep = ';'
        self.fields = 3
        self.student_data_file = 'students.txt'

        self.student_file_reader(grades,majors)


    def student_file_reader(self, other: "Student", majors: "Student") -> "Student":
        '''
        process student data
        '''
        student_id: Dict[str, str] = dict()
        line: str
        v: str
        id: str
        grades: Dict[str, str] = {'A':4.0,'A-':3.75,'B+':3.25,'B':3.0,'B-':2.75,'C+':2.25,'C':2.0,'C-':0,'D+':0,'D':0,'D-':0,'F':0}
        total_grades: Dict[str, str] = dict()
        header: bool = True

        try:
            fp:IO = open(os.path.join(self.directory,self.student_data_file), 'r', encoding='utf-8')
        except FileNotFoundError:
            return (f"Warning can't open {os.path.join(self.directory,self.student_data_file)}")
            pass
        else:
            with fp:
                    for number, line in enumerate (fp,1):
                        student_fields: str = line.strip('\n').split(self.sep)
                        try:
                            if len(student_fields) == self.fields:
                                if number == 1 and header == True:
                                    pass
                                else:
                                    if str(other).find(str(student_fields[0])) == -1:
                                        print(f"Warning unknown student {student_fields[0]} in {os.path.join(self.directory, {os.path.join(self.directory,self.student_data_file)})} but not in grade file 'grades.txt'")
                                    else:
                                        for id in other:
                                            if id[0] == student_fields[0]:
                                                if id[0] in student_id:
                                                    total_grades[id[0]] = total_grades[id[0]] + grades[id[2]]
                                                    student_id[student_fields[0]] =  student_id[student_fields[0]] + [id[1]]
                                                else:
                                                    total_grades[id[0]] = grades[id[2]]
                                                    student_id[student_fields[0]] = [id[1]]
                                            if student_fields[0] in student_id:
                                                self.files_summary_student[student_fields[0]] = {'Name': student_fields[1],'Major':student_fields[2],
                                                                                                  'Completed Courses': student_id[student_fields[0]], 'GPA': total_grades}
                            else:
                                num_of_values: int = len(student_fields)
                                print (f"Warning : {os.path.join(self.directory,self.student_data_file)} has {num_of_values} fields on line {number} but expected {self.fields}")

                        except IndexError as e:
                            return (
                                f"Error {e} in {os.path.join(self.directory, self.student_data_file)} at line {number}")


                    return self.files_summary_student


    def pretty_print(self) -> None:
        """
        display the summary using pretty table format
        """
        res = PrettyTable()
        res.field_names = ["CWID", "Name", "Major", "Completed Courses", "Remaining Required", "Remaining Electives","GPA"]
        for key, value in sorted(self.files_summary_student.items(), key = lambda x : (x[0][2])):
                res.add_row([key, value['Name'], value['Completed Courses'],value['Major'],list(set(self.majors[(value['Major']),'R']) - set(value['Completed Courses'])),[ x for x in (list(set(self.majors[(value['Major']),'E']) - set(value['Completed Courses']))) if not set(self.majors[(value['Major']), 'E']).intersection(set(value['Completed Courses']))],round(value['GPA'][key]/len(value['Completed Courses']),2)])
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
        self.sep = '|'
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
        id: str
        line: str
        header: bool = True

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
                for number, line in enumerate(fp,1):
                    instructor_fields: str = line.strip('\n').split(self.sep)
                    try:
                        if len(instructor_fields) == self.fields:
                            if number == 1 and header == True:
                                pass
                            else:
                                if str(other).find(str(instructor_fields[0])) == -1:
                                    print(f"Warning unknown instructor {instructor_fields[0]} in {os.path.join(self.directory,self.instructor_data_file)} but not in grade file 'grades.txt'")
                                else:
                                    for id in other:
                                        if id[3] == instructor_fields[0]:
                                            self.files_summary_instructor[instructor_fields[0]].add(
                                                (instructor_fields[1], instructor_fields[2], id[1], instruct_feq[(instructor_fields[0],id[1])] ))

                        else:
                            num_of_values: int = len(instructor_fields)
                            print(
                                f"Warning : {os.path.join(self.directory, self.instructor_data_file)} has {num_of_values} fields on line {number} but expected {self.fields}")

                    except IndexError as e:
                        return (f"Error {e} in {os.path.join(self.directory, self.instructor_data_file)} at line {number}")

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



university_data: University = University('/Users/jermainejackson/PycharmProjects/ssw810/University_Files')
