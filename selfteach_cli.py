import sqliteapi
import sys
import os
import json
from datetime import datetime
from datetime import date

def bookingestion_parseline(line):
    contents = line.split("->")
    section_name = contents[0].strip()
    description = contents[1].strip()
    number_of_problems = int(contents[2].strip())
    return (section_name, description, number_of_problems)

# import new book into database
def ingest(path):
    with open(path, "r") as file:
        lines = file.read().splitlines() 
        if not sqliteapi.well_formed_booktemplate(lines):
            raise Exception("ill-formed book template")
        book_name = lines[1].split(":")[1].strip()
        subject = lines[2].split(":")[1].strip()
        author = lines[3].split(":")[1].strip()
        edition = int(lines[4].split(":")[1].strip())
        sqliteapi.add_book_to_database(subject, book_name, author, edition)
        for i in range(6, len(lines)):
            # skip line if empty
            if "->" not in lines[i]:
                continue
            # add all the sections and problems
            print(lines[i])
            (section_name, description, number_of_problems) = bookingestion_parseline(lines[i])
            sqliteapi.add_section_to_database(book_name, section_name, 0, description)
            for j in range(1, number_of_problems + 1):
                sqliteapi.add_new_problem_to_database(book_name, section_name, str(j))
        print(f"ingestion of {path} complete")
    

def one_problem_new():
    pass

def one_problem_complete():
    pass

def assignment_new():
    pass

def assignment_complete():
    pass

# interactively mark sections as studied as entered
def studied_sections_interactive(bookname):
    print("That book has the following sections: ")
    print("\n".join(sqliteapi.list_sections(bookname)) + "\n")
    while(True):
        section = input("Enter a section to be recorded as studied (or q for quit): ")
        if section == "q":
            print("All done")
            return
        if not sqliteapi.has_section(bookname, section):
            print("Section not found in this book.")
            continue
        sqliteapi.mark_section_as_studied(bookname, section)
        print(f"Okay, that database now reflects that {section} has been studied.")

# read sections from file and mark as studied
def studied_sections_bulk(bookname, path):
    with open(path) as f:
        sections = f.read().splitlines()
        for section in sections:
            if not sqliteapi.has_section(bookname, section):
                print(f"Section {section} not found in {bookname}.")
                continue
            sqliteapi.mark_section_as_studied(bookname, section)
            print(f"Okay, that database now reflects that {section} has been studied.")
    
# generate a new problem set of incomplete problems from studied sections of the books given.
def new_problem_set(books, number_of_problems):
    problems = sqliteapi.get_new_problem_set(books, number_of_problems)
    with open("problem_sets/assignment.json", 'w+') as outjson:
        outjson.write(json.dumps(problems))
    #build markdown string
    md = "# Current Assignment\n| Book Title | Section Title | Section Name | Problem Number |\n| -- | -- | -- | -- |\n"
    for row in problems:
        md = md + f"|{row[4]}|{row[3]}|{row[2]}|{row[1]}|\n"
    with open("problem_sets/assignment.md", 'w+') as outmd:
        outmd.write(md)

# read in the current assignment and update the data to reflect all problems in it have been done
def complete_problem_set():
    with open("problem_sets/assignment.json", 'r') as injson:
        problems = json.loads(injson.read())

def clear_problem_set():
    files = os.listdir("problem_sets")
    if len(files) == 0:
        print("Nothing to clear.")
    try:
        for file in files:
            os.remove("problem_sets/" + file)
    except Exception as error:
        print(" Failed to delete current problem set: ", error)
    print("All done")

def backup_assignment():
    files = os.listdir("problem_sets")
    if len(files) == 0:
        return
    try:
        for file in files:
            data = ""
            with open("problem_sets/" + file) as f:
                data = f.read()
            with open(f"backups/assignment_backups/backup_assignment_{datetime.now().timestamp()}.txt", "w+") as backupfile:
                backupfile.write(data)
    except Exception as error:
        print(" Failed to backup current problem set: ", error)

# display books in menu format
def display(books):
    displaystr = "\n"
    for i in range(len(books)):
        displaystr = displaystr + str(i) + ": " + books[i] + "\n"
    print(displaystr)


def main():

    #
    #
    sqliteapi.dump_to_backups()
    backup_assignment()
    # quickly make database backup before doing anything else
    #

    if len(sys.argv) < 2:
        print("backed up db")
    if sys.argv[1] == "clear":
            clear_problem_set()
    if sys.argv[1] == "ingest":
            path = sys.argv[2]
            ingest(path)
    if sys.argv[1] == "studied":
        print("Glad you've been studying dringus.")
        print("Here are your books: ")
        books = sqliteapi.list_books()
        print(books)
        bookname = input("Enter a book name: ")
        if not sqliteapi.has_book(bookname):
            print("That book is not in the database")
            return
        # check to see if there is a bulk studied file. If not, do interactive
        if len(sys.argv) == 4:
            if sys.argv[2] == "-file":
                studied_sections_bulk(bookname, sys.argv[3])
            return
        else: 
            studied_sections_interactive(bookname)
        print("done")
    if sys.argv[1] == "generate":
        if len(os.listdir("problem_sets")) != 0:
            print("Unifinished problem set currently lingers. Consider finishing it or deleting it")
            return 
        print("Okay, will generate a new set. Enter the books you want to pull from in a comma-separated list below by index.")
        print("Here are your books: ")
        books = sqliteapi.list_books()
        display(books)
        indices = input(" ").split(",")
        books = list(map(lambda a: a.strip(), books))
        for index in indices:
            book = books[int(index)]
            if not (sqliteapi.has_book(book)):
                print(f"The book {book} is not in the database")
                return
        books = [books[int(i)] for i in indices]
        number_of_problems = int(input("How many new problems? "))
        number_of_problems_meeting_criteria = sqliteapi.number_of_problems_meeting_assignment_criteria(books, number_of_problems)
        if number_of_problems > number_of_problems_meeting_criteria:
            print(f"You asked for {number_of_problems} problems, but only {number_of_problems_meeting_criteria} meet your criteria.")
            return
        print(f"Okay. Generating a new problem set from these books:{books} with {number_of_problems} problems in it.\n\
                A total of {number_of_problems_meeting_criteria} met your desired criteria. You can find it in the problem_sets directory.")
        new_problem_set(books, number_of_problems)
    

if __name__ == "__main__":
    main()