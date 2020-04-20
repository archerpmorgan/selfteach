import sqlite3
import sys
import os
from datetime import datetime
from datetime import date


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
        outfile = open(f"db_backups/backup_{datetime.now().timestamp()}.sql", "w+")
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
        section_id = cursor.execute(f"SELECT section_id FROM section WHERE name='{section}';").fetchall()[0][0]                               
        # make INSERT 
        sqlite_insert_with_param = """INSERT INTO problem
                          (book_id, section_id, name, completed)
                          VALUES (?, ?, ?, ?);"""
        data_tuple = (book_id, section_id, name, 0) 
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
        today = date.today()
        cursor.execute(f"UPDATE section SET studied=1,date_studied='{today}' WHERE section_id = {section_id};")
        sqliteConnection.commit()
    except sqlite3.Error as error:
        print("Failed verifying book name", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()


