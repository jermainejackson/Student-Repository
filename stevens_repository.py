#!/bin/python
from typing import Any, List, Optional, Sequence, Iterator, DefaultDict, Tuple, Set, Dict
from typing.io import IO
from prettytable import PrettyTable
import sqlite3
from flask import Flask
app = Flask(__name__)
from jinja2 import Template
import os
from flask import Flask, render_template
app = Flask(__name__)
db_path: str = "/Users/jermainejackson/PycharmProjects/ssw810/hw11.sqlite.db"
student_grades_db: List[str] = list()

@app.route("/")
def template_test():
    if os.path.exists(db_path):
        db_file: str = db_path
        res = PrettyTable()
        db: sqlite3.Connection = sqlite3.connect(db_file)
        query: str = f"select o.Name,o.CWID,i.Course, i.Grade, s.Name from students o join grades i on o.CWID == i.StudentCWID join instructors s on s.CWID = i.InstructorCWID order by o.Name"
        for row in db.execute(query):
            student_grades_db.append(row)
    else:
        raise FileNotFoundError(f"Can't open {db_path}")
    return render_template('template.html', repository=student_grades_db)

if __name__ == '__main__':
    app.run(debug=True)



