import sqliteapi
import sys
import os

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
            for j in range(number_of_problems):
                sqliteapi.add_new_problem_to_database(book_name, section_name, str(j))
        print(f"ingestion of {path} complete" )
    

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
    
# generate a new problem set.
def new_problem_set(books, number_of_problems):
    pass
        

def main():

    #
    #
    #
    sqliteapi.dump_to_backups()
    # quickly make database backup before doing anything else
    #
    #
    #

    if len(sys.argv) < 2:
        print("backed up db")
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
        if len(os.listdir("problem_sets")) is not 0:
            print("Unifinished problem set currently lingers. Consider finishing it or deleting it")
            return 
        print("Okay, will generate a new set. Enter the books you want to pull from in a comma-separated list below.")
        print("Here are your books: ")
        books = sqliteapi.list_books()
        print(books)
        books = input(" ").split(",")
        books = list(map(lambda a: a.strip(), books))
        for book in books:
            if not sqliteapi.has_book(book):
                print(f"The book {book} is not in the database")
                return
        number_of_problems = int(input("How many new problems? "))
        print(f"Okay. Generating a new problem set from these books:{books} with {number_of_problems} problems in it. You can find it in the problem_sets directory.")

if __name__ == "__main__":
    main()