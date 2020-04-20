import sys
import os
import random
from Textbook import Textbook
from datetime import datetime

def build_new_assignment(pairs):
    file = open("Current_Assignment.txt", "w")
    for (book, num) in pairs:
        file.write(book.name + "\n")
        file.write(" ".join(book.more(num)) + "\n\n")

def complete_current_assignment():
    file = open("Current_Assignment.txt", "r")
    contents = file.read().splitlines()
    file.close()
    file = open("Current_Assignment.txt", "w")
    for i in range(0, len(contents)):
        if ".txt" in contents[i]:
            print(f"completing section for {contents[i]}")
            textbook = Textbook("Current_Textbooks/" + contents[i])
            problems = contents[i+1].split(" ")
            for p in problems:
                textbook.complete_problem(p)
            textbook.write_out()
    file.write("empty")
    file.close()

def current_assignment_check():
    file = open("Current_Assignment.txt", "r")
    contents = file.read().strip()
    file.close()
    if contents != "empty":
        print("Current assignment is not complete")
        while(True):
            response = input("Complete current assignment? (y or n): ")
            if response == "y":
                complete_current_assignment()
                return 1
            elif response == "n":
                print("Quitting program; currently must start with empty current assignment.")
                return -1    
            else:
                print("must be (y or n)")
    return 1

def backup():

    infile = open("Current_Assignment.txt", "r")
    contents = infile.read()
    infile.close()
    outfile = open(f"backups/Current_Assignment/Current_Assignment{datetime.now().timestamp()}.txt", "w+")
    outfile.write(contents)
    outfile.close()
    for filename in [x for x in os.listdir("Current_Textbooks") if not (x.startswith('.'))]:
        filename_without_extension = filename.split(".")[0]
        tfile = open("Current_Textbooks/" + filename, "rb")
        contents = tfile.read()
        tfile.close()
        toutfile = open(f"backups/{filename_without_extension}/{filename}{datetime.now().timestamp()}", "w+b")
        toutfile.write(contents)
        toutfile.close()


def main():

    ## Always, first thing, backup current state
    # Includes current assignments and all textbooks
    backup()
    #
    #

    if sys.argv[1] == "generate":
        x = current_assignment_check()
        if x < 0:
           return
        books_and_nums = []
        while(True):
            book = input("Enter a book to sample problems from (q to quit): ")
            if book == "q":
                return
            textbook = Textbook("Current_Textbooks/" + book)
            num = int(input(f"Enter number of new problems you want from {book}: "))
            if textbook.num_remaining_eligible() < num:
                num = textbook.num_remaining_eligible()
                print(f"There are only {num} remaining from {book}, so we're giving you that many.")
            books_and_nums.append((textbook, num))
            response = input("Want to include another book? (y or n): ")
            if response == "n":
                break
        build_new_assignment(books_and_nums)
        for (book, num) in books_and_nums:
            book.write_out()
        return

    if sys.argv[1] == "complete":
        response = input("Are you sure you want to complete the current assignment? (y or n) ")
        if response == "y":
            complete_current_assignment()
        else:
            print("Quitting program")
        return

    if sys.argv[1] == "move":
        if sys.argv[2] == "eligible":
            #expecting a book name and subchaptername to be provided
            book = sys.argv[3]
            subchapter = sys.argv[4] #default behavior is move everything whose key begins with the one provided
            num_moved = textbooks[book]

            print("total chapters moved = ")
    if sys.argv[1] == "inchoate":
        if sys.argv[2] == "extend":
            book = input("Enter a book name to extend (q to quit): ")
            if book == "q":
                return
            skip_evens = input("Do you want to skip evens? (y or n, q to quit): ")
            Textbook.extend_inchoate(book, skip_evens)
            return
    
    print("arguments not recognized")


if __name__ == '__main__':
    main()