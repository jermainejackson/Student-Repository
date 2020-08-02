#!/bin/python
'''
Created on July 26 2020
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
import sqlite3



class University:
    '''
    Stores students, instructor and grades
    '''

    def __init__(self, directory: str) -> "None":
        """
        initialize directory and files_summary
        """
        self.directory: str = directory
        self.files_summary_grades: List[str] = list()
        self.files_summary_majors: DefaultDict[str,str] = defaultdict()
        self.files_summary_student: Dict[str, Dict[str, int]] = dict()
        self.student_grades_db: List[str] = list()
        self.files_summary_instructor: DefaultDict[str] = defaultdict(set)
        self.files_counts_classes: List[str] = list()


        self.grades_data_file: str = self.file_reader('grades.txt', directory,'\t')
        self.majors_data_file: str = self.file_reader('majors.txt', directory,'\t')
        self.students_data_file: str = self.file_reader('students.txt', directory,'\t')
        self.instructors_data_file: str = self.file_reader('instructors.txt', directory,'\t')


        self.process_grades(self.grades_data_file,True,4)
        self.process_majors(self.majors_data_file, True, 3)
        self.student(self.grades_data_file,self.majors_data_file, self.students_data_file,True,3)
        self.instructor(self.grades_data_file, self.majors_data_file, self.instructors_data_file, True, 3)



    def file_reader(self,data_file: str, directory: str,sep: int):

        data: List[str] = list()

        try:
            with open(os.path.join(directory, data_file), 'r', encoding='utf-8') as fp:IO
        except FileNotFoundError:
            raise  FileNotFoundError (f"Can't open {os.path.join(directory, data_file)}")
        else:
            with open(os.path.join(directory, data_file), 'r') as fp:
                for line in fp:
                    data.append(line.strip('\n').split(sep))

        return data




    def process_grades(self,grades_data_file: List[str],header: bool,fields: int) -> 'process_grades':
        '''
         process student data
         '''

        for number, line in enumerate(grades_data_file,1):
            try:
                if len(line) == fields:
                    if number == 1 and header == True:
                        pass
                    else:
                        self.files_summary_grades.append(tuple(line))
                else:
                    print(
                        f"Warning grades  {self.grades_data_file} file has {len(line)} fields but expected {fields} at line {number}")
            except IndexError as e:
                return (f"Error {e} in {os.path.join(self.directory, self.grades_data_file)} at line {number}")

        return self.files_summary_grades



    def process_majors(self,majors_data_file: List[str],header: bool,fields: int) -> 'process_majors':
        '''
         process majors data
         '''

        for number, line in enumerate(majors_data_file, 1):
            try:
                if len(line) == fields:
                    if number == 1 and header == True:
                        pass
                    else:
                        if (line[0],line[1]) in self.files_summary_majors:
                            self.files_summary_majors[line[0],line[1]].append(line[2])
                        else:
                            self.files_summary_majors[line[0],line[1]]=[
                                line[2]]

                else:
                    print(
                        f"Warning file has {len(line)} fields but expected {fields}")
            except IndexError as e:
                return (f"Error {e} in {os.path.join(self.directory, self.majors_data_file)} at line {line}")

        return self.files_summary_majors


    def pretty_print_majors(self) -> None:
        """
            display the summary using pretty table format
        """
        res = PrettyTable()
        res.field_names = ["Major", "Required Courses", "Electives"]
        res.add_row(('SFEN', sorted(self.files_summary_majors[('SFEN', 'R')]), sorted(self.files_summary_majors[('SFEN', 'E')])))
        res.add_row(('CS', sorted(self.files_summary_majors[('CS', 'R')]),sorted(self.files_summary_majors[('CS', 'E')])))
        print(f'Majors summary')
        print(res)



    def student_grades_table_db(self,db_path: str):
        '''
        connect to db and display data
        '''
        if os.path.exists(db_path):
            db_file: str = db_path
            res = PrettyTable()
            db: sqlite3.Connection = sqlite3.connect(db_file)
            query: str = f"select o.Name,o.CWID,i.Course, i.Grade, s.Name from students o join grades i on o.CWID == i.StudentCWID join instructors s on s.CWID = i.InstructorCWID order by o.Name"
            for row in db.execute(query):
                self.student_grades_db.append(row)
        else:
            raise FileNotFoundError(f"Can't open {db_path}")



    def pretty_print_student_grades_table_db(self) -> None:
        """
            display the summary using pretty table format
        """
        res = PrettyTable()
        res.field_names = ["Name", "CWID", "Course","Grade", "Instructor"]
        for row in self.student_grades_db:
            res.add_row([row[0],row[1],row[2],row[3],row[4]])
        print(f'Student Grade Summary')
        print(res)



    def student(self, gd_list: List[str] , majors: List[str],student_data_file: List[str],header: bool,fields: int) -> "Student":
        '''
        process student data
        '''
        student_id: Dict[str, str] = dict()
        line: str
        v: str
        id: str
        grades: Dict[str, str] = {'A':4.0,'A-':3.75,'B+':3.25,'B':3.0,'B-':2.75,'C+':2.25,'C':2.0,'C-':0,'D+':0,'D':0,'D-':0,'F':0}
        total_grades: Dict[str, str] = dict()

        for number, line in enumerate (student_data_file,1):
            try:
                if len(line) == fields:
                    if number == 1 and header == True:
                        pass
                    else:
                        if str(gd_list).find(str(line[0])) == -1:
                            print(f"Warning unknown student {line[0]} in {os.path.join(self.directory, {os.path.join(self.directory,self.student_data_file)})} but not in grade file 'grades.txt'")
                        else:
                            for id in gd_list:
                                if id[0] == line[0]:
                                    if id[0] in student_id:
                                        total_grades[id[0]] = total_grades[id[0]] + grades[id[2]]
                                        if id[2] == 'F':
                                            student_id[line[0]] = student_id[line[0]] + []
                                        else:
                                            student_id[line[0]] =  student_id[line[0]] + [id[1]]
                                    else:
                                        total_grades[id[0]] = grades[id[2]]
                                        if id[2] == 'F':
                                            student_id[line[0]] = []
                                        else:
                                            student_id[line[0]] = [id[1]]
                                if line[0] in student_id:
                                    self.files_summary_student[line[0]] = {'Name': line[1],'Major':line[2],
                                                                                      'Completed Courses': student_id[line[0]], 'GPA': total_grades}
                else:
                    num_of_values: int = len(line)
                    print (f"Warning : {os.path.join(self.directory,self.student_data_file)} has {num_of_values} fields on line {number} but expected {fields}")

            except IndexError as e:
                return (
                    f"Error {e} in {os.path.join(self.directory, self.student_data_file)} at line {number}")

        return self.files_summary_student




    def instructor(self, gd_list: List[str] , majors: List[str],instructors_data_file: List[str],header: bool,fields: int) -> "instructor":
        '''
        process instructor data and return results
        '''
        instructor_id: Dict[str, str] = dict()
        instruct_feq: Dict[str, str] = dict()
        id: str
        line: str

        for id in gd_list:
            self.files_counts_classes.append((id[3],id[1]))

        for grade in self.files_counts_classes:
            if (grade in instruct_feq):
                instruct_feq[grade] += 1
            else:
                instruct_feq[grade] = 1


        for number, line in enumerate(instructors_data_file,1):
            try:
                if len(line) == fields:
                    if number == 1 and header == True:
                        pass
                    else:
                        if str(gd_list).find(str(line[0])) == -1:
                            print(f"Warning unknown instructor {line[0]} in {os.path.join(self.directory,self.instructors_data_file)} but not in grade file 'grades.txt'")
                        else:
                            for id in gd_list:
                                if id[3] == line[0]:
                                    self.files_summary_instructor[line[0]].add(
                                        (line[1], line[2], id[1], instruct_feq[(line[0],id[1])] ))

                else:
                    num_of_values: int = len(line)
                    print(
                        f"Warning : {os.path.join(self.directory, self.instructors_data_file)} has {num_of_values} fields on line {number} but expected {fields}")

            except IndexError as e:
                return (f"Error {e} in {os.path.join(self.directory, self.instructors_data_file)} at line {number}")

        return self.files_summary_instructor





class Student:
    """
    Student class
    """
    def __init__(self, files_summary_student:Dict[str, str], files_summary_majors: Dict[str, str]) -> None:
        """
        initialize student attributes
        """
        self.files_summary_student = files_summary_student
        self.files_summary_majors = files_summary_majors


    def student_pretty_print(self) -> None:
        """
        display the summary using pretty table format
        """
        res = PrettyTable()
        res.field_names = ["CWID", "Name", "Major", "Completed Courses", "Remaining Required", "Remaining Electives","GPA"]
        for key, value in sorted(self.files_summary_student.items()):
                res.add_row([key, value['Name'],value['Major'],sorted(value['Completed Courses']),sorted(list(set(self.files_summary_majors[(value['Major']),'R'])
                - set(value['Completed Courses']))),sorted([ x for x in (list(set(self.files_summary_majors[(value['Major']),'E']) - set(value['Completed Courses'])))
                if not set(self.files_summary_majors[(value['Major']), 'E']).intersection(set(value['Completed Courses']))]),
                                    round(value['GPA'][key]/len(value['Completed Courses']),2)])
        print(f'Student summary')
        print(res)




class Instructor:
    """
    Instructor class
    """
    def __init__(self, files_summary_instructor: Dict[str, str], files_summary_majors: Dict[str, str]) -> None:
        """
        initialize Instructor attributes
        """
        self.files_summary_instructor = files_summary_instructor
        self.files_summary_majors = files_summary_majors

    def instructor_pretty_print(self) -> None:
        """
        display the instructor summary using pretty table format
        """
        res = PrettyTable()
        res.field_names = ["CWID", "Name", "Dept", "Course", "Students"]
        for key, value in sorted(self.files_summary_instructor.items(), key = lambda x : (x[0][1])):
            for k in value:
                res.add_row([key, k[0], k[1], k[2], k[3]])
        print(f'Instructor summary')
        print(res)