import sys
import random
from Chapter import Chapter

class Textbook:

    def __init__(self, name):
        self.text_reference = ""
        self.chapters = {}
        self.name = name.split("/")[1]

        textfile = open(name)
        # scan to eligibles, read them in
        while(True):
            self.text_reference = textfile.readline()
            if "Text" in self.text_reference:
                break
        while(textfile.readline().find("Eligible") < 0):
            pass
        while(True):
            next_line = textfile.readline().strip()
            if (next_line == ""):
                break
            key = next_line.split(":")[0]
            ps = next_line.split(":")[1].strip().split(" ")
            if ps == ['']:
                continue
            if key in self.chapters.keys():
                self.chapters[key].add_eligibles(ps)
            else:
                self.chapters[key] = Chapter(key)
                self.chapters[key].add_eligibles(ps)
        # scan to ineligibles, read those in
        while(textfile.readline().find("Ineligible") < 0):
            pass
        while(True):
            next_line = textfile.readline().strip()
            if (next_line == ""):
                break
            key = next_line.split(":")[0]
            ps = next_line.split(":")[1].strip().split(" ")
            if ps == ['']:
                continue
            if key in self.chapters.keys():
                self.chapters[key].add_ineligibles(ps)
            else:
                self.chapters[key] = Chapter(key)
                self.chapters[key].add_ineligibles(ps)
        # scan to finished, read those in
        while(textfile.readline().find("Finished") < 0):
            pass
        while(True):
            next_line = textfile.readline().strip()
            if (next_line == ""):
                break
            key = next_line.split(":")[0]
            ps = next_line.split(":")[1].strip().split(" ")
            if ps == ['']:
                continue
            if key in self.chapters.keys():
                self.chapters[key].add_finished(ps)
            else:
                self.chapters[key] = Chapter(key)
                self.chapters[key].add_finished(ps)
        textfile.close()

    def more(self, num):
        # give new problems, don't move them
        count = 0
        problems = []
        while(True):
            rKey = random.choice(list(self.chapters.keys()))
            if self.chapters[rKey].has_remaining_eligible():
                problems.append(rKey + ":" + self.chapters[rKey].next_eligible())
                count+=1
            if count == num:
                break
        return problems

    def finish(self):
        file = open(self.name)
    
    def make_eligible(self, subchapterKey):
        num_moved = 0
    
    def write_out(self):
        # when done with operation, write self back to textbook file
        outfile = open("Current_Textbooks/" + self.name, 'w')
        outfile.write(self.text_reference+"\nStart Unfinished Problems\n\nEligible\n")
        for k in self.chapters.keys():
            newline = k + ": " + " ".join(self.chapters[k].unfinished["el"]) + "\n"
            outfile.write(newline)
        outfile.write("\nIneligible\n")
        for k in self.chapters.keys():
            newline = k + ": " + " ".join(self.chapters[k].unfinished["inel"]) + "\n"
            outfile.write(newline)
        outfile.write("\n")
        outfile.write("\nStart Finished Problems\n")
        for k in self.chapters.keys():
            newline = k + ": " + " ".join(self.chapters[k].finished) + "\n"
            outfile.write(newline)

    def __str__(self):
        for k in self.chapters:
            print(self.chapters[k])

    def num_remaining_eligible(self):
        x = 0
        for c in self.chapters.keys():
            x += self.chapters[c].num_remaining_eligible()
        return x
    
    def complete_problem(self, problem):
        (key, p) = tuple(problem.split(":"))
        print(f'completing {problem}')
        self.chapters[key].complete_problem(p)



    @staticmethod
    def extend_inchoate(filename):
        #TODO check format of inchoate file name, throw exception if bad
        ifile = open(filename)
        inchoate_lines = ifile.readlines()
        #TODO check format, throw exception if bad
        ifile.close()
        new_textbook_contents = []
        # skip inchoate marker, zoom to ineligibles
        i = 1
        while(True):
            new_textbook_contents.append(inchoate_lines[i])
            if inchoate_lines[i].find("Ineligible") >= 0:
                i+=1
                break
            i+=1
        #extend subchapters until read finished problems
        while(True):
            line = inchoate_lines[i]
            if line.find("Fin") >= 0:
                break
            if line.isspace():
                i+=1
                continue
            subchapterKey = line.split(":")[0].strip()
            subchapterNumProblems = int(line.split(":")[1].strip())
            newline = subchapterKey + ":" + " "
            for j in range(1, subchapterNumProblems, 2):
                newline += subchapterKey + "." + str(j) + " "
            new_textbook_contents.append(newline)
            i+=1

        new_textbook_contents.extend(["",inchoate_lines[i]])

        outf = open(filename.split("_")[0] + ".txt", "w")
        for line in new_textbook_contents:
            outf.write(line + "\n")
        outf.close()



