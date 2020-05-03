import sqlite3
import sys
import os
import random
from datetime import datetime
from datetime import date

def mydate():
    return "-".join([str(date.today().month),str(date.today().day),str(date.today().year)])

# initialize local sqlite database according to hard-coded schema
def initialize_db():
    con = sqlite3.connect('db.sqlite3')
    #TODO

def list_books():
    try:
        # make database connection
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()

        # make select
        sqlite_select = """SELECT name FROM book;"""
        book_names = cursor.execute(sqlite_select).fetchall()
        return list(map(lambda a: a[0], book_names))
    except sqlite3.Error as error:
        print("Failed list", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


def list_sections(bookname):
    try:
        # make database connection
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()

        # grab book_id by book name
        book_id = cursor.execute(f"SELECT book_id FROM book WHERE name='{bookname}'").fetchall()[0][0]

        # make select
        sqlite_select = f"""SELECT name FROM section WHERE book_id={book_id};"""
        sections = cursor.execute(sqlite_select).fetchall()
        return list(map(lambda a: a[0], sections))
    except sqlite3.Error as error:
        print("Failed list", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


# TODO
def well_formed_booktemplate(lines):
    if not "ingestion template" in lines[0]:
        return False # stuff like this
    return True

def dump_to_backups():
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        data = '\n'.join(sqliteConnection.iterdump())
        outfile = open(f"backups/db_backups/backup_{datetime.now().timestamp()}.sql", "w+")
        outfile.write(data)
        outfile.close()
    except sqlite3.Error as error:
        print("Failed baking up db", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
    

def add_book_to_database(subject, name, author, edition):
    try:
        # make database connection
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()

        # grab subject_id by subject name
        subject_id_selection = f"SELECT subject_id FROM subject WHERE name='{subject}';"
        subject_id = cursor.execute(subject_id_selection).fetchall()[0][0]

        # make INSERT 
        sqlite_insert_with_param = """INSERT INTO book
                          (subject_id, name, author, edition) 
                          VALUES (?, ?, ?, ?);"""
        data_tuple = (subject_id, name, author, edition)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
    except sqlite3.Error as error:
        print("Failed failed adding book", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
    

def add_section_to_database(book, section_name, studied, description):
    try:
        # make database connection
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()

        # grab book_id by book name
        book_id = cursor.execute(f"SELECT book_id FROM book WHERE name='{book}'").fetchall()[0][0]

        # make INSERT 
        sqlite_insert_with_param = """INSERT INTO section
                          (book_id, name, studied, description) 
                          VALUES (?, ?, ?, ?);"""
        data_tuple = (book_id, section_name, studied, description) 
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
    except sqlite3.Error as error:
        print("Failed adding section", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

def add_new_problem_to_database(book, section, name):
    try:
        # make database connection
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()

        # grab book_id by book name
        book_id = cursor.execute(f"SELECT book_id FROM book WHERE name='{book}';").fetchall()[0][0]

         # grab section_id by section name
        section_id = cursor.execute(f"SELECT section_id FROM section WHERE name='{section}' AND section.book_id = {book_id};").fetchall()[0][0]                               
        # make INSERT 
        sqlite_insert_with_param = """INSERT INTO problem
                          (book_id, section_id, name, completed)
                          VALUES (?, ?, ?, ?);"""
        data_tuple = (book_id, section_id, name, 0) 
        print(f"data tuple: {book_id} {section_id} {name}")
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
    except sqlite3.Error as error:
        print("Failed adding problem", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

# True if bookname is a book in db
def has_book(bookname):
    try:
        # make database connection
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()

        # grab book_id by book name
        book_id = cursor.execute(f"SELECT book_id FROM book WHERE name='{bookname}';").fetchall()
        if len(book_id) != 0:
            sqliteConnection.close()
            return True
        else:
            sqliteConnection.close()
            return False
    except sqlite3.Error as error:
        print("Failed verifying book name", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
    
def has_section(bookname, section_name):
    try:
        # make database connection
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()

        # grab section with nested subquery
        results = cursor.execute(f"SELECT * FROM section \
                                    WHERE name='{section_name}' \
                                    AND book_id=(SELECT book_id FROM book WHERE name='{bookname}');").fetchall()
        if len(results) != 0:
            sqliteConnection.close()
            return True
        else:
            sqliteConnection.close()
            return False
    except sqlite3.Error as error:
        print("Failed verifying section name", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


def mark_section_as_studied(bookname, section_name):
    try:
        # make database connection
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()

        # grab section with nested subquery
        section_id = cursor.execute(f"SELECT * FROM section \
                                    WHERE name='{section_name}' \
                                    AND book_id=(SELECT book_id FROM book WHERE name='{bookname}');").fetchall()[0][0]
        # update 'studied' field to 1
        today = mydate()
        cursor.execute(f"UPDATE section SET studied=1,date_studied='{today}' WHERE section_id = {section_id};")
        sqliteConnection.commit()
    except sqlite3.Error as error:
        print("Failed verifying book name", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


# given a set of assignment criteria, return the number of problems remaining which meet it
def number_of_problems_meeting_assignment_criteria(books, number_of_problems):
    num = 0
    books = ",".join(list(map(lambda a: "'" + a + "'", books)))
    try:
        # make database connection
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()

        eligible_problems = cursor.execute(f"SELECT * FROM problem \
                                            INNER JOIN section on problem.section_id=section.section_id \
                                            INNER JOIN book on book.book_id = section.book_id  \
                                            WHERE problem.completed = 0 AND section.studied = 1 AND book.name in ({books});").fetchall()
        num = len(eligible_problems)
    except sqlite3.Error as error:
        print("Failed counting elligible problems", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
    return num


# assumes that we have enough problems because we checked already
def get_new_problem_set(books, number_of_problems):
    problems = []
    books = ",".join(list(map(lambda a: "'" + a + "'", books)))
    try:
        # make database connection
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()

        # while still havent grabbed enough problems:
        #     grab random section from random book
        #     grab from problems sorted by number and try to add sequentially
        while len(problems) < number_of_problems:
            eligible_sections = cursor.execute(f"SELECT section.section_id FROM problem \
                                                INNER JOIN section on problem.section_id=section.section_id \
                                                INNER JOIN book on book.book_id = section.book_id  \
                                                WHERE problem.completed = 0 AND section.studied = 1 AND book.name in ({books});").fetchall()
            chosen_section_id = random.choice(eligible_sections)[0]
            problems_in_chosen_section = cursor.execute(f"SELECT problem_id, problem.name, section.name, section.description, book.name FROM problem \
                                                            INNER JOIN section on problem.section_id=section.section_id \
                                                            INNER JOIN book on book.book_id = section.book_id  \
                                                            WHERE problem.completed = 0 AND section.studied = 1 AND book.name in ({books}) \
                                                            AND section.section_id = {chosen_section_id} \
                                                            ORDER BY CAST(problem.name as int) ASC;").fetchall()
            for i in range(len(problems_in_chosen_section)):
                if problems_in_chosen_section[i] in problems:
                    continue
                else:
                    problems.append(problems_in_chosen_section[i])
                break
            
    except sqlite3.Error as error:
        print("Failed generating new problem set", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
    return problems

# given a list of p_ids, mark the corresponding problems as completed in the problems table
def complete(p_ids):
    try:
        # make database connection
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        today = mydate()
        for p_id in p_ids:
            cursor.execute(f"UPDATE problem \
                            SET completed = 1, completion_date = \"{today}\"\
                            WHERE problem_id = {p_id};")
        sqliteConnection.commit()
    except sqlite3.Error as error:
        print("Failed completing problems", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()

