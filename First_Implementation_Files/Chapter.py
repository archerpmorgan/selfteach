class Chapter:

    def __init__(self, name):
        self.name = name
        self.unfinished = {"el":[], "inel":[]}
        self.finished = []

    def add_eligibles(self, list):
        self.unfinished["el"].extend(list)
    
    def add_ineligibles(self, list):
        self.unfinished["inel"].extend(list)
    
    def add_finished(self, list):
        self.finished.extend(list)

    def __str__(self):
        return(self.name + "\n" + str(self.unfinished) + "\n" + str(self.finished) + "\n")
    
    def num_remaining_eligible(self):
        return len(self.unfinished["el"])

    def next_eligible(self):
        return self.unfinished["el"].pop(0)
    
    def has_remaining_eligible(self):
        if len(self.unfinished["el"]) == 0:
            return False
        return True
    
    def complete_problem(self, problem):
        self.finished.append(problem)
        