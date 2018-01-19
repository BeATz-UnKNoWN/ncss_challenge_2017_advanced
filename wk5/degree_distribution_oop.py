import csv
from collections import defaultdict
class Student:
    @staticmethod
    def cap(num):
        return num if num < 99.95 else 99.95
 
    def __init__(self, name, base, courses):
 
        self.bonus = defaultdict(float)
        self.base = float(base)
        self.name = name
        self.courses = []
        self.enrol = None
 
        for i in courses:
            degree, bonus = self.seperate(i)
            self.courses.append(degree)
            self.bonus[degree.code] = bonus
 
    def get_score(self, code):
        return self.cap(self.base + self.bonus[code])
 
    @staticmethod
    def twodp(f):
        return "{:.2f}".format(f)
 
    @staticmethod
    def seperate(course):
        bonus = 0
        suffix = course.rsplit("+", 1)
        if len(suffix)>1:
            bonus = float(suffix[1])
        return degrees[suffix[0]], bonus
 
    def __str__(self):
        return "{},{},{}".format(self.name, self.twodp(self.base), self.enrol.code if self.enrol else '-')
 
    def __lt__(self, other):
        return (self.base, self.name) < (other.base, other.name)
 
    def __gt__(self, other):
        return (self.base, self.name) > (other.base, other.name)
 
    def try_place(self):
        # try to place the student into one of their subjects
        for sub in self.courses:
            if sub.try_accept(self):
                self.enrol = sub
                break
 
    def remove_course(self):
        self.enrol = None
 
    def __repr__(self):
        return str(self)
 
class Degree:
    def __init__(self, code, name, inst, places):
        self.code = code
        self.name = name
        self.total = places
        self.taken = 0
        self.inst = inst
 
 
        self.enrolled = []
    @staticmethod
    def twodp(f):
        return "{:.2f}".format(f)
 
    def __str__(self):
        return "{},{},{},{},{},{}".format(self.code, self.name, self.inst, self.twodp(self.enrolled[-1].get_score(self.code)) if self.enrolled else '-', len(self.enrolled), "Y" if len(self.enrolled) < self.total else "N")
 
    def __repr__(self):
        return str(self)
 
 
    def try_accept(self, student):
        score = student.get_score(self.code)
        cutoff = self.get_cutoff()
 
        # only set cut-off if self.enrolled is full
        if score == cutoff:
            if self.is_full():
                # if the last name in sorted list from smallest to biggest
                temp = self.enrolled[-1]
                if temp.name > student.name:
                    # lexographically after, therefore kick that person out
                    self.evict_replace(student)
                    return True
                else:
                    return False
            else:
                self.add(student)
 
        elif score > cutoff:
            if self.is_full():
                # kick out the last student
                self.evict_replace(student)
            else:
                # still spots, no need to kick anyone out
                self.add(student)
            return True
        else:
            return False
 
    def get_cutoff(self):
        return self.enrolled[-1].get_score(self.code) if len(self.enrolled) >= self.total else 0
 
    def is_full(self):
        return len(self.enrolled) >= self.total
 
 
    def evict_replace(self, student):
        temp = self.enrolled[-1]
        self.enrolled[-1] = student
        self.sort()
 
        temp.remove_course()
        temp.try_place()
 
    def sort(self):
        # sort by descending score, then ascending name
        # ... [largest score, smallest name, largest score, second smallest name ...]
        self.enrolled.sort(key=self.sort_help)
 
    def sort_help(self, x):
        return 1/(x.get_score(self.code)), x.name
 
 
    def add(self, student):
        self.enrolled.append(student)
        self.sort()
 
 
 
 
 
 
    def __lt__(self, other):
        return self.code < other.code
    def __gt__(self, other):
        return self.code > other.code
 
degrees = {}
students = []
 
# for each subject, make a list of ppl who want to do it
 
with open("degrees.csv") as f:
    for line in csv.DictReader(f):
        degrees[line['code']] =Degree(line['code'], line['name'], line['institution'], int(line['places']))
 
with open("students.csv") as f:
    for line in csv.DictReader(f):
        students.append(Student(line['name'], line['score'], line['preferences'].split(";")))
 
 
for i in students:
    i.try_place()
 
de = sorted(degrees.values())
students.sort(key=lambda x: (1/x.base, x.name))
# sort by inverse base, then name
# therefore biggest base will be at the top, then smallest name
# sort by base, then name
print("code,name,institution,cutoff,offers,vacancies")
for i in de:
    print(i)
print()
print("name,score,offer")
for i in students:
    print(i)