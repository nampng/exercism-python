class School:
    def __init__(self):
        self.grade_dict = {}

    def add_student(self, name, grade):
        if grade in self.grade_dict:
            self.grade_dict[grade].append(name)
        else:
            self.grade_dict[grade] = [name]

        self.grade_dict[grade].sort()

    def roster(self):
        key_list = list(self.grade_dict.keys())
        key_list.sort()
        roster_list = [self.grade_dict[key] for key in key_list]
        print(roster_list)
        flat_roster = [name for grade in roster_list for name in grade]
        print(flat_roster)
        return flat_roster


    def grade(self, grade_number):
        if grade_number in self.grade_dict:
            return self.grade_dict[grade_number]
        else:
            return []
