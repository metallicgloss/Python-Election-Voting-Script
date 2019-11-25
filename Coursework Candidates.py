##Not yet working

class Candidates:

    def __init__(self, position, candidate_name):
        self.position = position
        self.candidate_name = candidate_name

    def get_info(self):
        with open('GSUCandidates.txt') as f:
            if candidate_name in f.read():
                return ""
            else:
                return "%s is applying for %s"%(self.candidate_name, self.position)


    def insert_new_candidate(self):
        x = 0
        while x == 0:
            choice = input("Type 'Yes' if you want to add a new candidate or 'No' if not: ")
            #while choice == 'Yes':
            if choice == "Yes" or choice == "yes" or choice == "Y" or choice == "y":
                self.position, self.candidate_name = input("Enter position applied for then your name").split(",")
                with open('GSUCandidates.txt') as f:
                    if candidate_name in f.read():
                        print("You can't enter more than once!\n")

                        f.close()
                        pass
                    else:
                        candidate = Candidates(position, candidate_name)
                       # candidates.append(candidate)
                        f = open("GSUCandidates.txt", "a+")
                        f.write(self.position + "," + self.candidate_name + "\n")
                        f.close()


            elif choice == "No" or choice == "no" or choice == "N" or choice == "n":
                x = 1
            else:
                print("Not a valid choice")
                pass


i = 0
candidates = []
f = open("GSUCandidates.txt", "r")
for line in f:
    if i > 0:
        position, candidate_name = line.split(",")
        candidate = Candidates(position, candidate_name)
        candidates.append(candidate)
    i = i + 1
f.close()



candidate.insert_new_candidate()

for candidate in candidates:
    print(candidate.get_info())





